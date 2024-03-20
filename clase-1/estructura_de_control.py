
if True != False:
    print("No se ejecuta")
elif True == True:
    print('Se ejecuta')
else:
    print('Se ejecuta')


# while

# while True:
#     print('Se ejecuta')
#     break


# for in
mi_lista = [10, 20, 30, 40, 50]

# for i in mi_lista:
#     print(i)

# for i in range(0, 10, 1):
#     print(i)

# for i in range(10, 1, -1):
#     print(i)

# metodo enumerate
for i, x in enumerate(mi_lista):
    print(i, x)

