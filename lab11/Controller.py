'''
Created on Dec 12, 2019

@author: reteg
'''

class Controller():
    def __init__(self, repo):
        self.__repo=repo
        
    def addPlaneC(self, num,company, numSeats,destination,list):
        self.__repo.addPlane(num,company, numSeats,destination,list)
                
    def getAllC(self):
        self.__repo.getAll()    
    
    def updatePlaneC(self,num,company, numSeats,destination,list):
        self.__repo.updatePlane(num,company, numSeats,destination,list)
        
    def updatePassengerList(self,num,list):
        self.__repo.updatePassengerList(num,list)
        
    def updatePassenger(self,num,index,list):
        self.__repo.updatePassenger(num, index ,list)
    
    def deletePassengerC(self,plane,index):
        self.__repo.deletePassengerRepo(plane,index)
        
    def deletePlaneC(self,plane):
        self.__repo.deletePlane(plane)
    
    def sortPassengerByLastNameC(self,index):
        self.__repo.sortPassengerByLastNameR(index)
        
    def sortPlanesByNrPassengerC(self):  
        self.__repo.sortPlaneByNrPassengerR()
    
    def sortPlanesByConcatC(self):
        self.__repo.sortPlanesByConcat()
        
    def sortPlanesByNrPassengerStartWithStringC(self,str):
        self.__repo.sortPlanesByNrPassengerStartWithString(str)
    
    def getPlanesStartPassWithSame3C(self):
        l=self.__repo.getPlanesStartPassWithSame3()
        for i in range(0,len(l)):
            print(l[i])
            
    def getPassengerWithStringinFirstorLastNameC(self, index,str):
        l=self.__repo.getPassengerWithStringinFirstorLastName(index,str)
        for i in range(0,len(l)):
            print(l[i])
            
    def getPlaneWithPassengerWithGivenNameC(self,fname,lname):
        l=self.__repo.getPlaneWithPassengerWithGivenName(fname,lname)
        for i in range(0,len(l)):
            print(l[i])
            
    def Recursion1C(self,index,k):
        self.__repo.Recursion1R(index,k)
        
    def Recursion2C(self,k):
        self.__repo.Recursion2R(k)