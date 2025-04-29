#Faça um programa em python que leia dois valores para as variáveis A e B. O programa deve somar os dois valores e apresentar o resultado. Repetindo a sequência de entrada de A e B e soma perguntando se deseja continuar.
#OBS.: Utilize uma pergunta para o usuário digitar um valor por exemplo :
#Digite 0 para sair ou 1 para continuar.
i = 0
while i < 1:
    A = int(input("Digite o primeiro número aqui :"))
    B = (int(input("Digite o segundo número aqui :")))
    Soma = A + B
    print("", Soma)
    option = int(input("1-Se dejesa continuar 0- Se deseja sair. "))
    if option == 0:
        print("Encerrando o programa. Até logo!")
        break
    elif option == 1:
        print("Vamos continuar!")
    