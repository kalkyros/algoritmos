def biblioteca():
    livros = [
        ["dom casmurro", "beatriz", 7],
        ["1984", "cintia", 18],
        ["o hobbit", "mariana", 31],
        ["o senhor dos anéis", "ana luiza", 2],
        ["a revolução dos bichos", "manuela", 5]
    ]

    livrosposetedias = [livro for livro in livros if livro[2] > 7]
    print("Livros emprestados há mais de 7 dias:")
    for titulo, usuario, dias in livrosposetedias:
        print(f"- {titulo} (Usuário: {usuario}, Dias: {dias})")

    livromaistempo = max(livros, key=lambda x: x[2])
    print(f"\nLivro emprestado há mais tempo: {livromaistempo[0]} (Usuário: {livromaistempo[1]}, Dias: {livromaistempo[2]})")

    usuariospossuilivros = list(set(livro[1] for livro in livros))
    print("\nUsuários com livros emprestados:")
    for usuario in usuariospossuilivros:
        print(f"- {usuario}")

    mediadiasemprestimo = sum(livro[2] for livro in livros) / len(livros)
    print(f"\nMédia de dias de empréstimo: {mediadiasemprestimo:.2f} dias")
biblioteca()