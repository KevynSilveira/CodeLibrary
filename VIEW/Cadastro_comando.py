import customtkinter

def cadastro_comando():
    # Cria a janela principal do código.
    FCadcomando = customtkinter.CTk()
    FCadcomando.geometry("500x330")
    FCadcomando.title("cadastro comando")
    FCadcomando.resizable(False, False)

    # Frame conteudo
    FConteudo = customtkinter.CTkFrame(master=FCadcomando, width=480, height=270, corner_radius=10)
    FConteudo.place(x=10, y=10)

    label_CLinguagem = customtkinter.CTkLabel(master=FConteudo, text="Insira a linguagem:")
    label_CLinguagem.place(x=10, y=10)

    opcoes_filtro = ["SQL", "Python", "GIT", "Java"]

    CFiltro = customtkinter.CTkComboBox(master=FConteudo, values=opcoes_filtro, width=460, height=30)
    CFiltro.place(x=10, y=40)

    label_CComando = customtkinter.CTkLabel(master=FConteudo, text="Insira o comando:")
    label_CComando.place(x=10, y=80)

    # Campo comando
    CComando = customtkinter.CTkEntry(master=FConteudo, width=460, height=30, corner_radius=10)
    CComando.place(x=10, y=110)
    text = CComando.get()

    label_CDescricao = customtkinter.CTkLabel(master=FConteudo, text="Insira a descrição:")
    label_CDescricao.place(x=10, y=140)

    # Campo descricao
    CDescricao = customtkinter.CTkTextbox(master=FConteudo, width=460, height=90, corner_radius=10)
    CDescricao.place(x=10, y=170)

    # Botao para definir o tema
    BCancelar = customtkinter.CTkButton(master=FCadcomando, width=100, height=30, text="Cancelar")
    BCancelar.place(x=130, y=290)

    # Botao para definir o tema
    BCadcomando = customtkinter.CTkButton(master=FCadcomando, width=100, height=30, text="Cadastrar")
    BCadcomando.place(x=260, y=290)

    FCadcomando.mainloop()


if __name__ == "__main__":
    cadastro_comando()