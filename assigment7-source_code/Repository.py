from Error import RepositoryError


class Repository:
    def __init__(self):
        self.__listOfElements = []

    def Add(self, newElement):
        """
        append newElement, if the element exists raise a RepositoryError
        :param newElement:
        """
        for element in self.__listOfElements:
            if (element == newElement):
                raise RepositoryError("Existing element")

        self.__listOfElements.append(newElement)

    def Update(self, oldElement, newElement):
        """
        replace oldElement with newElement
        :param oldElement:
        :param newElement:
        :return:
        """
        position = self.FindPositonOfElement(oldElement)
        self.__listOfElements[position] = newElement

    def Remove(self, element):
        """
        remove element from the list
        :param element:
        """
        position = self.FindPositonOfElement(element)
        del self.__listOfElements[position]

    def FindElement(self, element):
        """
        find and return an element, if the element doesn't exist raise a RepositoryError
        :param element:
        :return: element if it is found
        """
        for eachElement in self.__listOfElements:
            if eachElement == element:
                return eachElement
        raise RepositoryError("Inexisting Element")

    def FindElementById(self, id):
        """
        find an element and return the id, if the element doesn't exist raise a RepositoryError
        :param element:
        :return: element if it is found
        """
        for element in self.__listOfElements:
            if element.get_studentID() == id:
                return element
        raise RepositoryError("Inexisting Element")

    def FindPositonOfElement(self, element):
        """
        find the position of an element in the list, if if the element doesn't exist raise a RepositoryError
        :param element:
        :return: the position of the element
        """
        for i in range(len(self.__listOfElements)):
            existingElement = self.__listOfElements[i]
            if (existingElement == element):
                return i
        raise RepositoryError("Inexisting Element")

    def GetLen(self):
        """
        :return: the len of the list
        """
        return len(self.__listOfElements)

    def GetAllElements(self):
        """
        :return: all the element as a list
        """
        return self.__listOfElements
