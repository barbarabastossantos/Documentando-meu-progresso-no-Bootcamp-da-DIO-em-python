# para saber se um conjunto pertence a outro

conjunto_a={1,2,3}
conjunto_b={4,1,2,5,6,3}
print("Conjunto A ", conjunto_a)
print("Conjunto B ", conjunto_b)
print("Todos os elementos de A estão em B ? ", conjunto_a.issubset(conjunto_b))
print("Todos os elementos de B estão em A ? ", conjunto_b.issubset(conjunto_a))