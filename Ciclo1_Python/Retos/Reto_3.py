# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 15:58:46 2020

@author: Daniel
"""

    
def ruteo(distancias: dict, ruta_inicial: list)-> dict:
    """
    funcion que genera una ruta optimizada basada en una matriz de distancias
    
    Parameters
    ----------
    distancias : dict
        cada llave {i,j} se relaciona con el valor de la distancia entre i y j.
    ruta_inicial : list
        contiene el orden de visita segun la ruta actual.

    Returns
    -------
    dict
        ruta: la nueva ruta.
        distancia: valor de distancia total

    """
    
    #validacion de los valores del diccionario
    for key , elemento in distancias.items():
        if elemento < 0:
            return "Por favor revisar los datos de entrada."
        if key[0] == key[1]:
            if elemento != 0:
                return "Por favor revisar los datos de entrada."
        
    #metodo para buscar la distancia
    def dist(lista: list)->int:
        distancia = 0
        for i in range(0,len(lista)-1):
            distancia += distancias[(lista[i],lista[i+1])]
        return distancia
    
    #permutar una lista
    def permutar(lista: list)->tuple:
        permutaciones = list()
        for i in range(1,len(lista)-2):
            for j in range(i+1,len(lista)-1):
                permutaciones.append((lista[i],lista[j]))
        return permutaciones

    #iniciar la distancia inicial
    ruta_menor = ruta_inicial.copy()
    distancia = dist(ruta_inicial)
    distancia_menor = 0
        
    #iteracion para crear nueva ruta
    while distancia_menor < distancia: #corregir condicion
        #se crean los posibles cambios
        ruta = ruta_menor.copy()
        distancia = dist(ruta)
        cambios = permutar(ruta)
        #realiza cada uno de los cambios
        for cambio in cambios:
            ruta_nueva = ruta.copy()
            #crea la nueva ruta
            for i in range(0, len(ruta_nueva)-1):
                if ruta_nueva[i] == cambio[0]:
                    ruta_nueva[i] = cambio[1]
                elif ruta_nueva[i]== cambio[1]:
                    ruta_nueva[i] = cambio[0]
            distancia_nueva = dist(ruta_nueva)
            #si la distancia de la nueva ruta es menor que la ruta menor guardada
            if distancia_nueva < dist(ruta_menor):
                #actualiza la menor ruta
                ruta_menor = ruta_nueva.copy()
                distancia_menor = dist(ruta_menor)
                
    #crea la respuesta
    respuesta = {'ruta': '-'.join(ruta), 'distancia': distancia }
    return respuesta
        
    
distancias_2 = {('H', 'H'): 0, ('H', 'A'): 60, ('H', 'B'): 202, ('H', 'C'): 206, ('H', 'D'): 40, ('H', 'E'): 27,
('A', 'H'): 72, ('A', 'A'): 0, ('A', 'B'): 135, ('A', 'C'): 150, ('A', 'D'): 240, ('A', 'E'): 117,
('B', 'H'): 188, ('B', 'A'): 166, ('B', 'B'): 0, ('B', 'C'): 149, ('B', 'D'): 126, ('B', 'E'): 199,
('C', 'H'): 39, ('C', 'A'): 19, ('C', 'B'): 123, ('C', 'C'): 0, ('C', 'D'): 206, ('C', 'E'): 19,
('D', 'H'): 45, ('D', 'A'): 14, ('D', 'B'): 110, ('D', 'C'): 95, ('D', 'D'): 0, ('D', 'E'): 31,
('E', 'H'): 36, ('E', 'A'): 179, ('E', 'B'): 235, ('E', 'C'): 106, ('E', 'D'): 25, ('E', 'E'): 0}

distancias_1 = {('H', 'H'): 0, ('H', 'A'): 21, ('H', 'B'): 57, ('H', 'C'): 58, ('H', 'D'): 195, ('H', 'E'): 245, ('H', 'F'): 241,
('A', 'H'): 127, ('A', 'A'): 0, ('A', 'B'): 231, ('A', 'C'): 113, ('A', 'D'): 254, ('A', 'E'): 179, ('A', 'F'): 41,
('B', 'H'): 153, ('B', 'A'): 252, ('B', 'B'): 0, ('B', 'C'): 56, ('B', 'D'): 126, ('B', 'E'): 160, ('B', 'F'): 269,
('C', 'H'): 196, ('C', 'A'): 128, ('C', 'B'): 80, ('C', 'C'): 0, ('C', 'D'): 136, ('C', 'E'): 37, ('C', 'F'): 180,
('D', 'H'): 30, ('D', 'A'): 40, ('D', 'B'): 256, ('D', 'C'): 121, ('D', 'D'): 0, ('D', 'E'): 194, ('D', 'F'): 109,
('E', 'H'): 33, ('E', 'A'): 144, ('E', 'B'): 179, ('E', 'C'): 114, ('E', 'D'): 237, ('E', 'E'): 0, ('E', 'F'): 119,
('F', 'H'): 267, ('F', 'A'): 61, ('F', 'B'): 79, ('F', 'C'): 39, ('F', 'D'): 135, ('F', 'E'): 55, ('F', 'F'): 0}


print(ruteo(distancias_1,['H', 'A', 'B', 'C', 'D', 'E', 'F', 'H']))
print(ruteo(distancias_2,['H', 'B', 'E', 'A', 'C', 'D', 'H']))