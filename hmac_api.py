import argparse
import binascii
from build import hmac_cpp

def validate_key(key):
    key_length = len(key) * 4
    if key_length != 512:
        raise ValueError(f"La clé n'est pas de 512 bits, elle est de {key_length} bits.")
    try:
        int(key, 16)
    except ValueError:
        raise ValueError("La clé n'est pas en format hexadécimal.")
        
def validate_and_generate_hmac(key, message):
    # Validate key
    validate_key(key)

    # Convert message to hexadecimal
    message_hex = binascii.hexlify(message.encode()).decode()

    # Generate HMAC
    return hmac_cpp.get_hmac(key, message_hex, hmac_cpp.TypeHash.SHA512)

def main():
    parser = argparse.ArgumentParser(description="Générer un HMAC à l'aide d'une clé et d'un message.")
    parser.add_argument("key", help="La clé de 512 bits en format hexadécimal.")
    parser.add_argument("message", help="Le message pour générer le HMAC.")
    args = parser.parse_args()

    try:
        hmac = validate_and_generate_hmac(args.key, args.message)
        print(f"Le HMAC généré est : {hmac}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
