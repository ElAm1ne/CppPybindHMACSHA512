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
python3.9

## Instructions d'installation

### Étape 1: Installation des dépendances
Ouvrez un terminal et exécutez les commandes suivantes pour installer les packages nécessaires:

```

sudo apt-get update
sudo apt-get install build-essential cmake mingw-w64 python3.9
```

### Étape 2: Cloner le dépôt
Clonez le dépôt contenant le code source de l'API :

```

git clone https://github.com/ElAm1ne/CppPybindHMACSHA512.git

```

### Étape 3: Compiler le code
Allez dans le répertoire du projet et construisez le code :

```

cd CppPybindHMACSHA512
cd build
cmake ..
make
```

### Étape 4: Test de l'API

Après avoir construit l'API, vous pouvez tester son fonctionnement en exécutant le script de test test_python.py à partir du dossier parent CppPybindHMACSHA512 :

```

python3 test_python.py
```

Si les tests sont passés avec succès, vous êtes prêt à utiliser l'API HMACSHA512.

### Étape 5: Utilisation de l'API

Pour générer un HMAC à l'aide d'une clé et d'un message, vous pouvez exécuter le script de l'API de la manière suivante :

```

python3 hmac_api.py <key> <message>

```

où <key> est votre clé de 512 bits en format hexadécimal et <message> est le message pour lequel vous souhaitez générer un HMAC. Remplacez nom_du_fichier.py par le nom réel de votre fichier Python. Si la clé ou le message ne sont pas conformes, une erreur sera renvoyée.

## Exemples d'usage : 

**Bon exemple :**

```

python3 hmac_api.py aabbccddeeff00112233445566778899aabbccddeeff00112233445566778899aabbccddeeff00112233445566778899aabbccddeeff00112233445566778899 "Hello, World!"

```

Devra retourner : 

```

Le HMAC généré est : 5da93089e5b539eedc0527e61745016056ce3eae5e35cb4e3dc620ab48aab5c136f1869beabbeb29ac30e172190c426219a0ff65776805d00204930d318e8836

```

**Exemple avec clé < 512 bits :**

```

python3 hmac_api.py aabbccddeeff00112233445566778899aabbccddeeff00112233445566778899aabbccddeeff00112233445566778899aabbccddeeff0011223344556677889 "Hello, World!"

```

Devra retourner : 

```

La clé n'est pas de 512 bits, elle est de 508 bits.

```

**Exemple avec clé non hexadécimal :**

```

python3 hmac_api.py aabbccddeeff00112233445566778899aabbccddeeff00112233445566778899aabbccddeeff00112233445566778899aabbccddeeff001122334455667788k9 "Hello, World!"

```

Devra retourner : 

```

La clé n'est pas en format hexadécimal.

```

