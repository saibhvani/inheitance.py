# single level inheritances
class Address:
    __address:str = ""
    def sumAddress(self,address):
        self.__address = address
    def getAddress(self):
        return self.__address
class Employee(Address):
    __firstName:str =""
    __lastName:str = ""
    __surname:str = ""
    def setname(self,fname:str,lname:str,sname:str):
        self.__firstName = fname
        self.__lastName = lname
        self.__surname = sname
    def __nameformat(self):
        return f'{self.__firstName} {self.__surname} {self.__lastName} '
    def getfullName(self):
        return self.__nameformat()
emp = Employee()
emp.setname(fname="Saibhavani",sname="M",lname="Motamarri")
emp.sumAddress("khammam")
print(emp.getfullName())
print(emp.getAddress())


# abstraction with functions

class Employee:
    __firstName:str = "sai bhavani"
    __lastName:str = "Motamarri"
    def fullname(self):
        return self.__nameformat(self.__firstName,self.__lastName)
    def __nameformat(self,fname:str,lname:str):
        return f'{fname,lname}'
emp = Employee()
emp.__firstName = "ABC"
print(emp.fullname())
print(emp.__nameformat("saibhavani","Motamarri"))

