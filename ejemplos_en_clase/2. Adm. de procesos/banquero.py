#!/usr/bin/python3

procesos = ['A', 'B', 'C', 'D']
reclamo = {'A': 3,
           'B': 4,
           'C': 2,
           'D': 3
           }
asignado = {'A': 3, 'B': 0, 'C': 2, 'D': 0}
# solicita = {'A': 0, 'B': 0, 'C': 0, 'D': 0}

disponibles = 6
libres = 6

def asigna(quien, cuanto):
    maximo = reclamo[quien] - asignado[quien]
    print('== Partamos de que: ==')
    print('== Reclamo:  ', reclamo)
    print('== Asignado: ', asignado)
    print('%s solicita %d' % (quien, cuanto))

    if cuanto > maximo:
        print('¡Nanai! (%d > %d)' % (cuanto, maximo) )
        return False

    if cuanto > libres:
        print('Se pasa a la sala de espera... (%d > %d)' % (cuanto, libres))

    restantes = {}
    for p in procesos:
        restantes[p] = reclamo[p] - asignado[p]
    restantes[quien] += cuanto

    while len(restantes.keys()) != 0:
        menor = encuentra_candidato(restantes)
        print('Mi candidato es "%s"  ' %
              (menor))
        print(restantes)
        recursos = restantes[menor]
        if libres < recursos:
            raise RuntimeError('¡No quedan suficientes para que %s termine',
                               menor)
        del(restantes[menor])

    print('Llegamos a un estado seguro')
    return(True)

def encuentra_candidato(restantes):
    candidato = min(restantes, key=restantes.get)
    return(candidato)

asigna('B', 2)
