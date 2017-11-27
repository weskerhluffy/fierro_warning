'''
Created on 27/11/2017

@author: 

XXX:
'''

import logging
import sys
from fractions import gcd
from functools import reduce

nivel_log = logging.ERROR
#nivel_log = logging.DEBUG
logger_cagada = None

def fierro_warning_obten_diferencias(eventos):
    eventos_tam = len(eventos)
    if eventos_tam == 1:
        return []
    else:
        caca = []
        eventos_ord = sorted(eventos, reverse=False)
        logger_cagada.debug("eventos ord {}".format(eventos_ord))
        caca.append(eventos_ord[1] - eventos_ord[0])
        for idx in range(2, eventos_tam):
            caca.append(eventos_ord[idx] - eventos_ord[idx - 1])
        logger_cagada.debug("difs de mierda {}".format(caca))
        return sorted(caca)

def fierro_warning_obten_mcd_total(diferencias):
    diferencias_tam = len(diferencias)
    mcd_total = 0
    if(not diferencias_tam):
        return 0
    if(diferencias_tam == 1):
        return diferencias[0]
    
    mcd_total = reduce(gcd, diferencias[2:], gcd(diferencias[0], diferencias[1]))
    
    logger_cagada.debug("el mcd es {}".format(mcd_total))
    
    return mcd_total

def fierro_warning_calcula_mult_min_mcd(mcd_total, primer_evento):
    mult = primer_evento // mcd_total
    if (primer_evento % mcd_total):
        mult += 1
    
    return mult * mcd_total

def fierro_warning_core(eventos):
    eventos_tam = len(eventos)
    if(eventos_tam == 1):
        return 0
    
    diferencias = fierro_warning_obten_diferencias(eventos)
    
    mcd_total = fierro_warning_obten_mcd_total(diferencias)
    
    primer_evento = min(eventos)
    mult_min = fierro_warning_calcula_mult_min_mcd(mcd_total, primer_evento)
    
    logger_cagada.debug("la pote min de {} para alcanzar {} es {}".format(mcd_total, primer_evento, mult_min))
    
    return mult_min - primer_evento

def fierro_warning_main():
    linea = sys.stdin.readline()
    cacasos = int(linea.strip())
    
    for cacaso in range(cacasos):
        cacas = [int(x) for x in sys.stdin.readline().strip().split(" ")]
        eventos = cacas[1:]
        mierda = fierro_warning_core(eventos)
        logger_cagada.debug("la mierda es {}".format(mierda))
        print("Case #{}: {}".format(cacaso + 1, mierda))
        
if __name__ == '__main__':
        FORMAT = "[%(filename)s:%(lineno)s - %(funcName)20s() ] %(message)s"
        logging.basicConfig(level=nivel_log, format=FORMAT)
        logger_cagada = logging.getLogger("asa")
        logger_cagada.setLevel(nivel_log)

        fierro_warning_main()
