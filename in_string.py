def check_vowels():
    nombre1 = input("Ingrese un nombre: ")

    a = ('a', 'A')
    e = ('e', 'E')
    i = ('i', 'I')
    o = ('o', 'O')
    u = ('u', 'U')

    print("Contiene a:", a[0] in nombre1 or a[1] in nombre1)
    print("Contiene e:", e[0] in nombre1 or e[1] in nombre1)
    print("Contiene i:", i[0] in nombre1 or i[1] in nombre1)
    print("Contiene o:", o[0] in nombre1 or o[1] in nombre1)
    print("Contiene u:", u[0] in nombre1 or u[1] in nombre1)
