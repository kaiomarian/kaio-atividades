# Classe Livro
class Livro:
    def _init_(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.status = "Disponível"

    def verificar_disponibilidade(self):
        return self.status == "Disponível"

    def alterar_status(self, novo_status):
        self.status = novo_status




def devolver_livro(titulo):
    for livro in biblioteca:
        if livro.titulo == titulo:
            livro.alterar_status("Disponível")
            print("Livro devolvido com sucesso!")
            return
    print("Livro não encontrado na biblioteca.")


def exibir_livros_disponiveis():
    print("Livros disponíveis na biblioteca:")
    for livro in biblioteca:
        if livro.verificar_disponibilidade():
            print(f"- {livro.titulo} por {livro.autor} ({livro.ano_publicacao})")


# Programa principal
import biblioteca

while True:
    print("\n=== Menu ===")
    print("1. Adicionar livro")
    print("2. Emprestar livro")
    print("3. Devolver livro")
    print("4. Exibir livros disponíveis")
    print("5. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        titulo = input("Digite o título do livro: ")
        autor = input("Digite o autor do livro: ")
        ano = input("Digite o ano de publicação do livro: ")
        novo_livro = biblioteca.Livro(titulo, autor, ano)
        biblioteca.adicionar_livro(novo_livro)
        print("Livro adicionado com sucesso!")

    elif opcao == "2":
        titulo = input("Digite o título do livro a ser emprestado: ")
        biblioteca.emprestar_livro(titulo)

    elif opcao == "3":
        titulo = input("Digite o título do livro a ser devolvido: ")
        biblioteca.devolver_livro(titulo)

    elif opcao == "4":
        biblioteca.exibir_livros_disponiveis()

    elif opcao == "5":
        print("Saindo do programa...")
        break

    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")