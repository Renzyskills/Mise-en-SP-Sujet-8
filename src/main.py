import re
import pdfplumber
import docx
import os
import argparse

# Regex simples pour détecter des infos sensibles
PATTERNS = {
    "email": r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-z]{2,}",
    "téléphone": r"\b(?:\+33|0)[1-9](?:[ .-]?\d{2}){4}\b",
    "carte_bancaire": r"\b(?:\d[ -]*?){13,16}\b",
}

def extract_text_from_pdf(path):
    text = ""
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text

def extract_text_from_docx(path):
    doc = docx.Document(path)
    return "\n".join([para.text for para in doc.paragraphs])

def extract_text(path):
    ext = os.path.splitext(path)[1].lower()
    if ext == ".txt":
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    elif ext == ".pdf":
        return extract_text_from_pdf(path)
    elif ext == ".docx":
        return extract_text_from_docx(path)
    else:
        raise ValueError("Format non supporté: " + ext)

def scan_text(text):
    results = {}
    for label, pattern in PATTERNS.items():
        matches = re.findall(pattern, text)
        if matches:
            results[label] = matches
    return results

def main():
    parser = argparse.ArgumentParser(description="Scanner de fuites de données")
    parser.add_argument("path", help="Chemin du document à analyser")
    args = parser.parse_args()

    text = extract_text(args.path)
    results = scan_text(text)

    print("\n=== Résultats de l'analyse ===")
    if results:
        for category, items in results.items():
            print(f"- {category}: {items}")
    else:
        print("Aucune donnée sensible détectée.")

if __name__ == "__main__":
    main()

