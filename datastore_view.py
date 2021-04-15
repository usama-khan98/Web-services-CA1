import ZODB, ZODB.FileStorage
import persistent
import transaction



class Student(persistent.Persistent):
    studentName = ''
    def setStudentName(self, sName):
        self.studentName = sName
    def getStudentName(self):
        return self.studentName
        


storage = ZODB.FileStorage.FileStorage('mydata.fs')
db = ZODB.DB(storage)
connection = db.open()
root = connection.root

        

# In this example, we are just pulling the record from the database and viewing the name
# that was stored inside of the s1 object.


print(root.s1.getStudentName())


