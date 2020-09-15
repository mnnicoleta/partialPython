from Console import UI
from Controller import Controller

def main():
    service = Controller()
    console = UI(service)


    console.showUI()

main()