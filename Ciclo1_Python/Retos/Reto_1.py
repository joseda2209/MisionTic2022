"""
Created on Fri Sep 18 15:23:02 2020

@author: Joseda2209

"""
def nota_quices(CodEst, N1 = 0, N2 = 0, N3 = 0, N4 = 0, N5 = 0):
    """
    
    Elimina la menor nota y muestra el promedio de las notas en escala: 0-5 del estudiante

    Parameters
    ----------
    CodEst : str
       codigo alfanumerico del estudiante.
    N1 : int, optional
        nota 1. The default is 0.
    N2 : int, optional
        nota 2. The default is 0.
    N3 : int, optional
        nota 3. The default is 0.
    N4 : int, optional
        nota 4. The default is 0.
    N5 : str, optional
        nota5. The default is 0.

   
    Returns
    -------
    respuesta : str
        El promedio ajustado del estudiante {CodEst} es: {promedio}.

    """
    
    #operacion para escalar 0-100 a  0-5
    escalar = lambda N : round(N/20,2)
    

    #descartar la nota minima
    minNota = min(N1,N2,N3,N4,N5)
    #suma las cinco notas y resta la menor
    SumaNotas = sum((N1,N2,N3,N4,N5))-minNota
    #calcular y escalar el promedio
    Promed= SumaNotas / 4
    Promed = escalar(Promed)
    
    #sentencia de retorno
    respuesta = 'El promedio ajustado del estudiante {} es: {}'
    return respuesta.format(CodEst,Promed)

print(nota_quices('AA0010276',19,90,38,55,68))
print(nota_quices('IS00201620',37,10,50,19,79))
print(nota_quices('BI02201810',45,46,33,74,22))
print(nota_quices('IQ102201810',57,100,87,93,21))
print(nota_quices('MA00201520',5,14,76,91,5))
