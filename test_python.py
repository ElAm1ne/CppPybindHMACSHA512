import hmac_cpp
import secrets
import binascii

list_input = ["delta", "gamma", "vega", "theta", "rho", "Black and Scholes", "BlockChain", "BitCoin", "Composant"]
list_true_hmac = [
    "4a457f08d5fe948661339e559c04d98003524a8b013b51ea1fa616848b190e95436f4f54a0e91020d61712f4a703e536a17168123d0a58ca8c65b43d6ec9ebdf",
    "fcf47de919f50c1f432a57afb2703ab53c784cae9601cf23007fcf2d0d448215a7af1a1c7ff1c8fe6b0bc55bc236eebba3069ce84112e7a00d4a091b04144d18",
    "c34d861d8380748ad73b195e0b8f8ac2f31682a2a9e0143599f385b45a079c6164915c5eb2cebd99cfbec669cd24aaf824f144f2d94cc2a985565de05014d78f",
    "ca619961db6de536f0ece04ba21b755af1d0500604c5c581b17a450a1cef08058039924ce45c1b21cc7b6c6cee344a8082c866d4fb6aec0c5cd78430b8a4e05f",
    "f228be34270f478d1c5b9c8899e5141c70ae8c0c15629a0b40c6be7915eca57a8162d65ac2bd9d104ae1be17e27d19ac5995f90e7cf16edaf93cc31e91d60ae3",
    "9dbf4a8fabfb06fc08bc0660e44f343169db13a88cc7afc70c90828a5e1757765aac74128d82105fd4a6c4faaf53f772da7d09480ff158478889ef9269db2744",
    "c07a6537ccaec893a8597b0ddc0abbe2cba60b280242d701f5a53143910b90111b9d3f24aa6bac149c48cb3860c745b0f998d3f4229015463622bdc0f939dfbd",
    "437010955bc72b4bffb41ac4aa862cbe40c693064bac8d360de58628524e7e3127bc909a255b4870978eb5494e1a6d4771d556dd91a9309977aac4a87f594d57",
    "36e6108a7f01210b86ea9864a012468b14e135c97110fdd40d3deeee086755b836bf46e45ec07dd1fa4e703c8f3a29a4fdc0f40eb2a676d4db35dfa1aff92a5a"
]
hex_keys = ["6512480b414f8f5c016b41c94994e1c73096f8cbed6fa211d35f725ce0b87272b99acbf4ff28ef16dfa6f0109aa7b8a379e7be16400ccced225a7edcbad9acfa",
"f419c4f0835a00a1ea47c61ccab69bd8f66e7663b15a0da7b3ba8821c82008b30965c9a02eb405495b1e0c47566dfeb52e8c20072d419551bdeaf0d46a5f6411",
"bf73fe233e94ea39707a042d08d23b8cb1c944b8e51fbd42c6011af02e8a1a097ac80fa329468962b9cf77ed11eb78d1809060109d46bbde1b83cebda0dede5d",
"cf985070b15ea0fe1c65604e32e66fee30e1254335e05f9d69bdc5648070f243843429946ac5e65d30ea196a549be9e724d304e8a90363f40af259201605b422",
"f3f52d43cc0f462ff7293b6f1268625c72c6ef859ca24cf0d3f760b38e4f66251a3d65729015c0c2420a235c42727bb2a182543cd2ea38a48ead9cd1b50948eb",
"9d52e4ba0f0df3145e2c8e925d28124ff68c062b227f26e2f71f0e47699baafff794e0830cdcf59b4abf057d8bd6c82328bf118f1a77850d0036f82ad3e06b34",
"0bdc13271c7ce356e662f125b47926a0cf98407f33dd71f433b95d8c41c8e08f37f75a2562590f50e22e3969cb33fc9cb47f3fa05c337bcb1cb70ca743206572",
"8781070cb204ec09305e47e02560e0914ec8d90a236bad3ac8d37264671cd236808850bd9ea6556337ca0633b6db5b8f5899c89179aa594894f73e8d33588b14",
"0f5c65c3dc4b771014e9633555f0080741c734c1751d654cf11a684c6962fd00679786b14d6fa5c65a807c37a3d340a4d0d6676d1959928b1b9c735415f57b2b"]


'''
Hex keys generated using this code :
#Generate a 512-bit key
    key = secrets.token_bytes(64)  # 64 bytes = 512 bits

    # Convert the key to hexadecimal
    key_hex = key.hex()
'''
total_tests = len(list_true_hmac)
failed_tests = 0

for i in range(0,9):
    # Create a binary message
    binary_message = list_input[i].encode()

    # Convert the binary message to hexadecimal
    binary_message_hex = binascii.hexlify(binary_message).decode()

    output1  = hmac_cpp.get_hmac(hex_keys[i], binary_message_hex, hmac_cpp.TypeHash.SHA512)
    print("get_hmac('"+ str(hex_keys[i]) +"','" + str(binary_message_hex) + "',SHA512): " + str(output1))
    print("The answer should be: ", str(list_true_hmac[i]) )

    if str(output1) != str(list_true_hmac[i]) :
        failed_tests += 1
        print("-----------------------------")
        print(f"Test n°{i+1} Failed.")
        print("-----------------------------")
        print(False)
    else:
        print("--------------------------------------------")
        print(f"Test n°{i+1} passed successfully.")
        print("--------------------------------------------")
    
print(f"Number of failed tests is {failed_tests}.")
print(f"Number of passed tests is {total_tests - failed_tests}.")
print(f"Success rate is {int((total_tests - failed_tests)/total_tests)*100}%.")
