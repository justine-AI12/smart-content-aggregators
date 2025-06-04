# Smart Content Aggregator 🚀

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-4.2-brightgreen.svg)](https://www.djangoproject.com/)
[![MongoDB](https://img.shields.io/badge/MongoDB-6.0-green.svg)](https://www.mongodb.com/)

Un agrégateur de contenu intelligent qui collecte, analyse et classe automatiquement des articles de presse en utilisant :
- Web scraping et RSS
- Traitement NLP (résumé, mots-clés)
- Stockage flexible avec MongoDB

## Fonctionnalités clés ✨

- **Collecte multi-sources** : RSS, scraping direct
- **Analyse intelligente** :
  - Résumé automatique des articles
  - Extraction de mots-clés
  - Catégorisation thématique
- **Interface d'administration** complète
- **API REST** intégrée

## Architecture 🏗️

```plaintext
django/
├── apps/
│   ├── content_aggregator/    # Cœur métier
│   └── users/                 # Authentification
├── aggregator_core/           # Configuration
└── static/                    # Assets frontend

mongodb/                       # Base de données
celery/                        # Tâches asynchrones
Prérequis 💻
Python 3.10+

MongoDB 6.0+

Git

Compte GitHub (optionnel)

Installation 🛠️
1. Configuration de base
bash
# Clonez le dépôt
git clone https://github.com/votre-utilisateur/smart-content-aggregator.git
cd smart-content-aggregator

# Créez l'environnement virtuel (Windows)
python -m venv .venv
.\.venv\Scripts\activate
2. Installation des dépendances
bash
pip install -r requirements.txt

# Pour le développement
pip install -r requirements_dev.txt
3. Configuration MongoDB
Démarrer le service :

powershell
net start MongoDB
Créer la base de données :

javascript
use content_aggregator
db.createUser({user: "admin", pwd: "password", roles: ["readWrite"]})
4. Variables d'environnement
Créez un fichier .env à la racine :

ini
DEBUG=1
SECRET_KEY=votre_cle_secrete_ici
MONGO_URI=mongodb://admin:password@localhost:27017/content_aggregator?authSource=admin
Utilisation 🚦
Lancer le serveur de développement
bash
python manage.py runserver
Commandes utiles
Commande	Description
python manage.py fetch_articles	Collecte les nouveaux articles
python manage.py process_content	Analyse le contenu avec NLP
python manage.py createsuperuser	Crée un admin Django
Structure des données 📊
python
class Article(Document):
    title: str                   # Titre de l'article
    source: str                  # URL source
    content: str                 # Texte intégral
    summary: str                 # Résumé généré
    keywords: List[str]          # Mots-clés (NLP)
    published_at: datetime       # Date publication
    is_processed: bool = False   # Statut traitement
API Endpoints 🌐
Endpoint	Méthode	Description
/api/articles/	GET	Liste tous les articles
/api/articles/{id}/	GET	Détail d'un article
/api/sources/	POST	Ajouter une nouvelle source
Contribution 🤝
Forkez le projet

Créez une branche (git checkout -b feature/amelioration)

Commitez vos changements (git commit -m 'Ajout feature')

Poussez vers la branche (git push origin feature/amelioration)

Ouvrez une Pull Request

Licence 📜
Ce projet est sous licence MIT - voir le fichier LICENSE pour plus de détails.
