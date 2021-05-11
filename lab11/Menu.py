'''
Created on Jan 5, 2020

@author: reteg
'''

class Menu():
    def __init__(self, userInterface):
        self.__ui=userInterface
        
    def printMenu(self):
        print("0.Print menu")
        print("1.Add plane")
        print("2.Get all planes")
        print("3.Update full plane")
        print("4.Update list of a plane")
        print("5.Update a passenger of a plane")
        print("6.Delete a passenger on a specific plane")
        print("7.Delete a plane")
        print("8.Sort the passenger by last name")
        print("9.Sort planes according to the number of passengers ")
        print("10.Sort planes according to the number of passengers with the first name starting with a str ")
        print("11.Sort planes by concatenation of the number of passengers in the plane and the destination")
        print("12.Identify planes that have passengers with passport numbers starting with the same 3 letters  ")
        print("13.Identify passengers from a given plane for which the first name or last name contain a string given as parameter ")
        print("14.Identify plane/planes where there is a passenger with given name")
        print("15.Recursion 1")
        print("16.Recursion 2")
    def getCommand(self):
        command=input(">>>")
        if command=="1":
            self.__ui.addPlaneUI()
        elif command=="2":
            self.__ui.getAllUI()
        elif command=="3":
            self.__ui.updateAllPlaneUI()
        elif command=="4":
            self.__ui.updatePassengerListUI()
        elif command=="5":
            self.__ui.updatePassengerUI()
        elif command=="6":
            self.__ui.deletePassengerUI()
        elif command=="7":
            self.__ui.deletePlaneUI()
        elif command=="0":
            self.printMenu()
        elif command=="8":
            self.__ui.sortPassengersByLastNameUI()
        elif command=="9":
            self.__ui.sortPlanesByNrPassengerUI()
        elif command=="10":
            self.__ui.sortPlanesByNrPassengerStartWithStringUI()       
        elif command=="11":
            self.__ui.sortPlanesByConcatUI()
        elif command=="12":
            self.__ui.getPlanesStartPassWithSame3UI()
        elif command=="13":
            self.__ui.getPassengerWithStringinFirstorLastNameUI()
        elif command=="14":
            self.__ui.getPlaneWithPassengerWithGivenNameUI()
        elif command=="15":
            self.__ui.Recursion1UI()
        elif command=="16":
            self.__ui.Recursion2UI()
        else:
            pass    
    
    def Menu(self):
        self.printMenu()
        while True:
            self.getCommand()
            
            
            
            
            
            
            
  
            