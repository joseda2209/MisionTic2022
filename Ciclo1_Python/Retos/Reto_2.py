# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 11:20:57 2020

@author: Daniel
"""

def prestamo(informacion: dict) -> dict:
    '''
    Funcion que permite decir si un credito es aprobado o no dependiendo del estado del aplicante.
    

    Parameters
    ----------
    informacion : dict
        Diccionario con la informacion de la peticion del prestamo.
        
        id_prestamo: str, Codigo alfanumerico
        casado: str, Si/No
        dependientes: int/str, 0,1,2,'3+'
        educacion: str, Graduado/No Graduado
        independiente: str, Si/No
        ingreso_deudor: float, ingreso del aplicante
        ingreso_codeudor: float, Ingreso del codeudor
        cantidad_prestamo: float, Cantidad del credito solicitado
        plazo_prestamo: int, Plazo del credito
        historia_credito: int, 1/0
        tipo_propiedad: str, Urbano/Rural/Semiurbano

    Returns
    -------
    dict
        Diccionario con la informacion de aprobacion del prestamo.
        
        id_prestamo: str
        aprobado: bool

    '''
    Resp = {
        'id_prestamo': informacion['id_prestamo'],
        'aprobado': False
        }
    i_c = informacion['ingreso_codeudor']
    i_d = informacion['ingreso_deudor']
    c_p = informacion['cantidad_prestamo']
    if isinstance(informacion['dependientes'],str):
        informacion['dependientes'] = 3
    
    #Historia de Credito
    #Rama Izquierda
    if informacion['historia_credito'] == 1:
        #Rama Izquierda
       if i_c > 0 and i_d/9 > c_p:    
           Resp['aprobado'] = True
       #Rama Derecha
       else:
           #Rama Izquierda
           if informacion['dependientes'] > 2 and informacion['independiente'] == 'Si':
               Resp['aprobado'] = i_c/12 > c_p
           #Rama Derecha
           else:
               Resp['aprobado'] = c_p < 200
    #Rama derecha
    else:
        #Rama Izquierda
        if informacion['independiente'] == 'Si':
            #Rama Izquierda
            if informacion['casado'] == 'No' and informacion['dependientes'] <= 1:
                #Rama Izquierda
                if(i_d / 10 > c_p) or (i_c / 10 > c_p):
                    Resp['aprobado'] = c_p <180
                #Rama Derecha
                else:
                    Resp['aprobado'] = False
            #Rama derecha
            else:
                Resp['aprobado'] = False
        #Rama Derecha
        else:
            #Rama Izquierda
            if not(informacion['tipo_propiedad'] == 'Semiurbano') and (informacion['dependientes'] < 2):
                #Rama Izquierda
                if (informacion['educacion'] == 'Graduado') :
                    Resp['aprobado'] = (i_d / 11 > c_p) and (i_c / 11 > c_p)
                #Rama Derecha
                else:
                    Resp['aprobado'] = False
            #Rama Derecha
            else:
                Resp['aprobado'] = False
    return Resp

P_1 = {
     'id_prestamo': 'RETOS2_001',
     'casado': 'No',
     'dependientes': 1,
     'educacion': 'Graduado',
     'independiente': 'Si',
     'ingreso_deudor': 4692,
     'ingreso_codeudor': 0,
     'cantidad_prestamo': 106,
     'plazo_prestamo': 360,
     'historia_credito': 1,
     'tipo_propiedad': 'Rural'
     }
print(prestamo(P_1))
P_2 = {
     'id_prestamo': 'RETOS2_002',
     'casado': 'No',
     'dependientes': '3+',
     'educacion': 'No Graduado',
     'independiente': 'No',
     'ingreso_deudor': 1830,
     'ingreso_codeudor': 0,
     'cantidad_prestamo': 100,
     'plazo_prestamo': 360,
     'historia_credito': 0,
     'tipo_propiedad': 'Urbano'
     }
print(prestamo(P_2))
P_3 = {
     'id_prestamo': 'RETOS2_003',
     'casado': 'No',
     'dependientes': '0',
     'educacion': 'No Graduado',
     'independiente': 'No',
     'ingreso_deudor': 3748,
     'ingreso_codeudor': 1668,
     'cantidad_prestamo': 110,
     'plazo_prestamo': 360,
     'historia_credito': 1,
     'tipo_propiedad': 'Semiurbano'
     }
print(prestamo(P_3))