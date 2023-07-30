import customtkinter
import textwrap
from Funcoes_frame import tema
from FUNCTIONS.Consulta_sql import consultar_dados
from FUNCTIONS.Consulta_sql import inserir_dados
from tkinter import messagebox


def criar_frame_principal():
    janela_principal = customtkinter.CTk()
    janela_principal.geometry("1000x590")
    janela_principal.title("Biblioteca de comandos")
    janela_principal.resizable(False, False)

    #Variavel usada na criacao de frames para exibicao de conteudo
    global y_pos
    y_pos = 10

    #Variavel armazena o conteudo das paginas
    conteudo_pages = []

    #Armazena a quantidade de paginas dentro da variavel com base no conteudo_pages
    total_pages = len(conteudo_pages)

    # Variáveis para funcionalidade de navegação do livro
    pagina_atual = 0

    def atualiza_pesquisa(linguagem):
        #Converte o comando par a linguagem passada a ele
        comando_select = f"select language, command, description from commands where language = '{linguagem}';"
        return comando_select

    def atualizar_conteudo_pages(resultado):
        #Atualiza o conteudo das paginas conforme o parametro recebido
        nonlocal conteudo_pages
        conteudo_pages = resultado
        atualizar_total_pages()
        exibir_pagina_atual()
    def busca_sql():
        global linguagem
        linguagem = 'sql'
        resultado = consultar_dados(atualiza_pesquisa(linguagem))
        atualizar_conteudo_pages(resultado)

    def busca_python():
        global linguagem
        linguagem = 'python'
        resultado = consultar_dados(atualiza_pesquisa(linguagem))
        atualizar_conteudo_pages(resultado)

    def busca_git():
        global linguagem
        linguagem = 'git'
        resultado = consultar_dados(atualiza_pesquisa(linguagem))
        atualizar_conteudo_pages(resultado)

    def busca_java():
        global linguagem
        linguagem = 'java'
        resultado = consultar_dados(atualiza_pesquisa(linguagem))
        atualizar_conteudo_pages(resultado)

    def cadastro_comando():
        # Função chamada ao clicar no botão "Cadastrar".
        def cancela_cadastro():
            # Remove a tela de cadastro.
            tela_cadastro.destroy()

        def valida_cadastro():
            #Valida se todos os dados foram preenchidos
            linguagem = combobox_linguagem.get()
            comando = entry_comando.get()
            descricao = text_descricao.get("1.0", "end-1c")

            if linguagem != "---Selecione uma linguagem---" and comando != "" and descricao != "":
                inserir_dados(linguagem, comando, descricao)
                messagebox.showinfo('Cadastro comando', 'Comando cadastrado com sucesso!')
            else:
                messagebox.showerror('Cadastro comando', 'Preencha todos os campos')

        tela_cadastro = customtkinter.CTkFrame(master=frame_conteudo, width=480, height=330, corner_radius=10)
        tela_cadastro.place(x=145, y=45)

        label_linguagem = customtkinter.CTkLabel(master=tela_cadastro, text="Escolha a linguagem:")
        label_linguagem.place(x=10, y=10)

        opcoes_linguagem = ["SQL", "Python", "Git", "Java"] # Opções de linguagem para o combobox
        combobox_linguagem = customtkinter.CTkComboBox(master=tela_cadastro, values=opcoes_linguagem, width=460, height=30, state="readonly")
        combobox_linguagem.set("---Selecione uma linguagem---")
        combobox_linguagem.place(x=10, y=40)

        label_comando = customtkinter.CTkLabel(master=tela_cadastro, text="Insira o comando:")
        label_comando.place(x=10, y=80)

        entry_comando = customtkinter.CTkEntry(master=tela_cadastro, width=460, height=30, corner_radius=10)
        entry_comando.place(x=10, y=110)

        label_descricao = customtkinter.CTkLabel(master=tela_cadastro, text="Insira a descrição:")
        label_descricao.place(x=10, y=140)

        text_descricao = customtkinter.CTkTextbox(master=tela_cadastro, width=460, height=90, corner_radius=10)
        text_descricao.place(x=10, y=170)

        botao_cancelar = customtkinter.CTkButton(master=tela_cadastro, width=100, height=30, text="Cancelar", command=cancela_cadastro)
        botao_cancelar.place(x=130, y=290)

        botao_cadastrar = customtkinter.CTkButton(master=tela_cadastro, width=100, height=30, text="Cadastrar", command=valida_cadastro)
        botao_cadastrar.place(x=260, y=290)

    def criar_frame_conteudo(linguagem, comando, descricao):
        global y_pos  # Indica que estamos utilizando a variável global y_pos
        # Cria um frame de conteúdo com as informações fornecidas.
        # Função interna para exibir a descrição completa.
        def mostrar_descricao(y): #Mostra a descricao do comando
            def voltar_descricao():
                tela_descricao.destroy()
                botao_voltar.destroy()

            tela_descricao = customtkinter.CTkTextbox(master=frame_conteudo, width=740, height=100)
            tela_descricao.insert(customtkinter.END, descricao)
            tela_descricao.bind("<Key>", lambda e: "break")
            tela_descricao.place(x=10, y=y)

            botao_voltar = customtkinter.CTkButton(master=frame_conteudo, width=10, height=10, text="", corner_radius=2, command=voltar_descricao)
            botao_voltar.place(x=740, y=y)

        #Cria o frame bloco de conteudo
        frame_bloco_conteudo = customtkinter.CTkFrame(master=frame_conteudo, width=740, height=45)
        frame_bloco_conteudo.place(x=15, y=y_pos)

        frame_linguagem = customtkinter.CTkFrame(master=frame_bloco_conteudo, width=100, height=45)
        frame_linguagem.place(x=0, y=0)
        label_linguagem = customtkinter.CTkLabel(master=frame_linguagem, text=linguagem)
        label_linguagem.place(relx=0.5, rely=0.5, anchor="center")

        frame_comando = customtkinter.CTkFrame(master=frame_bloco_conteudo, width=300, height=45)
        frame_comando.place(x=100, y=0)

        label_comando = customtkinter.CTkLabel(master=frame_comando, text=comando)
        label_comando.place(relx=0.5, rely=0.5, anchor="center")

        frame_descricao = customtkinter.CTkFrame(master=frame_bloco_conteudo, width=340, height=45)
        frame_descricao.place(x=400, y=0)

        botao_descricao = customtkinter.CTkButton(master=frame_descricao, width=10, height=10, text="", corner_radius=2, command=lambda y_pos=y_pos: mostrar_descricao(y_pos))
        botao_descricao.place(x=430, y=35)

        max_caracteres = 30 #Defini o maximo de caracter para mostrar superficialmente na descricao
        #Verifica se a descricao exede o numero maximo de caracter, caso aconteca ela coloca ... no final
        if len(descricao) > max_caracteres:
            texto_exibido = textwrap.shorten(descricao, width=max_caracteres - 3, placeholder="...")
        else:
            texto_exibido = descricao

        label_descricao = customtkinter.CTkLabel(master=frame_descricao, text=texto_exibido)
        label_descricao.place(relx=0.5, rely=0.5, anchor="center")

        y_pos += 55 #Atualiza a posicao do frame


    frame_linguagens = customtkinter.CTkFrame(master=janela_principal, width=200, height=570, corner_radius=10)
    frame_linguagens.place(x=10, y=10)

    botao_sql = customtkinter.CTkButton(master=frame_linguagens, width=180, height=30, text="SQL", command=busca_sql)
    botao_sql.place(x=10, y=10)

    botao_python = customtkinter.CTkButton(master=frame_linguagens, width=180, height=30, text="Python", command=busca_python)
    botao_python.place(x=10, y=50)

    botao_git = customtkinter.CTkButton(master=frame_linguagens, width=180, height=30, text="Git", command=busca_git)
    botao_git.place(x=10, y=90)

    botao_java = customtkinter.CTkButton(master=frame_linguagens, width=180, height=30, text="Java", command=busca_java)
    botao_java.place(x=10, y=130)

    def pesquisa():
        # Obter o conteúdo dos campos
        cpesquisa = campo_pesquisa.get()
        filtro = combobox_filtro.get()

        # Verificar se os campos estão preenchidos
        if cpesquisa.strip() == "" or filtro == "---Filtro---":
            messagebox.showwarning('Alerta', 'Por favor, preencha todos os campos antes de realizar a pesquisa.')
            return

        # Realizar a pesquisa
        realizar_pesquisa(cpesquisa, filtro)

    def realizar_pesquisa(cpesquisa, filtro): #Faz a pesquisa com base no texto de pesquisa e no filtro
        #formata o conteudo passado para fazer a pesquisa no banco
        if filtro == 'Linguagem':
            filtro = 'language'
        elif filtro == 'Comando':
            filtro = 'command'
        else:
            filtro = 'description'

        #Formata o comando para mando pro banco
        comando = f'select language, command, description from commands where {filtro} like "%{cpesquisa}%";'

        #Faz a consulta e atualiza as paginas
        resultado = consultar_dados(comando)
        atualizar_conteudo_pages(resultado)

    campo_pesquisa = customtkinter.CTkEntry(master=janela_principal, width=510, height=30, corner_radius=10)
    campo_pesquisa.place(x=220, y=10)

    opcoes_filtro = ["Linguagem", "Comando", "Descrição"] #Opções da combobox
    combobox_filtro = customtkinter.CTkComboBox(master=janela_principal, values=opcoes_filtro, width=200, height=30, state="readonly")
    combobox_filtro.set("---Filtro---")
    combobox_filtro.place(x=740, y=10)

    botao_pesquisa = customtkinter.CTkButton(master=campo_pesquisa, width=70, height=20, text="Pesquisa", command=pesquisa)
    botao_pesquisa.place(x=435, y=5)

    botao_tema = customtkinter.CTkButton(master=janela_principal, width=40, height=30, text="", command=tema)
    botao_tema.place(x=950, y=11)

    frame_conteudo = customtkinter.CTkFrame(master=janela_principal, width=770, height=420, corner_radius=10)
    frame_conteudo.place(x=220, y=100)

    botao_cadastrar = customtkinter.CTkButton(master=frame_linguagens, text="Cadastrar", command=cadastro_comando)
    botao_cadastrar.place(x=30, y=530)

    botao_exportar = customtkinter.CTkButton(master=janela_principal, text="Exportar", width=100)
    botao_exportar.place(x=880, y=540)

    def proxima_pagina():
        nonlocal pagina_atual, conteudo_pages
        if conteudo_pages and pagina_atual < total_pages - 1:
            pagina_atual += 1
            exibir_pagina_atual()

    def pagina_anterior():
        nonlocal pagina_atual, conteudo_pages
        if conteudo_pages and pagina_atual > 0:
            pagina_atual -= 1
            exibir_pagina_atual()

    def atualizar_total_pages():
        nonlocal total_pages
        nonlocal conteudo_pages
        if conteudo_pages:
            total_pages = len(conteudo_pages)
        else:
            total_pages = 0

    def exibir_pagina_atual():
        global y_pos
        y_pos = 10
        # Limpa o conteúdo atual antes de exibir a nova página
        for widget in frame_conteudo.winfo_children():
            widget.destroy()
        for tupla in conteudo_pages:
            for conteudo in tupla:
                linguagem, comando, descricao = conteudo
                criar_frame_conteudo(linguagem, comando, descricao)

    # Cria botões para avançar e voltar de página
    botao_proxima = customtkinter.CTkButton(master=janela_principal, width=140, height=30, text="Proxima", command=proxima_pagina)
    botao_proxima.place(x=585, y=540)

    botao_anterior = customtkinter.CTkButton(master=janela_principal, width=140, height=30, text="Voltar", command=pagina_anterior)
    botao_anterior.place(x=435, y=540)


    # Executa a janela principal
    janela_principal.mainloop()

if __name__ == "__main__":
    criar_frame_principal()