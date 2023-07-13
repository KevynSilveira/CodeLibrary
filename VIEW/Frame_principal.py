import customtkinter
import textwrap
from Funcoes_frame import tema

def criar_frame_principal():
    # Cria a janela principal do código.
    FPrincipal = customtkinter.CTk()
    FPrincipal.geometry("1000x590")
    FPrincipal.title("Biblioteca de comandos")
    FPrincipal.resizable(False, False)

    # Inicializa a posição vertical
    global y_pos  # Indica que estamos utilizando a variável global y_pos
    y_pos = 10

    # Função para cadastrar um novo comando
    def cadastro_comando():
        def cancela_cadastro():
            # Remove a tela de cadastro
            FCadcomando.destroy()

        def cadastrar():
            linguagem = CFiltro.get()
            comando = CComando.get()
            descricao = CDescricao.get("1.0", "end-1c")

            if linguagem != "---Selecione uma linguagem---" and comando != "" and descricao != "":
                FCadcomando.destroy()
            else:
                FCadcomando.destroy()

        # Frame conteúdo, onde ficarão todas as opções de cadastrar um comando
        FCadcomando = customtkinter.CTkFrame(master=FConteudo, width=480, height=330, corner_radius=10)
        FCadcomando.place(x=145, y=45)

        # Label de escolha de linguagem utilizando combobox
        label_CLinguagem = customtkinter.CTkLabel(master=FCadcomando, text="Escolha a linguagem:")
        label_CLinguagem.place(x=10, y=10)

        # Opções de linguagem para o combobox
        opcoes_filtro = ["SQL", "Python", "GIT", "Java"]

        # Campo combobox para selecionar a linguagem pegando como parâmetro as opções de filtro acima
        CFiltro = customtkinter.CTkComboBox(master=FCadcomando, values=opcoes_filtro, width=460, height=30,
                                            state="readonly")
        CFiltro.set("---Selecione uma linguagem---")
        CFiltro.place(x=10, y=40)

        # Label indicativa para cadastrar um comando
        label_CComando = customtkinter.CTkLabel(master=FCadcomando, text="Insira o comando:")
        label_CComando.place(x=10, y=80)

        # Campo de cadastro de comando
        CComando = customtkinter.CTkEntry(master=FCadcomando, width=460, height=30, corner_radius=10)
        CComando.place(x=10, y=110)

        # Label indicativa para descrever o que o comando faz
        label_CDescricao = customtkinter.CTkLabel(master=FCadcomando, text="Insira a descrição:")
        label_CDescricao.place(x=10, y=140)

        # Campo de cadastro de descrição
        CDescricao = customtkinter.CTkTextbox(master=FCadcomando, width=460, height=90, corner_radius=10)
        CDescricao.place(x=10, y=170)

        # Botão de cancelar operação
        BCancelar = customtkinter.CTkButton(master=FCadcomando, width=100, height=30, text="Cancelar",
                                            command=cancela_cadastro)
        BCancelar.place(x=130, y=290)

        # Botão de cadastrar comando
        BCadcomando = customtkinter.CTkButton(master=FCadcomando, width=100, height=30, text="Cadastrar",
                                              command=cadastrar)
        BCadcomando.place(x=260, y=290)

    # Função para criar os frames de conteúdo
    def criar_frame_conteudo(linguagem, comando, descricao):
        global y_pos  # Indica que estamos utilizando a variável global y_pos

        # Definição das variáveis
        linguagem = linguagem
        comando = comando
        descricao = descricao

        # Tamanho máximo de caracteres para a descrição
        max_caracteres = 30

        def mostrar_descricao(y):
            def voltar_descricao():
                MDescricao.destroy()
                BVoltar.destroy()

            MDescricao = customtkinter.CTkTextbox(master=FConteudo, width=740, height=100)
            MDescricao.insert(customtkinter.END, descricao)
            MDescricao.bind("<Key>", lambda e: "break")  # Desativa a entrada do teclado
            MDescricao.place(x=10, y=y)

            BVoltar = customtkinter.CTkButton(master=FConteudo, width=10, height=10, text="", corner_radius=2,
                                              command=voltar_descricao)
            BVoltar.place(x=740, y=y)

        global y_pos  # Indica que estamos utilizando a variável global y_pos

        for _ in range(1):
            # Cria o frame para o conteúdo
            FBlocoConteudo = customtkinter.CTkFrame(master=FConteudo, width=740, height=45)
            FBlocoConteudo.place(x=10, y=y_pos)

            # Cria o frame para exibir a linguagem
            FLinguagem = customtkinter.CTkFrame(master=FBlocoConteudo, width=100, height=45)
            FLinguagem.place(x=0, y=0)
            Llinguagem = customtkinter.CTkLabel(master=FLinguagem, text=linguagem)
            Llinguagem.place(relx=0.5, rely=0.5, anchor="center")

            # Cria o frame para exibir o comando
            FComando = customtkinter.CTkFrame(master=FBlocoConteudo, width=200, height=45)
            FComando.place(x=100, y=0)
            LComando = customtkinter.CTkLabel(master=FComando, text=comando)
            LComando.place(relx=0.5, rely=0.5, anchor="center")

            # Cria o frame para exibir a descrição
            FDescricao = customtkinter.CTkFrame(master=FBlocoConteudo, width=440, height=45)
            FDescricao.place(x=300, y=0)
            BDescricao = customtkinter.CTkButton(master=FDescricao, width=10, height=10, text="", corner_radius=2,
                                                 command=lambda y_pos=y_pos: mostrar_descricao(y_pos))
            BDescricao.place(x=430, y=35)

            # Verifica se o texto excede o limite e adiciona os três pontos se necessário
            if len(descricao) > max_caracteres:
                texto_exibido = textwrap.shorten(descricao, width=max_caracteres - 3, placeholder="...")
            else:
                texto_exibido = descricao
            LDescricao = customtkinter.CTkLabel(master=FDescricao, text=texto_exibido)
            LDescricao.place(relx=0.5, rely=0.5, anchor="center")

            y_pos += 55  # Atualiza a posição vertical para o próximo frame

    # Frame principal
    FLinguagens = customtkinter.CTkFrame(master=FPrincipal, width=200, height=570, corner_radius=10)
    FLinguagens.place(x=10, y=10)

    # Button for SQL
    BSQL = customtkinter.CTkButton(master=FLinguagens, width=180, height=30, text="SQL")
    BSQL.place(x=10, y=10)

    # Button for Python
    BPYTHON = customtkinter.CTkButton(master=FLinguagens, width=180, height=30, text="Python")
    BPYTHON.place(x=10, y=50)

    # Button for GIT
    BGIT = customtkinter.CTkButton(master=FLinguagens, width=180, height=30, text="GIT")
    BGIT.place(x=10, y=90)

    # Button for Java
    BJAVA = customtkinter.CTkButton(master=FLinguagens, width=180, height=30, text="Java")
    BJAVA.place(x=10, y=130)

    # Campo pesquisa
    CPesquisa = customtkinter.CTkEntry(master=FPrincipal, width=510, height=30, corner_radius=10)
    CPesquisa.place(x=220, y=10)

    # Opções da combobox
    opcoes_filtro = ["Linguagem", "Comando", "Descrição"]

    # Botão combobox filtro
    CFiltro = customtkinter.CTkComboBox(master=FPrincipal, values=opcoes_filtro, width=200, height=30,
                                        state="readonly")
    CFiltro.set("---Filtro---")
    CFiltro.place(x=740, y=10)

    # Botão para definir o tema
    BTema = customtkinter.CTkButton(master=FPrincipal, width=40, height=30, text="", command=tema)
    BTema.place(x=950, y=11)

    # Frame conteúdo
    FConteudo = customtkinter.CTkFrame(master=FPrincipal, width=770, height=420, corner_radius=10)
    FConteudo.place(x=220, y=100)

    # Scroll bar do frame conteúdo
    scrollbar = customtkinter.CTkScrollbar(master=FConteudo, )
    scrollbar.place(x=750, y=10)

    # Botão exportar
    BExportar = customtkinter.CTkButton(master=FPrincipal, text="Exportar")
    BExportar.place(x=840, y=540)

    # Botão Cadastrar comando
    BCadastrar = customtkinter.CTkButton(master=FPrincipal, text="Cadastrar", command=cadastro_comando)
    BCadastrar.place(x=670, y=540)

    git = "Git"
    sql = "SQL"
    python = "Python"

    comandoGit = "git add . "
    comandoSQL = "Select * From"
    comandoPython = "import"

    descricaoGit = "Adiciona arquivos no stage"
    descricaoSql = "Seleciona arquivos"
    descricaoPython = "Importa bibliotecas"

    criar_frame_conteudo(git, comandoGit, descricaoGit)
    criar_frame_conteudo(sql, comandoSQL, descricaoSql)
    criar_frame_conteudo(python, comandoPython, descricaoPython)
    criar_frame_conteudo(git, comandoGit, descricaoGit)
    criar_frame_conteudo(sql, comandoSQL, descricaoSql)
    criar_frame_conteudo(python, comandoPython, descricaoPython)
    criar_frame_conteudo(git, comandoGit, descricaoGit)
    criar_frame_conteudo(sql, comandoSQL, descricaoSql)
    criar_frame_conteudo(python, comandoPython, descricaoPython)
    criar_frame_conteudo(git, comandoGit, descricaoGit)
    criar_frame_conteudo(sql, comandoSQL, descricaoSql)
    criar_frame_conteudo(python, comandoPython, descricaoPython)
    criar_frame_conteudo(git, comandoGit, descricaoGit)
    criar_frame_conteudo(sql, comandoSQL, descricaoSql)
    criar_frame_conteudo(python, comandoPython, descricaoPython)
    criar_frame_conteudo(git, comandoGit, descricaoGit)
    criar_frame_conteudo(sql, comandoSQL, descricaoSql)
    criar_frame_conteudo(python, comandoPython, descricaoPython)


    # Executa o Frame principal
    FPrincipal.mainloop()


if __name__ == "__main__":
    criar_frame_principal()
