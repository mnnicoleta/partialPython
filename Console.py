from Comanda import Comanda

class UI:

    def __init__(self,controller):
        self.__controller=controller


    def __showOptions(self):
        print ('Bine ati venit la aplicatia Pizza ! :) ')
        print("0. Arata toate comenzile")
        print('1. Adauga comanda')
        print("2. Arata persoana cu cele mai multe comenzi")
        print('3. Ordoneaza descrescator adresele dupa nr de vocale continute')
        print("x. Exit")


    def __showAllComenzi(self):
        try:
            all = self.__controller.getAllComenzi()
            print('Comenzile inregistrate sunt: ')
            for comanda in all:
                print(comanda)
        except ValueError as ve:
            print(ve)


    def __adaugaComanda(self):


        nume=input('Dati numele persoanei: ')
        adresa=input('Dati adresa persoanei: ')

        listaPizza=[]
        tipDePizza=input('Dati felul pizzei dorite, -1 pentru iesire din meniu: ')
        listaPizza.append(tipDePizza)

        var='-1'
        while tipDePizza != var:
            tipDePizza = input('Dati felul pizzei dorite, -1 pentru iesire din meniu: ')
            if tipDePizza not in listaPizza:
                listaPizza.append(tipDePizza)

        listaPizza.pop(-1)

        for pizza in listaPizza:
            self.__controller.adaugaComanda(nume,adresa,pizza)




    def __showPersoanaMaximNrComenzi(self):
        try:
            a=self.__controller.persCuNrMaximDePizzaComandate()
            print(a)
        except ValueError as ve:
            print(ve)


    def __sortedListWithAddresses(self):
        try:
            a = self.__controller.adreseOrdonateDupaNrVocale()
            print(a)
        except ValueError as ve:
            print(ve)


    def showUI(self):
        while True:
            self.__showOptions()
            option = input("Alege o optiune: ")
            if option == "0":
                self.__showAllComenzi()
            elif option == "1":
                self.__adaugaComanda()
            elif option == "2":
                self.__showPersoanaMaximNrComenzi()
            elif option =='3':
                self.__sortedListWithAddresses()
            elif option == "x":
                break
            else:
                print("Optiune invalida!")
            print()


