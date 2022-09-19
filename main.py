

# Exercicio 7.1. Executar tres veces o programa potencia con valores de entrada (3,5), (3,3) e (5,3) respectivamente. Que sucede en cada caso?

listatupla= (1,2,3,4,5,6)
listaMap={
    1:9,
    2:8,
    3:7,
    4:8
}

def tuplaTrueFalse(lista):
    min=lista[0]
    bien=True
    for elementoTupla in lista:

        elemento = elementoTupla
        if elemento >= min:
            min=elementoTupla
        else:
            print("la lista no esta ordenada")
            bien=False
            break

    if bien==True:
        print("lista ordenada")
tuplaTrueFalse(listatupla)



#Escribir unha función que indique si duas fichas de dominó encaixan ou non. As fichas recíbense en duas tuplas, por exemplo: (3,4) y (5,4).
