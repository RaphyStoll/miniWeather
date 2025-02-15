# DSQ #1 - Mini Weather Dashboard

![Status](img/Badge%20de%20statut%20iPhone%20Vlog.svg)

## 🎮 Dev Side Quests ?

Ce projet fait partie des [Dev Side Quests](https://github.com/RaphyStoll/Dev-Side-Quests-DSQ), une
série de défis personnels de développement en temps limité. Chaque quête est une opportunité
d'explorer de nouvelles technologies et de s'améliorer en gestion de projet.

## 📋 Info Quest

- **Niveau**: Débutant
- **Temps Max**: 3 jours
- **Classes Suggérées**: Python, JavaScript, Java
- **Type**: Application de bureau
- [📔 DevLog](https://github.com/RaphyStoll/miniWeather/DEVLOG.md)

## 🎯 Objectifs

Créer une application de bureau qui permet aux utilisateurs de :

- Rechercher la météo d'une ville
- Voir les conditions météorologiques actuelles
- Consulter les prévisions sur x jours
- Sauvegarder une ville favorite

## 💻 Mon Implémentation (Python)

### Devlog

Pour plus de détails sur le processus de développement, les décisions prises et les défis
rencontrés, je vous invite à lire les [devlog](https://github.com/RaphyStoll/miniWeather/DEVLOG.md)

### Prérequis

- Python 3.8 ou supérieur
- poetry (gestionnaire de paquets Python)

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
     API_KEY=<votre_clé_api>
     ```

### Lancement

```bash
poetry run python3 main.py
```

### Structure des Fichiers

```
miniWather/
├── img/
│   ├── Badge de statut complet.svg
│   └── Badge de statut en cours.svg
├── src/
│   ├── api/
│   │   ├── __init__.py
│   │   └── weather_api.py
│   ├── cache/
│   │   └── cache_manager.py
│   ├── data/
│   │   └── favorites.json
│   └── ui/
│       ├── search_bar.py
│       └── weather_display.py
├── .gitignore
├── DEVLOG.MD
├── LICENSE
├── pyproject.toml
├── poetry.lock
└── README.md

```

### Fonctionnalités Implémentées

- 🔍 Recherche de ville
- 🌡️ Affichage de la température actuelle
- 💧 Indication du taux d'humidité
- 🌤️ description
- 📅 Prévisions sur 3 jours
- ⭐ Sauvegarde de cinq ville favorite

### Captures d'écran

![test](/img/prog_test.png)

### Points d'amélioration possibles

- Graphiques de température
- Alertes météo
- Support de la géolocalisation
- Mode sombre / claire

### Licence

Ce projet est sous licence GNU GPL v3. Cette licence garantit que :

- Le code source reste toujours accessible
- Toute modification ou extension doit être partagée sous la même licence
- La liberté du code est préservée et transmise
- Les utilisateurs ont le droit d'étudier, modifier et partager le code

Voir le fichier `LICENSE` pour plus de détails.
