# isdisjoint os elementos não  se tocam, não tem interserção

conjunto_a={1,2,3,4,5}
conjunto_b={6,7,8,9}
conjunto_c={1,0}

print(" Conjunto A : ",conjunto_a, " \n Conjunto B : ",conjunto_b, " \n Conjunto C : ", conjunto_c )
print("\n O conjunto A tem alguma interserção com o conjunto B ? ", conjunto_a.isdisjoint(conjunto_b))
print(" O conjunto A tem alguma interserção com o conjunto C ? ", conjunto_a.isdisjoint(conjunto_c))
