import customtkinter
import tkinter as tk

def Cria_frame_principal():
    #Cria a janela principal do codigo.
    FPrincipal = customtkinter.CTk()
    FPrincipal.geometry("1000x590")
    FPrincipal.title("Biblioteca de comandos")
    FPrincipal.resizable(False, False)

    FLinguagens = customtkinter.CTkFrame(master=FPrincipal, width=200, height=570, corner_radius=10)
    FLinguagens.place(x=10, y=10)

    FConteudo = customtkinter.CTkFrame(master=FPrincipal, width=770, height=480, corner_radius=10)
    FConteudo.place(x=220, y=100)

    opcoes_filtro = ["Linguagem", "Codigo", "Conteudo"]
    CFiltro = customtkinter.CTkComboBox(master=FPrincipal, values=opcoes_filtro, width=200, height=30)
    CFiltro.place(x=790, y=10)

    CPesquisa = customtkinter.CTkEntry(master=FPrincipal, width=540, height=30, corner_radius=10)
    CPesquisa.place(x=240, y=10)

    text = CPesquisa.get()

    label_selecione_layout = customtkinter.CTkLabel(master=FConteudo, text="Selecione o layout")
    label_selecione_layout.place(x=60, y=900)

    BExportar = customtkinter.CTkButton(master=FPrincipal, text="Exportar")
    BExportar.place(x=840, y=540)

    scrollbar = customtkinter.CTkScrollbar(FConteudo)
    scrollbar.place(x=750, y=10)

    FPrincipal.mainloop()

if __name__ == "__main__":
    Cria_frame_principal()
