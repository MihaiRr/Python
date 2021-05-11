class Passenger():
    def __init__(self, firstName, lastName, passportNumber):
        self.__firstName=firstName
        self.__lastName=lastName
        self.__passNum=passportNumber
    
    def getFirstName(self):
        return self.__firstName
    def setFirstName(self, newFName):
        self.__firstName=newFName
        
    def getLastName(self):
        return self.__lastName
    def setLastName(self, newLName):
        self.__lastName=newLName
        
    def getPassport(self):
        return self.__passNum
    def setPassport(self,newPNum):
        self.__passNum=newPNum
        
    def __str__(self):
        s=self.__firstName+ " " + self.__lastName + " " + self.__passNum
        return s  
    