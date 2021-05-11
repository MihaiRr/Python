'''
Created on Dec 12, 2019

@author: reteg
'''
from Controller import *
class UI():
    def __init__(self, controller):
        self.__controller=controller
    
    def createListPassengers(self):
        num=int(input("input numbers of passengers"))
        list=[]
        for i in range(0,num):
            l=[]
            firstName=input("\t input first name:")
            l.append(firstName)
            lastName=input("\t input last name:")
            l.append(lastName)
            passportNum=input("\t input passport number:")
            l.append(passportNum)
            list.append(l)
            print("\n")
        return list   
    
    def addPlaneUI(self):
        num=input("input plane name/number:")
        company=input("input airline company:")
        numSeats=input("input number of seats:")
        destination=input("input destination:")
        list=self.createListPassengers()
        self.__controller.addPlaneC(num,company,numSeats,destination,list)
    
    def getAllUI(self):
        self.__controller.getAllC()
        
    def updateAllPlaneUI(self):
        num=input("input plane name/number to update:")
        company=input("input airline company:")
        numSeats=input("input number of seats:")
        destination=input("input destination:")
        print("input new Passenger:")
        list=self.createListPassengers()
        self.__controller.updatePlaneC(num,company,numSeats,destination,list)
    
    def updatePassengerListUI(self):
        num=input("input plane name/number to update:")
        print("input new Passenger:")
        list=self.createListPassengers()
        self.__controller.updatePassengerList(num, list)
    
    def updatePassengerUI(self):
        num=input("input plane name/number to update:")
        index=input("input index:")
        fname=input("input first name:")
        lname=input("input last name:")
        numberpass=input("input number passport:")
        list=[fname,lname,numberpass]
        self.__controller.updatePassenger(num, index ,list)
        
    def deletePassengerUI(self):
        plane=int(input("input plane index:"))
        index=int(input("input passenger index:"))
        self.__controller.deletePassengerC(plane,index)
        
    def deletePlaneUI(self): 
        plane=int(input("input plane index:"))
        self.__controller.deletePlaneC(plane)
    
    def sortPassengersByLastNameUI(self):
        index=input("input index of plane you want to sort:")
        self.__controller.sortPassengerByLastNameC(index)
        
    def sortPlanesByNrPassengerUI(self):
        self.__controller.sortPlanesByNrPassengerC()
        
    def sortPlanesByNrPassengerStartWithStringUI(self):
        str=input("input string:")
        self.__controller.sortPlanesByNrPassengerStartWithStringC(str)
            
    def sortPlanesByConcatUI(self):
        self.__controller.sortPlanesByConcatC() 
        
    def getPlanesStartPassWithSame3UI(self):
        self.__controller.getPlanesStartPassWithSame3C()
        
    def getPassengerWithStringinFirstorLastNameUI(self):
        index=input("input index of plane:")
        str=input("input string:")
        self.__controller.getPassengerWithStringinFirstorLastNameC(index,str)   
        
    def getPlaneWithPassengerWithGivenNameUI(self):
        fname=input("input first name:")
        lname=input("input last name:")
        self.__controller.getPlaneWithPassengerWithGivenNameC(fname,lname)    
        
    def Recursion1UI(self):
        index=int(input("input plane index:"))
        k=int(input("input k:"))
        self.__controller.Recursion1C(index,k)
        
    def Recursion2UI(self):
        k=int(input("input k:"))
        self.__controller.Recursion2C(k)    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        