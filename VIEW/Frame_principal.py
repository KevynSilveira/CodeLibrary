import customtkinter
from Funcoes_frame import tema

def criar_frame_principal():
    # Cria a janela principal do código.
    FPrincipal = customtkinter.CTk()
    FPrincipal.geometry("1000x590")
    FPrincipal.title("Biblioteca de comandos")
    FPrincipal.resizable(False, False)

    #funcoes
    def cadastro_comando():

        #FCadcomando = customtkinter.CTkFrame(master=FPrincipal, width=500, height=330, corner_radius=10)
        #FCadcomando.place(x=250, y=130)

        # Frame conteudo, onde ficara todas as opcoes de cadastar um comando
        FRequisitocad = customtkinter.CTkFrame(master=FConteudo, width=480, height=330, corner_radius=10)
        FRequisitocad.place(x=145, y=45)

        # Label de escolha de linguagem utilizando combobox
        label_CLinguagem = customtkinter.CTkLabel(master=FRequisitocad, text="Escolha a linguagem:")
        label_CLinguagem.place(x=10, y=10)

        # Opcoes de linguagem para o combobox
        opcoes_filtro = ["SQL", "Python", "GIT", "Java"]

        # Campo combobox para selecionar a linguem pegando como parametro as opcoes de filtro acima
        CFiltro = customtkinter.CTkComboBox(master=FRequisitocad, values=opcoes_filtro, width=460, height=30)
        CFiltro.place(x=10, y=40)

        # Label indicativa para cadastrar um comando
        label_CComando = customtkinter.CTkLabel(master=FRequisitocad, text="Insira o comando:")
        label_CComando.place(x=10, y=80)

        # Campo de cadastro de comando
        CComando = customtkinter.CTkEntry(master=FRequisitocad, width=460, height=30, corner_radius=10)
        CComando.place(x=10, y=110)

        # Label indicativa para descrever o que o comando faz
        label_CDescricao = customtkinter.CTkLabel(master=FRequisitocad, text="Insira a descrição:")
        label_CDescricao.place(x=10, y=140)

        # Campo de cadastro de descricao
        CDescricao = customtkinter.CTkTextbox(master=FRequisitocad, width=460, height=90, corner_radius=10)
        CDescricao.place(x=10, y=170)

        # Botao de cancelar operacao
        BCancelar = customtkinter.CTkButton(master=FRequisitocad, width=100, height=30, text="Cancelar")
        BCancelar.place(x=130, y=290)

        # Botao de cadastrar comando
        BCadcomando = customtkinter.CTkButton(master=FRequisitocad, width=100, height=30, text="Cadastrar")
        BCadcomando.place(x=260, y=290)


    # Frame principal
    FLinguagens = customtkinter.CTkFrame(master=FPrincipal, width=200, height=570, corner_radius=10)
    FLinguagens.place(x=10, y=10)

    # Campo pesquisa
    CPesquisa = customtkinter.CTkEntry(master=FPrincipal, width=510, height=30, corner_radius=10)
    CPesquisa.place(x=220, y=10)
    text = CPesquisa.get()

    # Opcoes da combobox
    opcoes_filtro = ["Linguagem", "Comando", "Descrição"]

    # Botao combobox filtro
    CFiltro = customtkinter.CTkComboBox(master=FPrincipal, values=opcoes_filtro, width=200, height=30)
    CFiltro.place(x=740, y=10)

    # Botao para definir o tema
    BTema = customtkinter.CTkButton(master=FPrincipal, width=40, height=30, text="", command=tema)
    BTema.place(x=950, y=11)

    # Frame conteudo
    FConteudo = customtkinter.CTkFrame(master=FPrincipal, width=770, height=420, corner_radius=10)
    FConteudo.place(x=220, y=100)

    # Scroll bar do frame conteudo
    scrollbar = customtkinter.CTkScrollbar(FConteudo)
    scrollbar.place(x=750, y=10)

    # Botao exportar
    BExportar = customtkinter.CTkButton(master=FPrincipal, text="Exportar")
    BExportar.place(x=840, y=540)

    # Botao Cadastrar comando
    BCadastrar = customtkinter.CTkButton(master=FPrincipal, text="Cadastrar", command=cadastro_comando)
    BCadastrar.place(x=670, y=540)

    # Executa o Frame principal
    FPrincipal.mainloop()


if __name__ == "__main__":
    criar_frame_principal()
