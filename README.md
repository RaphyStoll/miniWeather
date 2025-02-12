# DSQ #1 - Mini Weather Dashboard

## 🎮 Dev Side Quests ?
Ce projet fait partie des [Dev Side Quests](https://github.com/RaphyStoll/Dev-Side-Quests-DSQ), une série de défis personnels de développement en temps limité. Chaque quête est une opportunité d'explorer de nouvelles technologies et de s'améliorer en gestion de projet.

## 📋 Info Quest
- **Niveau**: Débutant
- **Temps Max**: 3 jours (sessions de 8h)
- **Classes Suggérées**: Python, JavaScript, Java
- **Type**: Application de bureau

## 🎯 Objectifs
Créer une application de bureau qui permet aux utilisateurs de :
- Rechercher la météo d'une ville
- Voir les conditions météorologiques actuelles
- Consulter les prévisions sur 3 jours
- Sauvegarder une ville favorite

## 💻 Mon Implémentation (Python)

### Prérequis
- Python 3.8 ou supérieur
- pip (gestionnaire de paquets Python)

### Installation
1. Clonez le repository :
```bash
git clone https://github.com/RaphyStoll/miniWather.git
cd miniWather
```

2. Installez les dépendances avec Poetry :
```bash
# Si Poetry n'est pas installé
curl -sSL https://install.python-poetry.org | python3 -

# Installation des dépendances
poetry install
```

4. Configurez votre clé API OpenWeatherMap :
   - Créez un compte sur [OpenWeatherMap](https://openweathermap.org/)
   - Obtenez une clé API gratuite
   - Créez un fichier `.env` à la racine du projet :
     ```
     OPENWEATHER_API_KEY=votre_clé_api
     ```

### Lancement
```bash
python main.py
```

### Structure des Fichiers
```
miniWather/
├── main.py
├── weather_api.py
├── gui.py
├── requirements.txt
├── .env
└── README.md
```

### Fonctionnalités Implémentées
- 🔍 Recherche de ville
- 🌡️ Affichage de la température actuelle
- 💧 Indication du taux d'humidité
- 🌤️ Icônes météo
- 📅 Prévisions sur 3 jours
- ⭐ Sauvegarde d'une ville favorite

### Captures d'écran
[Insérez vos captures d'écran ici]

### Points d'amélioration possibles
- Ajout de plusieurs villes favorites
- Graphiques de température
- Alertes météo
- Support de la géolocalisation
- Mode sombre

### Licence
Ce projet est sous licence GNU GPL v3. Cette licence garantit que :
- Le code source reste toujours accessible
- Toute modification ou extension doit être partagée sous la même licence
- La liberté du code est préservée et transmise
- Les utilisateurs ont le droit d'étudier, modifier et partager le code

Voir le fichier `LICENSE` pour plus de détails.
