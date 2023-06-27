import hmac_cpp

list_input = ["delta", "gamma", "vega", "theta", "rho", "Black and Scholes", "BlockChain", "BitCoin", "Composant"]
list_key = ["1234", "4567", "8944", "7568", "3984", "2345867", "55567", "47567azer", "ErTuisadh45"]
list_true_hmac = [
    "0b9739aefa3a8ccf5a99cf0922908dc6589f0961aba9e92e9435d752e34e17754a56e6f55c7486c688ab0f8847b672730bda2663454bd732d10db2f6747c4611",
    "dffb1c4e6834c7d087c2d78a6cf2f2319cbaa042d8f8ffb716d236dc3d37a97f8f5dcb3a5ceb5fa4bfc11311dfcb2c080b8d4a2bd40e1319ce6557165c4c6322",
    "498c0b52408e4b7f65c1d982653b70031d3fcb4919a636f631c629c267258c98195f6936a2932a4c66f39c7e759343599343079ee74a212c58b143e87b1463e7",
    "c8e8e1896faeb4b8176ea314b57f3b79dd1493d0c209f4d51cbeb67aafeb314eb8b4ee18cc02124fcde6e81792f6b06386f60e832f38f850ea8e3ce92480ffb8",
    "cca86f461762d0c6633fbc8478c7ab3e3929d2e61f8a7552ae5407416d5b0594045326bea0e4d7f49b5cb96274deec29f24daa49167b35c12b2067b711ee3ec8",
    "e4628ec58d0eef46a935ede2408d0c9cbb8c2b7cb3686ba672d8cc18cc65e46bfc3ceeaffa0bb632455f2d95f2cc34d8789713bf06706b2cdaeeaae361d95e1f",
    "0eb6ab0cc74ef1749045979c4e0efc39aa848e1db9b7de22c3129d184b833071699a8990351ebeac13a1d50d2b7f13bb9ada6082e08999f7ce50ff0adf52e97e",
    "9ead353f3ff9565d8f96f48dc0ba98522ee074f84fd3c856eaa30348f35d712dd63c1ad19cd87813ae4f6d2d13c1bd5fca5703ade32774b5ee214f53941221f4",
    "4d57da3ac756ff90184c9ff8c64e376f28b60dd8cfa1bc15e803eb62b25797cc0c3bd79bb6952bba75ce5c46e421cfe550087e8b0c4acc1c3541c2c85f291615"
]

total_tests = len(list_true_hmac)
failed_tests = 0
for i in range(0,9):
    output1  = hmac_cpp.get_hmac(list_key[i], list_input[i], hmac_cpp.TypeHash.SHA512)
    print("get_hmac("+ str(list_key[i]) +"','" + str(list_input[i]) + "',SHA512): " + str(output1))
    print("The answer should be: ", str(list_true_hmac[i]) )

    if str(output1) != str(list_true_hmac[i]) :
        failed_tests += 1
        print("The test Failed")
        print(False)
    
print(f"Number of failed tests is {failed_tests}.")
print(f"Number of passed tests is {total_tests - failed_tests}.")
print(f"Success rate is {int((total_tests - failed_tests)/total_tests)*100}%.")