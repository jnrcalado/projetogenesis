# Categoria e Preço
categoria = int(input("Digite a categoria do produto:"))
if categoria == 1:
    preco = 10
else:
    if categoria == 2:
        preco = 18
    else:
        if categoria == 3:
            preco = 23
        else:
            if categoria == 4:
                preco = 26
            else:
                if categoria == 5:
                    preco = 31
                else:
                    print("Categoria Inválida\nDigite um valor entre 1 a 5!")
print(f"O Preço do produto é: R${preco:.2f}".replace('.', ','))


