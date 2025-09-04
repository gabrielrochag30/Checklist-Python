import os
import json
from datetime import date

ARQUIVO = "checklist.json"

# Carregar tarefas do arquivo
def carregar_tarefas():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            dados = json.load(f)
            # Se mudou o dia, desmarca todas as tarefas
            if dados["data"] != str(date.today()):
                for t in dados["tarefas"]:
                    t["feito"] = False
                dados["data"] = str(date.today())
            return dados
    return {"tarefas": [], "data": str(date.today())}

# Salvar tarefas no arquivo
def salvar_tarefas(dados):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)

# Programa principal
dados = carregar_tarefas()
tarefas = dados["tarefas"]

while True:
    print("\n--- MENU ---")
    print("1 - Adicionar tarefa")
    print("2 - Ver tarefas")
    print("3 - Marcar tarefa como concluída")
    print("4 - Desmarcar tarefa")
    print("5 - Remover tarefa")
    print("6 - Reordenar tarefa")
    print("7 - Editar tarefa")
    print("8 - Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        tarefa = input("Digite a nova tarefa: ")
        tarefas.append({"nome": tarefa, "feito": False})
        print("Tarefa adicionada!")

    elif escolha == "2":
        if not tarefas:
            print("Nenhuma tarefa na lista.")
        else:
            print("\nChecklist:")
            largura = len(str(len(tarefas)))  # calcula largura máxima do número
            for i, tarefa in enumerate(tarefas, start=1):
                status = "[X]" if tarefa["feito"] else "[ ]"
                # usa f-string com alinhamento
                print(f"{i:>{largura}}. {status} {tarefa['nome']}")

    elif escolha == "3":
        if not tarefas:
            print("Nenhuma tarefa para marcar.")
        else:
            num = int(input("Digite o número da tarefa concluída: "))
            if 1 <= num <= len(tarefas):
                tarefas[num - 1]["feito"] = True
                print("Tarefa marcada como concluída!")
            else:
                print("Número inválido.")

    elif escolha == "4":
        if not tarefas:
            print("Nenhuma tarefa para desmarcar.")
        else:
            num = int(input("Digite o número da tarefa a desmarcar: "))
            if 1 <= num <= len(tarefas):
                tarefas[num - 1]["feito"] = False
                print("Tarefa desmarcada!")
            else:
                print("Número inválido.")

    elif escolha == "5":
        if not tarefas:
            print("Nenhuma tarefa para remover.")
        else:
            num = int(input("Digite o número da tarefa a remover: "))
            if 1 <= num <= len(tarefas):
                removida = tarefas.pop(num - 1)
                print(f"Tarefa '{removida['nome']}' removida!")
            else:
                print("Número inválido.")

    elif escolha == "6":
        if len(tarefas) < 2:
            print("Precisa de pelo menos duas tarefas para reordenar.")
        else:
            num = int(input("Número da tarefa que deseja mover: "))
            nova_pos = int(input("Nova posição desejada: "))
            if 1 <= num <= len(tarefas) and 1 <= nova_pos <= len(tarefas):
                tarefa = tarefas.pop(num - 1)         # remove da posição atual
                tarefas.insert(nova_pos - 1, tarefa)  # insere na nova posição
                print("Tarefa movida com sucesso!")
            else:
                print("Número inválido.")

    elif escolha == "7":
        if not tarefas:
            print("Nenhuma tarefa para editar.")
        else:
            num = int(input("Digite o número da tarefa que deseja editar: "))
            if 1 <= num <= len(tarefas):
                novo_nome = input("Digite o novo nome da tarefa: ")
                tarefas[num - 1]["nome"] = novo_nome
                print("Tarefa editada com sucesso!")
            else:
                print("Número inválido.")

    elif escolha == "8":
        salvar_tarefas({"tarefas": tarefas, "data": str(date.today())})
        print("Saindo do checklist. Até mais!")
        break

    else:
        print("Opção inválida. Tente novamente.")
