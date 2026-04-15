# TRUSTIA

Application Django pour la gestion de produits et de factures.

## Setup

```bash
# Environnement virtuel
python -m venv venv
.\venv\Scripts\Activate.ps1  # Windows
source venv/bin/activate      # Linux/Mac

# Dépendances
pip install -r requirements.txt

# Base de données
python manage.py migrate

# Serveur
python manage.py runserver
```

L'interface est disponible à `http://localhost:8000/products/`

## Fonctionnalités

- Gestion des produits (CRUD)
- Gestion des factures avec articles
- Interface d'administration Django
- Pagination automatique
# TRUSTIA - Système de Gestion de Facturation

Bienvenue dans **TRUSTIA**, une application Django complète pour gérer des produits et générer des factures. Ce projet inclut une interface web full-stack avec Django, SQLite, HTML & CSS (Bootstrap 5).

## 🚀 Installation et Démarrage

### 1. Créer un environnement virtuel (si ce n'est pas fait)
```powershell
python -m venv venv
```

### 2. Activer l'environnement virtuel

**Sur Windows (PowerShell) :**
```powershell
.\venv\Scripts\Activate.ps1
```

**Sur Windows (CMD) :**
```cmd
venv\Scripts\activate.bat
```

**Sur macOS/Linux :**
```bash
source venv/bin/activate
```

### 3. Installer les dépendances
```bash
pip install -r requirements.txt
```

### 4. Accéder au dossier du projet
```bash
cd trustia_project
```

### 5. Appliquer les migrations de base de données
```bash
python manage.py migrate
```

### 6. Créer les migrations pour l'app invoicing
```bash
python manage.py makemigrations invoicing
python manage.py migrate invoicing
```

### 7. Créer un superutilisateur (administrateur)
```bash
python manage.py createsuperuser --noinput --username admin --email admin@local.com
```

Puis définir le mot de passe avec le script fourni **OU** utiliser :
```powershell
Get-Content create_admin.py | python manage.py shell
```

**Identifiants par défaut :**
- **Utilisateur :** admin
- **Mot de passe :** admin123

### 8. (Optionnel) Charger les données de test
```powershell
Get-Content init_data.py | python manage.py shell
```

Cela créera :
- 5 produits d'exemple
- 2 factures d'exemple avec articles

### 9. Lancer le serveur de développement
```bash
python manage.py runserver
```

L'application sera maintenant accessible à : **http://localhost:8000/**

## 📋 Accès à l'Interface d'Administration

1. Allez à : **http://localhost:8000/admin/**
2. Connectez-vous avec :
   - **Utilisateur :** admin
   - **Mot de passe :** admin123
3. Gérez les produits et factures depuis l'interface Django Admin

## 📦 Fonctionnalités

### Gestion des Produits
- ✅ Créer un produit
- ✅ Modifier un produit
- ✅ Supprimer un produit
- ✅ Afficher la liste des produits (avec pagination)
- ✅ Afficher le détail d'un produit

### Gestion des Factures
- ✅ Créer une facture
- ✅ Ajouter des produits à une facture
- ✅ Modifier les quantités
- ✅ Supprimer des produits d'une facture
- ✅ Afficher le détail d'une facture
- ✅ Voir le total et le nombre de produits
- ✅ Pagination des listes

## 🏗️ Structure du Projet

```
trustia_project/
├── manage.py                  # Utilitaire de gestion Django
├── db.sqlite3                 # Base de données (créée après migrate)
├── requirements.txt           # Dépendances du projet
├── trustia_project/           # Configuration du projet
│   ├── __init__.py
│   ├── settings.py            # Paramètres Django
│   ├── urls.py                # URLs principales
│   └── wsgi.py                # Configuration WSGI
├── invoicing/                 # Application de facturation
│   ├── models.py              # Modèles (Product, Invoice, InvoiceItem)
│   ├── views.py               # Vues (ListView, CreateView, etc.)
│   ├── urls.py                # URLs de l'application
│   ├── forms.py               # Formulaires
│   ├── admin.py               # Configuration Admin
│   └── migrations/            # Migrations de base de données
├── templates/                 # Templates HTML
│   ├── base.html              # Template de base
│   └── invoicing/             # Templates de l'application
│       ├── product_*.html
│       └── invoice_*.html
└── static/                    # Fichiers statiques (CSS, JS, images)
```

## 📊 Modèles de Données

### Product
- `name` : Nom du produit (CharField)
- `price` : Prix du produit (DecimalField)
- `expiration_date` : Date de péremption (DateField)
- `created_at` : Date de création (DateTimeField, auto)
- `updated_at` : Date de modification (DateTimeField, auto)

### Invoice
- `invoice_number` : Numéro unique de facture (CharField)
- `created_at` : Date de création (DateTimeField, auto)
- `updated_at` : Date de modification (DateTimeField, auto)

### InvoiceItem
- `invoice` : Lien vers une facture (ForeignKey)
- `product` : Lien vers un produit (ForeignKey)
- `quantity` : Quantité (IntegerField)
- `unit_price` : Prix unitaire au moment de l'achat (DecimalField)

## 🎨 Interface

L'application utilise **Bootstrap 5** pour un design moderne et responsive :
- Navigation élégante
- Cartes stylisées
- Boutons colorés
- Pagination intuitive
- Messages d'alerte pour le feedback utilisateur

## 🛠️ Commandes Utiles

### Créer les tables (migrations)
```bash
python manage.py migrate
```

### Créer un superutilisateur
```bash
python manage.py createsuperuser
```

### Faire des migrations après modification de modèles
```bash
python manage.py makemigrations
python manage.py migrate
```

### Lancer la console de test
```bash
python manage.py shell
```

### Collecter les fichiers statiques
```bash
python manage.py collectstatic
```

## 💡 Notes Importantes

1. **Base de données** : Par défaut, SQLite est utilisé (db.sqlite3). Parfait pour le développement.
2. **Admin** : Accédez à l'interface admin sur `/admin/` avec votre compte superutilisateur.
3. **DEBUG** : DEBUG est activé dans `settings.py` (changez en production).
4. **STATIC_FILES** : Les fichiers CSS/JS de Bootstrap sont servis via CDN.

## 🚀 Déploiement

Pour déployer en production :
1. Changez `DEBUG = False` dans `settings.py`
2. Generez une nouvelle `SECRET_KEY`
3. Configurez `ALLOWED_HOSTS` avec votre domaine
4. Utilisez un serveur d'application (Gunicorn, uWSGI)
5. Mettez en place une base de données PostgreSQL

## 📞 Support

Pour toute question, consultez la [documentation Django officielle](https://docs.djangoproject.com/).

---

✨ **Créé avec Django** - Test Technique TRUSTIA 2026
