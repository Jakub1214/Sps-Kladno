vek = int(input("Zadejte svůj věk: "))
student = input("Zadejte zda jste studentem skoly")
doprovod = input("mas doprovod")
zakaz = input("Mas zakaz?")



if vek >= 15 and (student == "ano" or doprovod == "ne") and zakaz == "ne":
    print("Vstup povolen")

else:
    print("Vstup zakazan")