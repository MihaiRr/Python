'''
Created on Jan 5, 2020

@author: reteg
'''
from UI import *
from Controller import * 
from Repository import *
from Plane import *
from Passenger import *
from Menu import Menu

def Run():
    repo=Repository()
    p1=["Alex","c","1234"]
    p2=["Alex11","A1","1231"]
    p3=["Alex12","b","1111"]
    p4=["Alex23","a","1114"]
    l=[p1,p2]
    l1=[p2,p3,p4,p1]
    l2=[p3,p4,p1]
    repo.addPlane("5","c3","3","d1",l)
    repo.addPlane("1","b2","4","d2",l1)
    repo.addPlane("3","a1","5","d3",l2)
    
    controller=Controller(repo)
    ui=UI(controller)
    menu=Menu(ui)
    menu.Menu()
    
Run()
    
    
    