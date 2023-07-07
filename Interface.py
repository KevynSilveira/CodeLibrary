import customtkinter

def Cria_frame_principal():
    #Cria a janela principal do codigo.
    FPrincipal = customtkinter.CTk()
    FPrincipal.geometry("1000x700")
    FPrincipal.title("Biblioteca de comandos")
    FPrincipal.resizable(False, False)
    FPrincipal.mainloop()



if __name__ == "__main__":
    Cria_frame_principal()
