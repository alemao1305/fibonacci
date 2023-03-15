string = input("Digite uma string: ")
tamanho = len(string)
caracteres = list(string)

for i in range(tamanho // 2):
    temp = caracteres[i]
    caracteres[i] = caracteres[tamanho - i - 1]
    caracteres[tamanho - i - 1] = temp

string_invertida = "".join(caracteres)
print("String invertida: ", string_invertida)
