import customtkinter

def cadastro_comando():
    # Cria a janela principal do código.
    FCadcomando = customtkinter.CTk()
    FCadcomando.geometry("500x330")
    FCadcomando.title("cadastro comando")
    FCadcomando.resizable(False, False)

    # Frame conteudo, onde ficara todas as opcoes de cadastar um comando
    FCadcomando = customtkinter.CTkFrame(master=FCadcomando, width=480, height=270, corner_radius=10)
    FCadcomando.place(x=10, y=10)

    # Label de escolha de linguagem utilizando combobox
    label_CLinguagem = customtkinter.CTkLabel(master=FCadcomando, text="Escolha a linguagem:")
    label_CLinguagem.place(x=10, y=10)

    #Opcoes de linguagem para o combobox
    opcoes_filtro = ["SQL", "Python", "GIT", "Java"]

    #Campo combobox para selecionar a linguem pegando como parametro as opcoes de filtro acima
    CFiltro = customtkinter.CTkComboBox(master=FCadcomando, values=opcoes_filtro, width=460, height=30)
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

    # Campo de cadastro de descricao
    CDescricao = customtkinter.CTkTextbox(master=FCadcomando, width=460, height=90, corner_radius=10)
    CDescricao.place(x=10, y=170)

    # Botao de cancelar operacao
    BCancelar = customtkinter.CTkButton(master=FCadcomando, width=100, height=30, text="Cancelar")
    BCancelar.place(x=130, y=290)

    # Botao de cadastrar comando
    BCadcomando = customtkinter.CTkButton(master=FCadcomando, width=100, height=30, text="Cadastrar")
    BCadcomando.place(x=260, y=290)

    FCadcomando.mainloop()

if __name__ == "__main__":
    cadastro_comando()