from Comanda import Comanda

class Controller:

    def __init__(self):
        self.__comenzi=[]


    def getAllComenzi(self):
        '''
        returneaza o lista cu toate comenzile
        :return:
        '''
        if len(self.__comenzi)==0:
            raise ValueError('Nu exista nicio comanda in baza de date! Va rugam introduceti o comanda.')
        else:
            return self.__comenzi


    def adaugaComanda(self,nume,adresa,tipDePizza):
        '''
        adauga o comanda in lista
        :param nume:
        :param adresa:
        :param tipDePizza:
        :return:
        '''
        allComenzi=self.__comenzi

        allComenzi.append(Comanda(nume,adresa,tipDePizza))


    def persCuNrMaximDePizzaComandate(self):
        '''
        returneaza ca string numele persoanei cu nr maxim de comenzi
        :return:
        '''
        if len(self.__comenzi) == 0:
            raise ValueError('Nu exista nicio comanda in baza de date! Va rugam introduceti o comanda.')


        allComenzi=self.__comenzi

        listWithAllNames=[]

        for persoana in allComenzi:
            listWithAllNames.append(persoana.getNume())

        numePersoana=[None]
        nrMaxDeAparitiiNume=0
        for nume in listWithAllNames:
            if listWithAllNames.count(nume)>nrMaxDeAparitiiNume:
                nrMaxDeAparitiiNume=listWithAllNames.count(nume)
                numePersoana[0]=nume

        return numePersoana

    def adreseOrdonateDupaNrVocale(self):
        '''
        returneaza o lista cu adresele ordonate descrescator in functie de nr de vocale continute
        :return:
        '''
        allComenzi=self.__comenzi

        listaAdreseOrdonate = []


        listaAdrese=[]
        for adresa in allComenzi:
            listaAdrese.append(adresa.getAdresa())

        maximNrVocale=0
        for adresa in listaAdrese:
            if self.getNrOfVowelsInString(adresa)>maximNrVocale:
                maximNrVocale=self.getNrOfVowelsInString(adresa)

        while maximNrVocale!=0:
            for adresa in listaAdrese:
                if maximNrVocale==self.getNrOfVowelsInString(adresa):
                    if adresa not in listaAdreseOrdonate:
                        listaAdreseOrdonate.append(adresa)
            maximNrVocale -=1



        return listaAdreseOrdonate




    def getNrOfVowelsInString(self,adresa):
        '''
        returneaza nr de vocale continute de un string
        :param adresa:
        :return:
        '''

        count=0
        for a in adresa:
            count +=1

        for e in adresa:
            count +=1

        for i in adresa:
            count +=1

        for o in adresa:
            count +=1

        for u in adresa:
            count +=1

        return count



def test_Controller():
    t=Controller()

    t.adaugaComanda('Nico','Bucuresti','Formagio')
    t.adaugaComanda('Nico', 'Cluj', 'Stagioni')

    all=t.getAllComenzi()
    assert len(all)==2

    assert t.adreseOrdonateDupaNrVocale()==['Bucuresti','Cluj']
    assert t.persCuNrMaximDePizzaComandate()==['Nico']



test_Controller()

