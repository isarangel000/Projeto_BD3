import mysql.connector


def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="banco_proj3"
    )

#cadastrar
def cadastrar_usuario():
    conexao = conectar()
    cursor = conexao.cursor()

    print("\n--- Cadastro de Usuário ---")
    nome = input("Nome: ")


    while True:
        idade_str = input("Idade: ")
        if idade_str.isdigit():
            idade = int(idade_str)
            break
        else:
            print("Por favor, digite um número inteiro válido para a idade.")

    while True:
        tipo = input("Tipo de deficiência: ")
        if tipo.replace(" ", "").isalpha():
            break
        else:
            print("Por favor,digite apenas letras para o tipo de deficiência.")

    sql = "INSERT INTO usuarios (nome, idade, tipo_deficiencia) VALUES (%s, %s, %s)"
    cursor.execute(sql, (nome, idade, tipo))
    conexao.commit()

    print("Usuário cadastrado com sucesso!\n")

    cursor.close()
    conexao.close()


# mostrar os usuários
def listar_usuarios():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()

    print("\n--- Lista de Usuários ---")
    if usuarios:
        for u in usuarios:
            print(f"ID: {u[0]} | Nome: {u[1]} | Idade: {u[2]} | Deficiência: {u[3]}")
    else:
        print("Nenhum usuário cadastrado.\n")

    cursor.close()
    conexao.close()

#tipo de deficiência
def buscar_por_deficiencia():
    conexao = conectar()
    cursor = conexao.cursor()

    tipo = input("Digite o tipo de deficiência para buscar: ")

    cursor.execute("SELECT * FROM usuarios WHERE tipo_deficiencia = %s", (tipo,))
    usuarios = cursor.fetchall()

    print("\n--- Resultado da Busca ---")
    if usuarios:
        for u in usuarios:
            print(f"ID: {u[0]} | Nome: {u[1]} | Idade: {u[2]} | Deficiência: {u[3]}")
    else:
        print("Nenhum usuário encontrado com esse tipo de deficiência.\n")

    cursor.close()
    conexao.close()

#menu
def menu():
    while True:
        print("\n--- Menu ---")
        print("1 - Cadastrar novo usuário")
        print("2 - Listar todos os usuários")
        print("3 - Buscar por tipo de deficiência")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_usuario()
        elif opcao == "2":
            listar_usuarios()
        elif opcao == "3":
            buscar_por_deficiencia()
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida! Tente novamente.")


def principal():
    menu()

principal()
