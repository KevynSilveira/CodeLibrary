import customtkinter
import textwrap
from Funcoes_frame import tema

def criar_frame_principal():
    # Cria a janela principal do aplicativo.
    janela_principal = customtkinter.CTk()
    janela_principal.geometry("1000x590")
    janela_principal.title("Biblioteca de comandos")
    janela_principal.resizable(False, False)

    # Inicializa a posição vertical
    global y_pos  # Indica que estamos utilizando a variável global y_pos
    y_pos = 10

    def cadastrar_comando():
        # Função chamada ao clicar no botão "Cadastrar".
        def cancelar_cadastro():
            # Remove a tela de cadastro.
            tela_cadastro.destroy()

        def cadastrar():
            linguagem = combobox_linguagem.get()
            comando = entry_comando.get()
            descricao = text_descricao.get("1.0", "end-1c")

            if linguagem != "---Selecione uma linguagem---" and comando != "" and descricao != "":
                tela_cadastro.destroy()
            else:
                tela_cadastro.destroy()

        # Frame conteúdo, onde ficarão todas as opções de cadastrar um comando
        tela_cadastro = customtkinter.CTkFrame(master=frame_conteudo, width=480, height=330, corner_radius=10)
        tela_cadastro.place(x=145, y=45)

        # Label de escolha de linguagem utilizando combobox
        label_linguagem = customtkinter.CTkLabel(master=tela_cadastro, text="Escolha a linguagem:")
        label_linguagem.place(x=10, y=10)

        # Opções de linguagem para o combobox
        opcoes_linguagem = ["SQL", "Python", "Git", "Java"]

        # Campo combobox para selecionar a linguagem pegando como parâmetro as opções de linguagem acima
        combobox_linguagem = customtkinter.CTkComboBox(master=tela_cadastro, values=opcoes_linguagem, width=460, height=30,
                                        state="readonly")
        combobox_linguagem.set("---Selecione uma linguagem---")
        combobox_linguagem.place(x=10, y=40)

        # Label indicativa para cadastrar um comando
        label_comando = customtkinter.CTkLabel(master=tela_cadastro, text="Insira o comando:")
        label_comando.place(x=10, y=80)

        # Campo de cadastro de comando
        entry_comando = customtkinter.CTkEntry(master=tela_cadastro, width=460, height=30, corner_radius=10)
        entry_comando.place(x=10, y=110)

        # Label indicativa para descrever o que o comando faz
        label_descricao = customtkinter.CTkLabel(master=tela_cadastro, text="Insira a descrição:")
        label_descricao.place(x=10, y=140)

        # Campo de cadastro de descrição
        text_descricao = customtkinter.CTkTextbox(master=tela_cadastro, width=460, height=90, corner_radius=10)
        text_descricao.place(x=10, y=170)

        # Botão de cancelar operação
        botao_cancelar = customtkinter.CTkButton(master=tela_cadastro, width=100, height=30, text="Cancelar",
                                        command=cancelar_cadastro)
        botao_cancelar.place(x=130, y=290)

        # Botão de cadastrar comando
        botao_cadastrar = customtkinter.CTkButton(master=tela_cadastro, width=100, height=30, text="Cadastrar",
                                          command=cadastrar)
        botao_cadastrar.place(x=260, y=290)

    def criar_frame_conteudo(linguagem, comando, descricao):
        global y_pos  # Indica que estamos utilizando a variável global y_pos

        # Cria um frame de conteúdo com as informações fornecidas.

        # Função interna para exibir a descrição completa.
        def mostrar_descricao(y):
            def voltar_descricao():
                tela_descricao.destroy()
                botao_voltar.destroy()

            tela_descricao = customtkinter.CTkTextbox(master=frame_conteudo, width=740, height=100)
            tela_descricao.insert(customtkinter.END, descricao)
            tela_descricao.bind("<Key>", lambda e: "break")
            tela_descricao.place(x=10, y=y)

            botao_voltar = customtkinter.CTkButton(master=frame_conteudo, width=10, height=10, text="", corner_radius=2,
                                          command=voltar_descricao)
            botao_voltar.place(x=740, y=y)

        frame_bloco_conteudo = customtkinter.CTkFrame(master=frame_conteudo, width=740, height=45)
        frame_bloco_conteudo.place(x=10, y=y_pos)

        frame_linguagem = customtkinter.CTkFrame(master=frame_bloco_conteudo, width=100, height=45)
        frame_linguagem.place(x=0, y=0)
        label_linguagem = customtkinter.CTkLabel(master=frame_linguagem, text=linguagem)
        label_linguagem.place(relx=0.5, rely=0.5, anchor="center")

        frame_comando = customtkinter.CTkFrame(master=frame_bloco_conteudo, width=200, height=45)
        frame_comando.place(x=100, y=0)
        label_comando = customtkinter.CTkLabel(master=frame_comando, text=comando)
        label_comando.place(relx=0.5, rely=0.5, anchor="center")

        frame_descricao = customtkinter.CTkFrame(master=frame_bloco_conteudo, width=440, height=45)
        frame_descricao.place(x=300, y=0)
        botao_descricao = customtkinter.CTkButton(master=frame_descricao, width=10, height=10, text="", corner_radius=2,
                                         command=lambda y_pos=y_pos: mostrar_descricao(y_pos))
        botao_descricao.place(x=430, y=35)

        max_caracteres = 30
        if len(descricao) > max_caracteres:
            texto_exibido = textwrap.shorten(descricao, width=max_caracteres - 3, placeholder="...")
        else:
            texto_exibido = descricao

        label_descricao = customtkinter.CTkLabel(master=frame_descricao, text=texto_exibido)
        label_descricao.place(relx=0.5, rely=0.5, anchor="center")

        y_pos += 55

    # Frame principal
    frame_linguagens = customtkinter.CTkFrame(master=janela_principal, width=200, height=570, corner_radius=10)
    frame_linguagens.place(x=10, y=10)

    # Botão para SQL
    botao_sql = customtkinter.CTkButton(master=frame_linguagens, width=180, height=30, text="SQL")
    botao_sql.place(x=10, y=10)

    # Botão para Python
    botao_python = customtkinter.CTkButton(master=frame_linguagens, width=180, height=30, text="Python")
    botao_python.place(x=10, y=50)

    # Botão para Git
    botao_git = customtkinter.CTkButton(master=frame_linguagens, width=180, height=30, text="Git")
    botao_git.place(x=10, y=90)

    # Botão para Java
    botao_java = customtkinter.CTkButton(master=frame_linguagens, width=180, height=30, text="Java")
    botao_java.place(x=10, y=130)

    # Campo de pesquisa
    campo_pesquisa = customtkinter.CTkEntry(master=janela_principal, width=510, height=30, corner_radius=10)
    campo_pesquisa.place(x=220, y=10)

    # Opções da combobox
    opcoes_filtro = ["Linguagem", "Comando", "Descrição"]

    # Botão combobox filtro
    combobox_filtro = customtkinter.CTkComboBox(master=janela_principal, values=opcoes_filtro, width=200, height=30,
                                    state="readonly")
    combobox_filtro.set("---Filtro---")
    combobox_filtro.place(x=740, y=10)

    # Botão para definir o tema
    botao_tema = customtkinter.CTkButton(master=janela_principal, width=40, height=30, text="", command=tema)
    botao_tema.place(x=950, y=11)

    # Frame conteúdo
    frame_conteudo = customtkinter.CTkFrame(master=janela_principal, width=770, height=420, corner_radius=10)
    frame_conteudo.place(x=220, y=100)

    # Scrollbar do frame conteúdo
    scrollbar = customtkinter.CTkScrollbar(master=frame_conteudo)
    scrollbar.place(x=750, y=10)

    # Botão exportar
    botao_exportar = customtkinter.CTkButton(master=janela_principal, text="Exportar", width=100)
    botao_exportar.place(x=880, y=540)

    # Botão Cadastrar comando
    botao_cadastrar = customtkinter.CTkButton(master=frame_linguagens, text="Cadastrar", command=cadastrar_comando)
    botao_cadastrar.place(x=30, y=530)

    sql = "SQL"
    comando_sql = "Select * From"
    descricao_sql = "Seleciona arquivos"

    python = "Python"
    comando_python = "import"
    descricao_python = "Importa bibliotecas"

    git = "Git"
    comando_git = "git add . "
    descricao_git = "Adiciona arquivos no stage"

    conteudo_pages = [
        [(sql, comando_sql, descricao_sql), (python, comando_python, descricao_python), (git, comando_git, descricao_git)],
        [(sql, comando_sql, descricao_sql), (python, comando_python, descricao_python),
         (git, comando_git, descricao_git)],
        [(sql, comando_sql, descricao_sql), (python, comando_python, descricao_python),
         (git, comando_git, descricao_git)]
    ]

    total_pages = len(conteudo_pages)

    # Variáveis para funcionalidade de navegação do livro
    pagina_atual = 0

    def proxima_pagina():
        nonlocal pagina_atual
        if pagina_atual < total_pages - 1:
            pagina_atual += 1
            exibir_pagina_atual()

    def pagina_anterior():
        nonlocal pagina_atual
        if pagina_atual > 0:
            pagina_atual -= 1
            exibir_pagina_atual()

    def exibir_pagina_atual():
        global y_pos
        y_pos = 10

        for widget in frame_conteudo.winfo_children():
            widget.destroy()

        conteudo_pagina = conteudo_pages[pagina_atual]
        for conteudo in conteudo_pagina:
            criar_frame_conteudo(*conteudo)

    # Cria botões para avançar e voltar de página
    botao_proxima = customtkinter.CTkButton(master=janela_principal, width=140, height=30, text="Proxima", command=proxima_pagina)
    botao_proxima.place(x=585, y=540)

    botao_anterior = customtkinter.CTkButton(master=janela_principal, width=140, height=30, text="Voltar", command=pagina_anterior)
    botao_anterior.place(x=435, y=540)

    exibir_pagina_atual()

    # Executa a janela principal
    janela_principal.mainloop()


if __name__ == "__main__":
    criar_frame_principal()
