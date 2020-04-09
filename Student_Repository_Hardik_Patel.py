from typing import List,Dict,Tuple,DefaultDict
from HW08_Hardik_Patel import file_reader
from prettytable import PrettyTable
from _collections import defaultdict
import os

class Student:
    """Contains information about every student"""
    def __init__(self,cwid:str,name:str,major:str):
        self._cwid:str=cwid
        self._name:str=name
        self._major:str=major
        self._course:Dict[str,str]=dict()                #key=coursename and values=grade

    def comp_courses(self,course:str,grade:str):
        """Use to get completed courses in form of list as keys for this assignment"""
        self._course[course]:Dict[str, str]=grade

    def result_return_student(self):
        """Use to return the final value of the class student
         and this value is used and printed in pretty table of student summary"""
        return [self._cwid, self._name,sorted(self._course.keys())]

class Instructor:
    """Contains every information about instructor"""
    def __init__(self,cwid:str,name:str,dept:str):
        self._cwid:str=cwid
        self._name:str=name
        self._dept:str=dept
        self._courses:DefaultDict[str,int]=defaultdict(int)         #key=coursename and values=count of students(int)

    def add_num_of_students(self,course:str):
        """This function is use to keep the count of number of students taken courses of a particular instructor"""
        self._courses[course]+=1

    def result_return_instructor(self):
        """Use to return the final value of the class instructor
         and this value is used and printed in pretty table of instructor summary"""
        for course, count in self._courses.items():
            yield [self._cwid,self._name,self._dept,course,count]


class Repository:
    """Contain every information"""
    def __init__(self,path:str):
        self._path:str=path
        self._students:Dict[str,Student]=dict()                 #keys=cwid and values=Instance of Class Student
        self._instructors:Dict[str,Instructor]=dict()           #keys=cwid and values=Instance of Class Instructor
        #path1:str=os.path.join(self._path, "students.txt")
        #self.path:str=os.path.join(self._path, "instructors.txt")
        #path1:str=os.path.join(self._path, "grades.txt")
        self.check_student_data()
        self.check_instructor_data()
        self.check_grades_data()
        self.printpretty_1()
        self.printpretty_2()

    def check_student_data(self):
        """This function read the students.txt file and fill values in self._students"""
        path1:str=os.path.join(self._path, "students.txt")
        try:
            open_file1=file_reader(path1,fields=3,sep="\t")
            for cwid,name,major in open_file1:
                self._students[cwid]=Student(cwid,name,major)
        except ValueError as e:
            print(e)
        except FileNotFoundError as fe:
            print(fe)

    def check_instructor_data(self):
        """This function read the instructors.txt file and fill values in self._instructors"""
        path2:str=os.path.join(self._path,"instructors.txt")
        try:
            open_file2=file_reader(path2,fields=3,sep="\t")
            for cwid,name,dept in open_file2:
                self._instructors[cwid]=Instructor(cwid,name,dept)
        except ValueError as e:
            print(e)
        except FileNotFoundError as fe:
            print(fe)

    def check_grades_data(self):
        """This function read the grades.txt file and fill values in both self._students and self._instructors"""
        path3:str=os.path.join(self._path,"grades.txt")
        try:
            open_file3=file_reader(path3,fields=4,sep="\t")
            for cwid_stud,course,grade,cwid_inst in open_file3:
                if cwid_stud in self._students:
                    self._students[cwid_stud].comp_courses(course,grade)
                else:
                    print("Invalid Student")
                if cwid_inst in self._instructors:
                    self._instructors[cwid_inst].add_num_of_students(course)
                else:
                    print("Invalid Instructor")
        except ValueError as e:
            print(e)
        except FileNotFoundError as fe:
            print(fe)

    def printpretty_1(self):
        """This function is use to print the prettytable of students summary"""
        print("Student Summary")
        testvar_1:Dict=dict()
        p1:PrettyTable=PrettyTable(field_names=["CWID","Name","Completed Courses"])
        #print(self._students.values())
        for a in self._students.values():
            testvar_1[a.result_return_student()[0]]=tuple(a.result_return_student()[1:])
            #print(a.result_return_student())
            p1.add_row(a.result_return_student())

        print(p1)
        return testvar_1

    def printpretty_2(self):
        """This function is use to print the pretty table of instructors summary"""
        print("Instructor Summary")
        testvar_2:Dict=dict()
        p2:PrettyTable=PrettyTable(field_names=["CWID","Name","Dept","Course","Students"])
        #print(self._instructors)
        for i in self._instructors.values():
            for j in i.result_return_instructor():
                testvar_2[j[0]]=tuple(j[1:])
                p2.add_row(j)

        print(p2)
        return testvar_2



def main():
    Repository(r"C:\Users\Hardik\Downloads\SSW 810\Assign 9")

if __name__ == '__main__':
    main()
