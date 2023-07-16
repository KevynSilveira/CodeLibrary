import mysql.connector

# Parâmetros de conexão
usuario = "root"
senha = "123qweasdzxc!@#"
database = "codelibrary"

linguagem = ''

# Variáveis globais para armazenar o comando de seleção e o resultado da consulta
comando_select_global = f"select * from commands where language like('%{linguagem}%');"
resultado_global = []



# Função para estabelecer conexão com o banco de dados
def conectar_banco():
    try:
        conexao = mysql.connector.connect(
            host="localhost",
            user=usuario,
            password=senha,
            database=database
        )
        print("Conexão estabelecida com sucesso!")
        return conexao
    except mysql.connector.Error as erro:
        print(f"Erro ao conectar ao banco de dados: {erro}")
        return None


# Função para consultar dados na tabela
def consultar_dados(comando_select_global):
    #global comando_select_global, resultado_global  # Declara as variáveis globais
    global resultado_global
    conexao = conectar_banco()
    if conexao is not None:
        try:
            cursor = conexao.cursor()
            cursor.execute(comando_select_global)  # Utiliza a variável global com o comando de seleção
            resultado = cursor.fetchall()
            if len(resultado) > 0:
                resultado_global = resultado  # Armazena o resultado na variável global
                for linha in resultado:
                    print(linha)
            else:
                print("Nenhum resultado encontrado.")
            cursor.close()
        except mysql.connector.Error as erro:
            print(f"Erro ao executar a consulta: {erro}")
        finally:
            conexao.close()
            print("Conexão fechada.")

# Função para inserir conteúdo na tabela
def inserir_dados(language, command, description):
    conexao = conectar_banco()
    if conexao is not None:
        try:
            cursor = conexao.cursor()
            # Substitua "tabela_exemplo" e os nomes das colunas pelo nome da tabela e colunas reais
            query = "INSERT INTO commands (Language, Command, Description) VALUES (%s, %s, %s)"
            valores = (language, command, description)
            cursor.execute(query, valores)
            conexao.commit()
            print("Dados inseridos com sucesso!")
            cursor.close()
        except mysql.connector.Error as erro:
            print(f"Erro ao inserir dados: {erro}")
        finally:
            conexao.close()
            print("Conexão fechada.")

# Exemplo de uso
#consultar_dados()  # Chama a função para consultar dados na tabela

# Exemplo de uso para inserir dados
#inserir_dados("Python", "print('CONTEUDO A SER IMPRESSO')", "Imprimi a mensagem indicado.")
