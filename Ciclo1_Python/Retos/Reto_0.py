# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 10:10:15 2020

@author: Daniel
"""

def inicio_reaccion(codigo: str, hora_terminacion: int, minuto_terminacion: int,
duracion_horas:int, duracion_minutos:int, duracion_segundos:int) -> str:
    '''
    
    funcion que calcula la hora de inicio de los experimentos dependiendo de su hora de finalizacion y su duracion
    Parameters
    ----------
    codigo : str
        codigo del experimento.
    hora_terminacion : int
        Hora requerida para la finalizacion de la reaccion.
    minuto_terminacion : int
        Minuto requerido para la finalizacion de la reaccion.
    duracion_horas : int
        Estimacion de las horas que dura la reaccion.
    duracion_minutos : int
        Estimacion de los minutos que dura la reaccion.
    duracion_segundos : int
        Estimacion de los segundos que dura la reaccion.

    Returns
    -------
    str
        Texto con la siguiente estructura: "La reacción {código} debe iniciarse a las {hh}
        horas, {mm} minutos con {ss} segundos para que esté lista en en el momento
        requerido".

    '''
    #calcular total de segundos de finalizacion y duracion
    segFin = hora_terminacion* 3600 + minuto_terminacion * 60
    segDur = duracion_horas * 3600 + duracion_minutos * 60 + duracion_segundos
    #diferencia de los segundos
    segIni = segFin - segDur
    #Calcular hora minutos y segundos iniciales
    horaIni = segIni // 3600
    segIni = segIni % 3600
    minIni = segIni // 60
    segIni = segIni % 60
     
    #organizar string de salida
    respuesta = 'La reacción {} debe iniciarse a las {} horas, {} minutos con {} '
    respuesta += 'segundos para que esté lista en en el momento requerido'
    return respuesta.format(codigo, horaIni, str(minIni).zfill(2), str(segIni).zfill(2))
 
    
print(inicio_reaccion('HHA01', 16, 30, 4, 11, 23))
print(inicio_reaccion('IQ100', 16, 30, 7, 24, 58))
