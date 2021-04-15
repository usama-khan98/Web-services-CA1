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

        
# saving the data


root.s1 = Student()

# set the data into the node
root.s1.setStudentName("james")

# save the changes!
transaction.commit()






