from Recursion import *
class Plane():
    def __init__(self, number, company,numberSeats, Destination, listOfPassengers):
        self.__number=number
        self.__company=company
        self.__numberSeats=numberSeats
        self.__destination=Destination
        self.__listOfPassenger=listOfPassengers
        
    def getNumber(self):
        return self.__number
    def setNumber(self,newNumber):
        self.__number=newNumber
        
    def getCompany(self):
        return self.__company
    def setCompany(self,newCompany):
        self.__company=newCompany
        
    def getNumberSeats(self):
        return self.__numberSeats
    def setNumberSeats(self, newNumberSeats):
        self.__numberSeats=newNumberSeats
        
    def getDestination(self):
        return self.__destination
    def setDestination(self, newDestination):
        self.__destination=newDestination
    
    def getLenList(self):
        return len(self.__listOfPassenger)
    def getList(self):
        return self.__listOfPassenger
    
    def setList(self, newList):
        self.__listOfPassenger=newList        
    
    def updateToList(self, index, p):
        if int(index)>len(self.__listOfPassenger):
            raise ValueError
        else:
            self.__listOfPassenger[int(index)]=p
    
    def deletePassenger(self,index):
        if index>len(self.__listOfPassenger):
            raise ValueError
        else:
            del self.__listOfPassenger[index]
    
    def sortPassengerByLastName(self):
        for i in range(0,len(self.__listOfPassenger)-1):
            for j in range(i+1,len(self.__listOfPassenger)):
                if self.__listOfPassenger[i].getLastName()>self.__listOfPassenger[j].getLastName():
                    self.__listOfPassenger[i], self.__listOfPassenger[j]=self.__listOfPassenger[j], self.__listOfPassenger[i]
     
    
    def Recursion1(self,k):
        printCombination(self.__listOfPassenger, len(self.__listOfPassenger), k)
    
    def __str__(self):
        s= self.__number+ " " + self.__company + " "+ self.__numberSeats + " " + self.__destination + "\n"
        for i in range(0,len(self.__listOfPassenger)):
            s+="\t" + self.__listOfPassenger[i].getFirstName() + " " + self.__listOfPassenger[i].getLastName() + " " + self.__listOfPassenger[i].getPassport() + "\n"
        return s
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
   
   
    