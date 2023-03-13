# tamanho do ovo
Pequeno = 7.80
Médio = 12.90
Grande = 23.95
# sabores
choco_preto = 9.67
choco_branco = 4.50
choco_leite = 9.32
# adicionais
kit = 4.67
mm = 5.43
Valor = 0

 
print("Vamos montar seu ovo, de acordo com sua preferência!\n")
# tamanho do ovo=====================================================================
print("Escolha o tamanho do seu ovo: \n")
tamanho = input(f"Pequeno - R${Pequeno}\n Médio - R${Médio}\n Grande - R${Grande}\n").upper()

if tamanho == "Pequeno".upper():
    Valor += Pequeno
elif tamanho == "Médio":
    Valor += Médio
else:
    Valor += Grande

print("========================================\n")
   
# sabor do ovo===================================================================
sn = input("Deseja dois sabores? (s/n)\n").upper()
if sn == "s".upper():
    print("Escolha o primeiro sabor: ")
    saborum = input(f"Chocolate Preto - R${choco_preto}\n Chocolate Branco - R${choco_branco}\n Chocolate ao Leite - R${choco_leite}\n").upper()
    
    if saborum == "Chocolate Preto".upper():
        Valor += (choco_preto / 2)
    elif saborum == "Chocolate Branco".upper():
        Valor += (choco_branco / 2)
    else:
        Valor += (choco_leite / 2)
        
    print("Escolha o segundo sabor: ")
    sabordois = input(f"Chocolate Preto - R${choco_preto}\n Chocolate Branco - R${choco_branco}\n Chocolate ao Leite - R${choco_leite}\n").upper()

    if sabordois == "Chocolate Preto".upper():
        Valor += (choco_preto / 2)
    elif sabordois == "Chocolate Branco".upper():
        Valor += (choco_branco / 2)
    else:
        Valor += (choco_leite / 2)
else:
    print("Escolha o sabor: ")
    sabor = input(f"Chocolate Preto - R${choco_preto}\n Chocolate Branco - R${choco_branco}\n Chocolate ao Leite - R${choco_leite}\n").upper()

    if sabor == "Chocolate Preto".upper():
        Valor += choco_preto
    elif sabor == "Chocolate Branco".upper():
        Valor += choco_branco
    else:
        Valor += choco_leite
    print("========================================\n")
    
    
# adicionais ================================================================

adicional = input("Deseja adicionar algum adicional?(s/n)\n")
if adicional == "s":
    print("Qual adicional deseja colocar?")
    adicionais = input("KitKat - R$ 4.67\n MM's - R$5.43\n ").upper()
    if adicionais == "KitKat".upper():
       Valor += kit
    else:
        Valor += mm
    outro_adicional = input("Deseja adicionar outro?(s/n)\n")
    if  outro_adicional == "s":
        print("Qual adicional deseja colocar?")
        adicionaldois = input("KitKat - R$ 4.67\n MM's - R$5.43\n ").upper()
        if adicionais == "KitKat".upper():
            Valor += kit
        else:
            Valor += mm

    else:
        print("========================================\n")

else:
    print("========================================\n")

# presente

presente = input("O ovo será para presente?(s/n)\n").upper()

if presente == "s".upper():
    Valor += 2.50
    print("Será adicionado R$ 2.50 no valor do seu ovo")
else:
    print("========================================\n")
    

# entrega 

entrega = input("Retirada na loja ou entrega?\n (loja/entrega)\n").upper()

if entrega == "LOJA":
    print("========================================\n")
else:
    Valor += 5.00
    print("Será adicionado R$ 5.00 no valor do seu ovo")


print(f"Seu ovo de páscoa ficou R${Valor}")
print("========================================\n")

# quantidade

n = int(input("Qual a quantidade de ovos? \n"))

Valor = (Valor * n)
print("========================================\n")


# pagamento

print("Temos as seguintes formas de pagamento: \n")
pagamento =  input("Cartão de crédito - R$ 3.30 a mais \n Pix - desconto de 10% \n Dinheiro - desconto de 10% \n  ").upper()
if pagamento == "Cartao de credito".upper():
    Valor += 3.3
    print(f"O valor total do seu ovo é de: {Valor}. Muito obrigada pela preferência!")
else:
    Valor = Valor - (Valor * 0.10)
    print(f"O valor total do seu ovo é de: {Valor}. Muito obrigada pela preferência!")
    
    
    



    

