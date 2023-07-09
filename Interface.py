import customtkinter

#Armazena o tema atual do frame
tema_atual = "dark"

def tema():
    global tema_atual
    if tema_atual == "light":
        customtkinter.set_appearance_mode("dark")
        tema_atual = "dark"
    else:
        customtkinter.set_appearance_mode("light")
        tema_atual = "light"

def criar_frame_principal():
    # Cria a janela principal do código.
    FPrincipal = customtkinter.CTk()
    FPrincipal.geometry("1000x590")
    FPrincipal.title("Biblioteca de comandos")
    FPrincipal.resizable(False, False)

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
    FConteudo = customtkinter.CTkFrame(master=FPrincipal, width=770, height=480, corner_radius=10)
    FConteudo.place(x=220, y=100)

    # Scroll bar do frame conteudo
    scrollbar = customtkinter.CTkScrollbar(FConteudo)
    scrollbar.place(x=750, y=10)

    # Botao exportar
    BExportar = customtkinter.CTkButton(master=FPrincipal, text="Exportar")
    BExportar.place(x=840, y=540)

    # Executa o Frame principal
    #FPrincipal.mainloop()

def cadastro_comando():
    # Cria a janela principal do código.
    FCadcomando = customtkinter.CTk()
    FCadcomando.geometry("600x450")
    FCadcomando.title("cadastro comando")
    FCadcomando.resizable(False, False)

    # Frame conteudo
    FConteudo = customtkinter.CTkFrame(master=FCadcomando, width=580, height=350, corner_radius=10)
    FConteudo.place(x=10, y=60)

    label_CLinguagem = customtkinter.CTkLabel(master=FConteudo, text="Insira a linguagem:")
    label_CLinguagem.place(x=20, y=10)

    # Campo linguagem
    CLinguagem = customtkinter.CTkEntry(master=FConteudo, width=560, height=30, corner_radius=10)
    CLinguagem.place(x=20, y=40)
    text = CLinguagem.get()

    label_CComando = customtkinter.CTkLabel(master=FConteudo, text="Insira o comando:")
    label_CComando.place(x=20, y=80)

    # Campo comando
    CComando = customtkinter.CTkEntry(master=FConteudo, width=560, height=30, corner_radius=10)
    CComando.place(x=20, y=110)
    text = CComando.get()

    label_CDescricao = customtkinter.CTkLabel(master=FConteudo, text="Insira a descrição:")
    label_CDescricao.place(x=20, y=140)

    # Campo descricao
    CDescricao = customtkinter.CTkEntry(master=FConteudo, width=560, height=30, corner_radius=10)
    CDescricao.place(x=20, y=170)
    text = CDescricao.get()

    FCadcomando.mainloop()



if __name__ == "__main__":
    cadastro_comando()
