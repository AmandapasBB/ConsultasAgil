# Estruturas de dados
from datetime import datetime
pacientes = []
consultas_agendadas = []

#cadastrar um paciente:
def cadastrar_paciente():
    nome = input( "Digite o nome do paciente: ")
    telefone = input( "Digite o telefone do paciente(xxxx-xxxx): ")
    for paciente in pacientes:
        if paciente['telefone'] == telefone:
            print("Paciente já cadastrado!")
            return
    pacientes.append({
    'nome': nome,
    'telefone': telefone,
    'consultas': []
    })
    print("Paciente cadastrado com sucesso!")
    

def marcar_consulta():
    print("Lista de Pacientes Cadastrados:")
    for i, paciente in enumerate(pacientes, start=1):
        print(f"{i}. {paciente['nome']} - {paciente['telefone']}")

    escolha = int(input("Escolha o número do paciente para agendar a consulta: ")) - 1
    paciente_escolhido = pacientes[escolha]

    data = input("Digite a data da consulta (DD/MM/AAAA): ")
    hora = input("Digite a hora da consulta (HH:MM): ")

    # Verificar se a data e hora são anteriores a data atual 
    try:
        data_hora_consulta = datetime.strptime(f"{data} {hora}", "%d/%m/%Y %H:%M")
        if data_hora_consulta < datetime.now():
            print("Não é possível agendar consultas retroativas.")
            return
    except ValueError:
        print("Formato de data ou hora inválido.")
        return

    especialidade = input("Digite a especialidade da consulta: ")

    # Verificar se o horário está disponível para o paciente
    for consulta in paciente_escolhido['consultas']:
        if consulta['data'] == data and consulta['hora'] == hora:
            print("Você já tem uma consulta agendada nesse horário.")
            return

    # Verificar se o horário está disponível em geral
    for consulta in consultas_agendadas:
        if consulta['data'] == data and consulta['hora'] == hora:
            print("Horário indisponível para agendamento.")
            return

    # Marcar a consulta
    consulta_detalhes = {
        'paciente': paciente_escolhido,
        'data': data,
        'hora': hora,
        'especialidade': especialidade
    }

    consultas_agendadas.append(consulta_detalhes)
    paciente_escolhido['consultas'].append({
        'data': data,
        'hora': hora,
        'especialidade': especialidade
    })

    print("Consulta agendada com sucesso!")


#cancelamento de consulta:
def cancelar_consulta():
    print("Lista de Consultas Agendadas:")
    for i, consulta in enumerate(consultas_agendadas, start=1):
        print(f"{i}. {consulta['paciente']['nome']} - {consulta['data']} às {consulta['hora']} - {consulta['especialidade']}")
    escolha = int(input("Escolha o número da consulta para cancelar: ")) - 1
    consulta_cancelar = consultas_agendadas[escolha]
    print(f"Consulta marcada para {consulta_cancelar['data']} às {consulta_cancelar['hora']} - {consulta_cancelar['especialidade']}.")
    confirmacao = input("Tem certeza que deseja cancelar esta consulta? (s/n): ").strip().casefold()
    if confirmacao == 's':
        consultas_agendadas.pop(escolha)
        consulta_cancelar['paciente']['consultas'].remove({
        'data': consulta_cancelar['data'],
        'hora': consulta_cancelar['hora'],
        'especialidade': consulta_cancelar['especialidade']
        })
        print("Consulta cancelada com sucesso!")
    else:
        print("Operação de cancelamento cancelada.")

#menu inicial e loop de execução:
def exibir_menu():
    print("\n### Clínica de Consultas Ágil ###")
    print("1. Cadastrar paciente")
    print("2. Marcar consulta")
    print("3. Cancelar consulta")
    print("4. Sair do programa")

while True:
    exibir_menu()
    opcao = input("Escolha uma opção: ")
    if opcao == '1':
        cadastrar_paciente()
    elif opcao == '2':
        marcar_consulta()
    elif opcao == '3':
        cancelar_consulta()
    elif opcao == '4':
        print("Encerrando o programa...")
        break
    else:
        print("Opção inválida. Escolha novamente.")

        open = "a"

        f = open("dados.txt", "a")
f.write("Now the file has more content!")
f.close()

#open and read the file after the appending:
f = open("dados.txt", "r")
print(f.read())