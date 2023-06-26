import hmac_cpp

input_string = "grape"
key = "12345"

output1 = hmac_cpp.get_hmac(key, input_string, hmac_cpp.TypeHash.SHA256)
print(f"get_hmac('{key}','{input_string}',SHA256): {output1}")
print("The answer should be: 7632ac2e8ddedaf4b3e7ab195fefd17571c37c970e02e169195a158ef59e53ca\n")

output2 = hmac_cpp.get_hmac(key, input_string, hmac_cpp.TypeHash.SHA512)
print(f"get_hmac('{key}','{input_string}',SHA512): {output2}")
print("The answer should be: c54ddf9647a949d0df925a1c1f8ba1c9d721a671c396fde1062a71f9f7ffae5dc10f6be15be63bb0363d051365e23f890368c54828497b9aef2eb2fc65b633e6\n")
