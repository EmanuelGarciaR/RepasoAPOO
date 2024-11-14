# TODO: Implementa el código del ejercicio aquí
from abc import ABC, abstractmethod

from validadorclave.modelo.errores import NoCumpleLongitudMinimaError, NoTieneLetraMayusculaError, \
    NoTieneLetraMinusculaError, NoTieneNumeroError, NoTieneCaracterEspecialError, NoTienePalabraSecretaError


class ReglaValidacion(ABC):
    def __init__(self, longitud_esperada: int):
        self._longitud_esperada: int = longitud_esperada

    @abstractmethod
    def es_valida(self, clave):
        pass

    def _validar_longitud(self, clave: str) ->bool:
        return len(clave) > self._longitud_esperada

    def _contiene_mayuscula(self, clave: str) -> bool:
        for letter in clave:
            if letter.isupper():
                return True
        return False

    def _contiene_minuscula(self, clave: str) -> bool:
        for letter in clave:
            if letter.islower():
                return True
        return False

    def _contiene_numero(self, clave: str) -> bool:
        for letter in clave:
            if letter.isdigit():
                return True
        return False

class ReglaValidacionGanimedes(ReglaValidacion):
    def __init__(self, longitud_esperada = 8):
        super().__init__(longitud_esperada)

    def contiene_caracter_especial(self, clave: str) -> bool:
        especial_match = '@_#$%'
        for letter in especial_match:
            if letter in clave :
                return True
        return False

    def es_valida(self, clave: str):
        if not self._validar_longitud(clave):
            raise NoCumpleLongitudMinimaError()
        if not self._contiene_mayuscula(clave):
            raise NoTieneLetraMayusculaError()
        if not self._contiene_minuscula(clave):
            raise NoTieneLetraMinusculaError()
        if not self._contiene_numero(clave):
            raise NoTieneNumeroError()
        if not self.contiene_caracter_especial(clave):
            raise NoTieneCaracterEspecialError()
        return True

class ReglaValidacionCalisto(ReglaValidacion):
    def __init__(self, longitud_esperada=6):
        super().__init__(longitud_esperada)

    def contiene_calisto(self, clave: str):
        if 'calisto' in clave.lower():
            counter = 0
            for letter in clave:
                if letter in "CALISTO":
                    counter += 1
            if 2 <= counter < 7:
                return True
        return False

    def es_valida(self, clave: str):
        if not self._validar_longitud(clave):
            raise NoCumpleLongitudMinimaError()
        if not self._contiene_numero(clave):
            raise NoTieneNumeroError()
        if not self.contiene_calisto(clave):
            raise NoTienePalabraSecretaError()
        return True

class Validador:
    def __init__(self, regla: ReglaValidacion):
        self.regla: ReglaValidacion = regla

    def es_valida(self, clave: str) -> bool:
        return self.regla.es_valida(clave)