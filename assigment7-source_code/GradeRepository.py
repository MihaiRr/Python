from Error import RepositoryError


class GradeRepository(object):
    def __init__(self):
        self.__listOfElements = []

    def remove_all_student(self, studentID):
        """
        remove all the grades from the list with studentID = studentID
        :param studentID:
        """
        i = self.find_position_of_element(studentID)
        while(i != -1):
            del self.__listOfElements[i]
            i = self.find_position_of_element(studentID)

    def remove_all_discipline(self, disciplineID):
        """
        remove all the grades from the list with disciplineID = disciplineID
        :param disciplineID:
        """
        i = self.find_position_of_element(disciplineID)
        while (i != -1):
            del self.__listOfElements[i]
            i = self.find_position_of_element(disciplineID)

    def find_position_of_element(self, id):
        """
        find and return the position of an element, if it doesn't exist return -1
        :param id:
        :return: position or -1
        """
        for i in range(self.get_len()):
            grade = self.__listOfElements[i]
            if grade.get_disciplineID() == id or grade.get_studentID() == id:
                return i
        return -1

    def add(self, newGrade):
        """
        add a new grade to the list
        :param newGrade:
        """
        self.__listOfElements.append(newGrade)

    def get_all_elements(self):
        """
        :return: all elements as a list
        """
        return self.__listOfElements

    def get_len(self):
        """
        :return: the len of the list
        """
        return len(self.__listOfElements)