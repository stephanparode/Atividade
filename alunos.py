alunos = ["Victor", "Felipe", "Aisla"]
matriculas = ["12346", "76153", "12234"]
# listas paralelas, cada aluno só pode ter uma matricula (ex: joão é o elemento 0 da lista alunos, portanto tem a matricula 0)

notas = {
    "Victor": [7.0, 8.5, 9.0],
    "Felipe": [6.0, 7.0, 10.0], 
    "Aisla": [4.0, 10.0, 10.0]
} # dicionário com notas correspondentes a cada elemento do array alunos (cada aluno pode ter mais de uma nota)

medias = {
    "Victor": None, 
    "Felipe": None,
    "Aisla": None
}

def adicionar_aluno (nome, matricula):
    if nome not in alunos: 
        alunos.append(nome)
        matriculas.append(matricula) # CORREÇÃO: Era 'matriculas.append(matriculas)', corrigido para 'matricula'.
        notas[nome] = [] # Inicializa uma lista de notas vazia para o novo aluno.
        medias[nome] = None 
        print(f"Aluno {nome} com matrícula {matricula} adicionado.")
    else:
        print(f"Aluno {nome} já existe no sistema.")

def adicionar_nota (nome, nota): 
    if nome in notas:
        notas[nome].append(nota) # CORREÇÃO: Usar colchetes [] para acessar itens em dicionários.
        print(f"Nota {nota} adicionada para o aluno {nome}.")
    else:
        print(f"Aluno {nome} não encontrado.")

def calcular_media (nome):
    if nome in notas:
        if len(notas[nome]) > 0: # Garante que o aluno tem notas para calcular a média.
            media = sum(notas[nome])/len(notas[nome])
            medias[nome] = media # Armazena a média calculada no dicionário 'medias'.
            return media 
        else:
            print(f"O aluno {nome} não possui notas para calcular a média.")
            return None # Retorna None se não houver notas.
    else:
        print(f"Aluno {nome} não encontrado.")
        return None # Retorna None se o aluno não for encontrado.


def mostrar_alunos():
    if alunos:
        print("\n--- Alunos Cadastrados ---")
        for i, aluno_nome in enumerate(alunos):
            print(f"Nome: {aluno_nome}, Matrícula: {matriculas[i]}")
        print("--------------------------")
    else:
        print("Nenhum aluno cadastrado.")

def mostrar_informacao (aluno_nome): 
    if aluno_nome in alunos:
        idx = alunos.index(aluno_nome)
        print(f"\n--- Informações de {aluno_nome} ---")
        print(f"Matrícula: {matriculas[idx]}")
        print(f"Notas: {notas.get(aluno_nome, 'N/A')}")
        media_atual = calcular_media(aluno_nome) # Calcula a média para exibir a informação atualizada.
        if media_atual is not None:
            print(f"Média: {media_atual:.2f}")
        else:
            print("Média: Não calculada ou sem notas.")
        print("------------------------------")
    else:
        print(f"Aluno {aluno_nome} não encontrado.")

def verificar_situacao (nome):
    if nome in medias:
        # Garante que a média esteja calculada antes de verificar a situação.
        if medias[nome] is None and nome in notas and len(notas[nome]) > 0:
            calcular_media(nome) # Calcula a média se ainda não foi.

        if isinstance(medias[nome], (float, int)): # Verifica se 'medias[nome]' é um número válido.
            if medias[nome] >= 6.0:
                situacao = "aprovado"
            else:
                situacao = "reprovado"
            return situacao
        else:
            print(f"Não há média calculada para o aluno {nome}.")
            return None
    else:
        print(f"Aluno {nome} não encontrado.")
        return None
