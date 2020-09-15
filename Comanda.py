
class Comanda:

    def __init__(self,nume, adresa, tipDePizza):
        self.__nume=nume
        self.__adresa=adresa
        self.__tipDePizza=tipDePizza

    def getNume(self):
        return self.__nume

    def getAdresa(self):
        return self.__adresa

    def getTipDePizza(self):
        return self.__tipDePizza

    def __str__(self):
        return '{0} cu adresa: {1} a comandat o pizza : {2}'.format(self.getNume(),self.getAdresa(),self.getTipDePizza())

