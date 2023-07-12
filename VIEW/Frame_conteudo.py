import customtkinter

# Definição das variáveis
linguagem = "SQL"
comando = "Select * From"
descricao = "Seleciona o campo indicado"

# Função para criar o frame de conteúdo
def criar_frame_conteudo(linguagem, comando, descricao):

    def mostrar_descricao():
        MDescricao = customtkinter.CTkTextbox(master=FPrincipal, width=500, height=100)
        MDescricao.insert(customtkinter.END, descricao)
        MDescricao.place(x=250, y=10)



    # Cria a janela principal do código.
    FPrincipal = customtkinter.CTk()
    FPrincipal.geometry("1000x590")  # Define as dimensões da janela
    FPrincipal.title("Biblioteca de comandos")  # Define o título da janela
    FPrincipal.resizable(False, False)  # Desabilita o redimensionamento da janela

    # Cria o frame para o conteúdo
    FConteudo = customtkinter.CTkFrame(master=FPrincipal, width=500, height=45)
    FConteudo.place(x=250, y=10)

    # Cria o frame para exibir a linguagem
    FLinguagem = customtkinter.CTkFrame(master=FConteudo, width=50, height=45)
    FLinguagem.place(x=0, y=0)
    Llinguagem = customtkinter.CTkLabel(master=FLinguagem, text=linguagem)
    Llinguagem.place(relx=0.5, rely=0.5, anchor="center")

    # Cria o frame para exibir o comando
    FComando = customtkinter.CTkFrame(master=FConteudo, width=100, height=45)
    FComando.place(x=50, y=0)
    LComando = customtkinter.CTkLabel(master=FComando, text=comando)
    LComando.place(relx=0.5, rely=0.5, anchor="center")

    # Cria o frame para exibir a descrição
    FDescricao = customtkinter.CTkFrame(master=FConteudo, width=350, height=45)
    FDescricao.place(x=150, y=0)
    LDescricao = customtkinter.CTkLabel(master=FDescricao, text=descricao)
    LDescricao.place(relx=0.5, rely=0.5, anchor="center")
    BDescricao = customtkinter.CTkButton(master=FDescricao, width=10, height=10, text="", corner_radius=2, command=mostrar_descricao)
    BDescricao.place(x=340, y=35)


    # Inicia o loop principal da janela
    FPrincipal.mainloop()

# Chama a função para criar o frame de conteúdo com as informações fornecidas
criar_frame_conteudo(linguagem, comando, descricao)
