import aluno # Importe o módulo 'aluno' para usar suas funções

escolha = "s"
while escolha == "s": # Usar '==' para comparação, essencial para o loop funcionar corretamente
    print("\nBem vindo ao sistema de alunos! O que deseja fazer?")
    opcao = int(input(" 1- Adicionar aluno \n 2- Ver informações de aluno\n 3- Adicionar nota \n 4- Calcular média \n 5- Verificar aprovação \n Escolha uma opção: "))

    if opcao == 1:
        nome = input("Insira o nome do aluno: ")
        matricula = input("Insira a matrícula do aluno: ")
        aluno.adicionar_aluno(nome, matricula)
    elif opcao == 2:
        nome_aluno_info = input("De qual aluno você deseja ver as informações? ")
        aluno.mostrar_informacao(nome_aluno_info) 
    elif opcao == 3:
        nome = input("A qual aluno você deseja adicionar a nota? ")
        try:
            
            nota = float(input(f"Qual foi a nota de {nome}? "))
            aluno.adicionar_nota(nome, nota)
        except ValueError:
            print("Entrada inválida. Por favor, insira um número para a nota.")
    elif opcao == 4:
        nome = input("Qual aluno deve ter a média calculada? ")
        media_calculada = aluno.calcular_media(nome) # A função agora retorna a média
        if media_calculada is not None: # Verifica se a média foi realmente calculada
            print(f"A média de {nome} é: {media_calculada:.2f}")
        else:
            print(f"Não foi possível calcular a média para {nome}.")
    elif opcao == 5: # Corrigido o elif duplicado, agora é para opção 5
        nome = input("Você quer verificar a aprovação de qual aluno? ")
        situacao = aluno.verificar_situacao(nome)
        if situacao: # Verifica se a situação foi retornada
            print(f"O aluno {nome} está {situacao}.")
        else:
            print(f"Não foi possível verificar a situação de {nome}.")
    else:
        print("Opção inválida! Por favor, escolha uma opção entre 1 e 5.")


    escolha = input("Deseja continuar? (s/n): ").lower()
    if escolha not in ["s", "n"]:
        print("Entrada inválida. Encerrando o sistema.")
        escolha = "n" # Garante que o loop termine se a entrada for inválida
