from bussines import BusinessLayer
from Error import RepositoryError


class UI:
    def __init__(self, controller):
        self._controller = controller

    def Run():
        businessLayer = BusinessLayer()
        while True:
            userInput = input(">>")
            if (userInput == "exit"):
                return


            elif (userInput == "help"):
                print("1 : Add\n2 : remove\n3 : update\n4 : list\n5 : grade students at a given discipline")
            else:
                command_controller(userInput, businessLayer)

    def Add(businessLayer):
        UserInput = int(input("Type 1 in order to add a student or 2 for a discipline:"))
        if UserInput == "1":
            studentID = input("Please insert the ID of the student:")
            studentName = input("Please insert the name of the student:")
            businessLayer.AddStudentToRepo(studentID, studentName)
        elif UserInput == "2":
            disciplineID = input("Insert ID of the discipline:")
            disciplineName = input("Please insert the name of the discipline:")
            businessLayer.AddDisciplineToRepo(disciplineID, disciplineName)

    def Remove(businessLayer):
        print("Type 1 in order to remove a student or 2 for a discipline")
        UserInput = input()
        if UserInput == "1":
            print("Please type the student ID")
            studentID = input()
            businessLayer.RemoveS(studentID)
        elif UserInput == "2":
            print("Please type the discipline ID")
            disciplineID = input()
            businessLayer.RemoveD(disciplineID)

    def update_controller(businessLayer):
        print("Type 1 in order to update a student or 2 for a discipline")
        UserInput = input()
        if UserInput == "1":
            print("Please type the student ID")
            studentID = input()
            print("Please type the new name")
            name = input()
            businessLayer.UpdateS(studentID, name)
        elif UserInput == "2":
            print("Please type the discipline ID")
            disciplineID = input()
            print("Please type the new name")
            name = input()
            businessLayer.UpdateD(disciplineID, name)

    def list_controller(businessLayer):
        print("Type 1 in order to list all the student or 2 for discipline:")
        UserInput = input()
        if (UserInput == "1"):
            string = businessLayer.ListAllS()
            print(string)
        elif (UserInput == "2"):
            string = businessLayer.ListAllD()
            print(string)

    def grade_controller(businessLayer):
        print("Please type the studentID")
        studentID = input()
        print("Please type the disciplineID")
        disciplineID = input()
        print("Please type the grade value")
        gradeValue = input()
        try:
            int(gradeValue)
        except:
            raise ValueError("grade value should be int")

        businessLayer.GradeStudentAtD(studentID, disciplineID, gradeValue)

    def list_grade_controller(businessLayer):
        string = businessLayer.ListAllGrade()
        print(string)

    def command_controller(userInput, businessLayer):
        commands = {
            "1": add_controller,
            "2": remove_controller,
            "3": update_controller,
            "4": list_controller,
            "5": grade_controller,
            "list_grade": list_grade_controller
        }
        try:
            commands[userInput](businessLayer)
        except KeyError as keyError:
            if userInput != "":
                print("Invalid command")
        except RepositoryError as repositoryError:
            print(repositoryError)
        except ValueError as valueError:
            print(valueError)
