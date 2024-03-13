# Módulo biblioteca
biblioteca = []


def adicionar_livro(livro):
    biblioteca.append(livro)


def emprestar_livro(titulo):
    for livro in biblioteca:
        if livro.titulo == titulo:
            if livro.verificar_disponibilidade():
                livro.alterar_status("Emprestado")
                print("Livro emprestado com sucesso!")
            else:
                print("O livro não está disponível no momento.")
            return
    print("Livro não encontrado na biblioteca.")
