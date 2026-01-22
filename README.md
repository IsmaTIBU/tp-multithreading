TP Multithreading et Systèmes Distribués
Ce dépôt contient une série d'exercices (TP) axés sur le multi-threading en Python et l'informatique distribuée utilisant une architecture hybride C++/Python.

🛠 Prérequis
Python (Tous les TPs)
Python 3.12+

Flask & Requests : Nécessaires pour le Proxy du TP4.

Bash

sudo apt install python3-flask python3-requests
C++ (TP4 uniquement)
Compilateur : GCC/G++.

Bibliothèques : Eigen3, nlohmann-json, et CPR (C++ Requests).

Bash

sudo apt install cmake g++ libcurl4-openssl-dev libeigen3-dev nlohmann-json3-dev
🚀 Comment exécuter chaque TP
TP1 : Logique de base & Multithreading
Se concentre sur la classe Task et la logique de résolution de matrices.

Exécuter les tests unitaires : Valide la précision mathématique du solveur.

Bash

python3 test_task.py
TP2 : Gestionnaire distribué Python
Utilise multiprocessing.managers pour créer une architecture Boss/Minion.

Terminal 1 (Manager) : python3 tp2/manager.py

Terminal 2 (Minion) : python3 tp2/minion.py

Terminal 3 (Boss) : python3 tp2/boss.py

TP3 : Sérialisation JSON
Se concentre sur la conversion des objets Task en chaînes JSON pour la transmission réseau.

Exécuter les tests unitaires :

Bash

python3 tp3/test_task_json.py
TP4 : Système distribué hybride C++/Python
Un système multi-langages où un Proxy Python coordonne des clients C++ via HTTP.

Compiler les clients C++ :

Bash

cd tp4
mkdir build && cd build
cmake ..
make
Terminal 1 (Proxy) : Exécuter depuis la racine du dossier tp4.

Bash

python3 proxy.py
Terminal 2 (Minion) : Exécuter depuis tp4/build.

Bash

./minion
Terminal 3 (Boss) : Exécuter depuis tp4/build.

Bash

./boss
📂 Structure du projet
tp1/ : Logique de base et implémentation initiale des tâches.

tp2/ : Calcul distribué via le BaseManager de Python.

tp3/ : Sérialisation JSON et gestion de l'état des objets.

tp4/ : Implémentation C++ haute performance avec un concentrateur API REST Python.