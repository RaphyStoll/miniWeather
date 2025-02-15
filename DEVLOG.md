# DevLog - Mini Weather

## Introduction

Ce journal de bord retrace les étapes de développement du projet Mini Weather, en mettant en lumière
les objectifs, les accomplissements, les défis rencontrés et les fonctionnalités qui auraient pu
être implémentées avec plus de temps.

## Jour 1 - 13 Février 2025

### Objectifs du Jour

- **Bases :**
  - Définir les besoins (technologies, frameworks, etc.).
  - Mise en place de l'environnement de développement.
  - Structuration des dossiers.
- **Interface Basique :**
  - Création d'une fenêtre.
  - Ajout d'une barre de recherche.
  - Mise en place d'une zone d'affichage.

### Accomplissements

- Définition des besoins du projet.
- Mise en place de la logique de l'API :
  - Récupération des prévisions météo actuelles et sur 5 jours.
  - Gestion des dépassements d'appels via le code d'erreur 429.
- Mise en place de tests pour s'assurer de la récupération correcte des données de l'API.

### Défis et Solutions

- **Défi :** Intégration de l'API avec gestion des erreurs.
- **Solution :** Implémentation de la gestion des erreurs 429 pour éviter les dépassements d'appels.

## Jour 2 - 14 Février 2025

### Objectifs du Jour

- **Interface Basique :**
  - Création d'une fenêtre.
  - Ajout d'une barre de recherche.
  - Mise en place d'une zone d'affichage.

### Accomplissements

- Journée de documentation :
  - Lecture de la documentation de Tkinter, qui sera notre framework d'interface.
  - Révision des objectifs du projet.

### Apprentissages

- Meilleure compréhension des capacités et des limites de Tkinter.

## Jour 3 - 15 Février 2025

### Objectifs du Jour

- **Interface Basique :**
  - Création d'une fenêtre.
  - Ajout d'une barre de recherche.
  - Mise en place d'une zone d'affichage.
- Mise en place de certains bonus.

### Accomplissements

- Création de l'interface.
- Mise en place d'un cache pour réduire les appels à l'API.
- Gestion des favoris.
- Optimisation de l'interface.
- Mise en place d'un focus sur la barre de recherche au lancement.

### Réflexions

- Tkinter est un bon point de départ, mais un framework plus avancé pourrait offrir une meilleure
  expérience utilisateur.

## Fonctionnalités Manquantes

- Utilisation d'un framework d'interface plus avancé que Tkinter pour une meilleure expérience
  utilisateur.
- Responsivité du cadre de la météo actuelle.
- Création de comptes utilisateur.
- Gestion d'une base de données centralisée pour réduire les requêtes API et permettre une meilleure
  modularité.
- Mise en place d'une section "Quick City" pour afficher les villes favorites et leurs données
  actuelles sur la page d'accueil.

## Prochaines Étapes

- Explorer d'autres frameworks d'interface pour de futurs projets.
- Continuer à optimiser et à ajouter des fonctionnalités basées sur le feedback des utilisateurs.
