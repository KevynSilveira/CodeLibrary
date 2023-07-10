import customtkinter

#Armazena o tema atual do frame
tema_atual = "dark"

def tema():#Muda o tema do frame para a cor oposta
    global tema_atual
    if tema_atual == "light":
        customtkinter.set_appearance_mode("dark")
        tema_atual = "dark"
    else:
        customtkinter.set_appearance_mode("light")
        tema_atual = "light"
