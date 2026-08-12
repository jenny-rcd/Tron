#  Jeu Tron en Python

Bienvenue sur le projet **Tron**, une réimplémentation en Python du célèbre jeu d'arcade rétrofuturiste. Ce projet a été conçu de A à Z en gérant à la fois l'interface visuelle (Front-end) et la logique algorithmique du jeu (Back-end) se projet a été réaliser quand j'était en première dans la cadre d'un projet de NSI.

##  Fonctionnalités Principales

* **Interface & Visuels (Front-end) :**
  * Création d'un menu, d'une leaderboard et d'un menu pour sélectionner le nombre de joueur
  * Gestion de l'affichage en temps réel du plateau et des obstacles.

* **Moteur & Logique de jeu (Back-end) :**
  * **Gestion des événements clavier :** Déplacements fluides et réactifs des motos lumineuses.
  * **Détection des collisions :** Algorithme calculant en temps réel les collisions avec les bordures de la carte, les traînées laissées par les joueurs et les obstacles.
  * **Conditions de victoire :** Gestion de la fin de partie, du score et de la réinitialisation du jeu.

---

## 🛠️ Stack Technique

* **Langage :** Python 
* **Bibliothèques utilisées :** Pygame 

---

## Installation et Exécution

Voici la procédure complète pour compiler les sources et lancer le jeu:

```bash
git clone git@github.com:jenny-rcd/Tron.git
cd ./Tron
pip install pygame (a faire si pygame n'est pas installer)
python Tron.py
```

