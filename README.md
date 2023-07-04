# CppPybindHMACSHA512


## HMACSHA512 Python API

Introduction

Ce README fournit des instructions sur comment construire et utiliser l'API HMACSHA512 qui est implémentée en Python avec une extension C++.

Pré-requis

Un système d'exploitation basé sur Debian (testé sur Debian, mais devrait fonctionner sur d'autres distributions comme Ubuntu).
Les packages suivants doivent être installés:

build-essential
cmake
mingw-w64

## Instructions d'installation

### Étape 1: Installation des dépendances
Ouvrez un terminal et exécutez les commandes suivantes pour installer les packages nécessaires:

```

sudo apt-get update
sudo apt-get install build-essential cmake mingw-w64
```

### Étape 2: Cloner le dépôt
Clonez le dépôt contenant le code source de l'API :

```

git clone https://github.com/ElAm1ne/CppPybindHMACSHA512.git

```

### Étape 3: Installer les dépendances Python
Dans le répertoire du projet, installez les dépendances Python en exécutant :

```

pip install -r requirements.txt

```

### Étape 4: Compiler le code
Allez dans le répertoire du projet et construisez le code :

```

cd CppPybindHMACSHA512
cd build
cmake ..
make
```

Test de l'API

Après avoir construit l'API, vous pouvez tester son fonctionnement en exécutant le script de test test_python.py à partir du dossier parent CppPybindHMACSHA512 :

```

python3 test_python.py
```

Si les tests sont passés avec succès, vous êtes prêt à utiliser l'API HMACSHA512.

Utilisation de l'API

Pour générer un HMAC à l'aide d'une clé et d'un message, vous pouvez exécuter le script de l'API de la manière suivante :

```

python3 nom_du_fichier.py <key> <message>

```

où <key> est votre clé de 512 bits en format hexadécimal et <message> est le message pour lequel vous souhaitez générer un HMAC. Remplacez nom_du_fichier.py par le nom réel de votre fichier Python. Si la clé ou le message ne sont pas conformes, une erreur sera renvoyée.
