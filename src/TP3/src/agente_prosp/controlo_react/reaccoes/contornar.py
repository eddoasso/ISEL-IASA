from lib.ecr.reaccao import Reaccao
from lib.ecr.resposta import Resposta

from psa.accao import Mover
from psa.actuador import ESQ, DIR, FRT


class Contornar(Reaccao):
    def detectar_estimulo(self,percepcao):
        return (percepcao[ESQ].contacto and percepcao[ESQ].obstaculo) or (percepcao[DIR].contacto and percepcao[DIR].obstaculo)
    
    def gerar_resposta(self,estimulo):
        return Resposta(Mover(FRT))
