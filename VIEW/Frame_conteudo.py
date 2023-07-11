import customtkinter

linguagem = "SQL"
comando = "Select * From"
descricao = "Seleciona o campo indicado"



def criar_frame_conteudo(linguagem, comando, descricao):
    # Cria a janela principal do código.
    FPrincipal = customtkinter.CTk()
    FPrincipal.geometry("1000x590")
    FPrincipal.title("Biblioteca de comandos")
    FPrincipal.resizable(False, False)

    FConteudo = customtkinter.CTkFrame(master=FPrincipal, width=500, height=60)
    FConteudo.place(x=250, y=10)

    FLinguagem = customtkinter.CTkFrame(master=FConteudo, width=50, height=60)
    FLinguagem.place(x=0, y=0)
    Llinguagem = customtkinter.CTkLabel(master=FLinguagem, text=linguagem)
    Llinguagem.place(x=0, y=0)

    FComando = customtkinter.CTkFrame(master=FConteudo, width=100, height=60)
    FComando.place(x=50, y=0)
    LComando = customtkinter.CTkLabel(master=FComando, text=comando)
    LComando.place(x=0, y=0)

    FDescricao = customtkinter.CTkFrame(master=FConteudo, width=350, height=60)
    FDescricao.place(x=150, y=0)
    LDescricao = customtkinter.CTkLabel(master=FDescricao, text=descricao)
    LDescricao.place(x=0, y=0)


    FPrincipal.mainloop()

criar_frame_conteudo(linguagem, comando, descricao)