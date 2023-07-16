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

sql = "SQL"
comando_sql = "Select * From"
descricao_sql = "Seleciona arquivos"

python = "Python"
comando_python = "import"
descricao_python = "Importa bibliotecas"

git = "Git"
comando_git = "git add . "
descricao_git = "Adiciona arquivos no stage"

conteudo_pages = [
    [(sql, comando_sql, descricao_sql), (python, comando_python, descricao_python), (git, comando_git, descricao_git)],
    [(sql, comando_sql, descricao_sql), (python, comando_python, descricao_python),
     (git, comando_git, descricao_git)],
    [(sql, comando_sql, descricao_sql), (python, comando_python, descricao_python),
     (git, comando_git, descricao_git)]
]

total_pages = len(conteudo_pages)

# Variáveis para funcionalidade de navegação do livro
global pagina_atual
pagina_atual = 0
global fconteudo
global criar_frame

def proxima_pagina():
    global pagina_atual
    pagina_atual
    if pagina_atual < total_pages - 1:
        pagina_atual += 1
        exibir_pagina_atual(fconteudo, criar_frame)

def pagina_anterior():
    global pagina_atual
    pagina_atual
    if pagina_atual > 0:
        pagina_atual -= 1
        exibir_pagina_atual(fconteudo, criar_frame)

def exibir_pagina_atual(frame_conteudo, criar_frame_conteudo):
    global y_pos
    y_pos = 10

    #global fconteudo
    #global criar_frame
    #fconteudo = frame_conteudo
    #criar_frame = criar_frame_conteudo

    for widget in frame_conteudo.winfo_children():
        widget.destroy()

    conteudo_pagina = conteudo_pages[pagina_atual]
    for conteudo in conteudo_pagina:
        criar_frame_conteudo(*conteudo)