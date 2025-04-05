#se um valor ja existe ele não altera se não existe ele adiciona

contato={"nome":"Barbara","telefone":"9999999"}
contato.setdefault("nome","Giovanna")
print(contato)
contato.setdefault("idade",28)
print(contato)