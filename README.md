<img width="1024" height="1024" alt="image" src="https://github.com/user-attachments/assets/9e9afe47-917b-4d5a-b6dd-c6ae96da8608" />

# 🔐 Moteur de Détection de Fuites de Données (DLP) — *Groupe Asten*

![Banner](https://img.shields.io/badge/FastAPI-0.115.0-009688?logo=fastapi)
![Banner](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![Banner](https://img.shields.io/badge/MSP-Sujet%208-orange)

---

## 📖 Contexte du projet

L’entreprise **Groupe Asten** manipule régulièrement des documents sensibles (*rapports internes, données RH, informations clients*).
Afin d’éviter toute fuite de données critiques, nous avons développé un **moteur DLP (Data Loss Prevention)**.

Ce moteur permet :

* d’analyser des fichiers **PDF** et **TXT**,
  
* de détecter des informations sensibles (IBAN, CB, NIR, mails, téléphones…),
* de calculer un **score de criticité**,
  
* de décider d’une action (LOG, WARN, ALERT, BLOCK),
  
* et de **générer un rapport PDF clair et professionnel**.

---

## ✨ Fonctionnalités principales

✔️ **Analyse en profondeur** des documents internes
✔️ **Détection multi-règles** (IBAN, carte bancaire, email, NIR, téléphone, …)
✔️ **Score de risque automatique** pondéré selon le canal (Email, Partage, Git, …)
✔️ **Interface Web moderne** avec upload et visualisation instantanée
✔️ **Tableau de détection** avec poids, confiance et valeurs caviardées
✔️ **Thermomètre dynamique** affichant le niveau de risque
✔️ **Export PDF professionnel** (mise en page, tableau, aperçu, pagination)
✔️ **API REST JSON** utilisable via Swagger ou cURL
✔️ **Logs complets** dans `analysis.log` pour audit et traçabilité

---

## 🏗️ Architecture du projet

```bash
Mise-en-SP-Sujet-8/
│
├── src/
│   ├── api.py                # FastAPI + UI + API JSON + Export PDF
│   ├── detection/
│   │   ├── detector.py       # Détection des patterns sensibles
│   │   ├── rules.py          # Règles (regex) + poids
│   │   ├── scorer.py         # Calcul du score
│   │   └── redact.py         # Caviardage
│   └── utils/
│       └── file_parser.py    # Lecture PDF & TXT
│
├── templates/                # Pages HTML (upload + résultats)
│   ├── upload.html
│   └── result.html
│
├── static/                   # CSS, images
│   └── style.css
│
├── tests/                    # Tests unitaires (pytest)
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation & Lancement

### 1️⃣ Cloner le projet

```bash
git clone https://github.com/<utilisateur>/<repo>.git
cd <repo>
```

### 2️⃣ Créer un environnement virtuel (optionnel)

```bash
python3 -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

### 3️⃣ Installer les dépendances

```bash
pip install -r requirements.txt
```

### 4️⃣ Démarrer le serveur

```bash
uvicorn src.api:app --host 0.0.0.0 --port 8000 --reload
```

🔗 Accès à l’application : [http://localhost:8000](http://localhost:8000)

---

## 🖥️ Interface utilisateur

### 🏠 Page d’accueil

➡️ Upload d’un fichier (drag & drop ou clic)
➡️ Choix du canal (Email / Partage / Inconnu)
➡️ Explications simples et claires

---

### 📊 Résultats d’une analyse

* Résumé : fichier, canal, score, décision
* **Tableau des détections** avec poids et confiance
* **Thermomètre de risque** dynamique
* **Aperçu caviardé** du texte sensible
* Boutons pour :

  * 📋 Copier le JSON
  * 📥 Télécharger le JSON
  * 🧾 Exporter un rapport PDF

---

## 📑 Exemple concret

### Entrée (tests/exemple.txt)

```
RIB ACME: FR7630006000011234567890189
Carte test 4539 1488 0343 6467
Mail: jean.dupont@example.com
Téléphone: +33 6 12 34 56 78
```

### Sortie (résumé)

```
Canal : email
Score : 18
Décision : BLOCK 🚨
```

### Résultats détectés

| Règle    | Match                                                     | Confiance | Poids |
| -------- | --------------------------------------------------------- | --------- | ----- |
| IBAN\_FR | FR7630006000011234567890189                               | 0.99      | 7     |
| PAN      | 4539 1488 0343 6467                                       | 0.99      | 9     |
| EMAIL    | [jean.dupont@example.com](mailto:jean.dupont@example.com) | 0.90      | 2     |

---

## 📑 Export PDF

👉 Le bouton **Exporter PDF** génère un rapport au format professionnel :

* Titre & en-tête (fichier, canal, score, décision colorée)
* Tableau des détections
* Aperçu du texte caviardé (monospace)
* Footer avec pagination

---

## 📜 Logs & Tests

### 🔎 Logs (analysis.log)

Chaque analyse est consignée :

```
2025-08-30 16:12:04,171 - INFO - Analyse effectuée - 
Fichier: RIB-Omnes.pdf, Canal: share, Score: 19, Décision: BLOCK, Règles détectées: 2
```

### ✅ Tests unitaires

```bash
PYTHONPATH=. pytest -q
```

Résultat attendu :

```
8 passed in 0.20s
```

---

## 🚧 Limites actuelles

⚠️ Taille max des fichiers non encore limitée (gros PDF → risque crash)
⚠️ Résultats non stockés en base (juste export PDF/JSON)
⚠️ Pas encore de Docker ni de reverse proxy HTTPS
⚠️ Pas de dashboard admin ni d’intégration SIEM

---

## 🔮 Améliorations futures

🚀 **Docker + reverse proxy HTTPS** : déploiement sécurisé et facile
📊 **Dashboard admin (Grafana/Loki)** : visualisation temps réel des logs
🛡️ **Intégration SIEM (Splunk/ELK)** : centralisation sécurité

---

## 👥 Auteurs & Équipe

👨‍💻 Développé par Angea Renza— Sujet 8
🎓 Étudiants ECE Paris — Spécialisation **Data & IA**
📅 Date limite : **10 septembre 2025**

---

