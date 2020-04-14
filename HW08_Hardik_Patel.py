from datetime import datetime, timedelta
from typing import Tuple,List,Dict,Iterator
import os
from prettytable import PrettyTable


def date_arithmetic()-> Tuple[datetime, datetime, int]:
    """ his function is used to find specific dates"""
    three_days_after_02272000:datetime = datetime.strptime("Feb 27, 2020","%b %d, %Y")+timedelta(days=3)
    #three_days_after_02272000:str=three_days_after_02272000.strftime('%b %d, %Y')
    three_days_after_02272017:datetime = datetime.strptime("Feb 27, 2019","%b %d, %Y")+timedelta(days=3)
    #three_days_after_02272017:str=three_days_after_02272017.strftime('%b %d, %Y')
    days_passed_01012017_10312017:int = int((datetime.strptime("Sep 30, 2019","%b %d, %Y") -
                                             datetime.strptime("Feb 01, 2019","%b %d, %Y")).days)
    return three_days_after_02272000, three_days_after_02272017, days_passed_01012017_10312017



def file_reader(path, fields, sep=',', header=False) -> Iterator[List[str]]:
    """This function is used to read the split and read the file according to the  specified variable sep."""
    try:
        a=open(path,"r")
        c:int=0
        c1:int=0
        """Counting number of lines in the original file"""
        for i in a:
            c=c+1
            if header==True and c==1:
                new_List:List=i.rstrip('\n').split(sep)
                if len(new_List)!=fields:
                    raise ValueError(f"Value Error:'{a.name}' has {len(new_List)} fields on line 1 but expected {fields}.")
                continue

        a.close()
        a = open(path, "r")
        for j in range(c):
            fl:bool=True
            c1=c1+1
            if header==True and c1==1:
                fl=False

            line=next(a)
            if fl==False:
                fl=True
                continue
            line=line.rstrip('\n')
            l1:List=[]
            b:Tuple=tuple(line.split(sep))
            if len(b)==fields:
                l1.append(b)
                yield(b)
            else:
                raise ValueError(f"Value Error:'{a.name}' has {len(b)} fields on line {c1} but expected {fields}.")
        a.close()
    except FileNotFoundError:
        raise


class FileAnalyzer:
    """ This class is use to show the prettytable and analyze the file."""
    def __init__(self, directory):
        """ It's is the constructor of the class."""
        self.directory:str = directory
        self.files_summary:Dict[str, Dict[str, int]] = dict()

        self.analyze_files()

    def analyze_files(self)-> None:
        """This function is used to find and analyze the files."""
        if os.path.exists(self.directory):
            for filename in os.listdir(self.directory):
                if filename.endswith('.py'):
                    try:
                        filename1=os.path.join(self.directory,filename)
                        open_file=open(filename1)
                        #print("1aa11")
                        num_char:int=len(open_file.read())
                        #print(open_file)
                        set_for_def:set=set()
                        ctr1:int=0
                        ctr2:int=0
                        ctr3:int=0
                        open_file.close()
                        open_file = open(filename1)
                        for line in open_file:
                            ctr3=ctr3+1
                            line=line.strip()
                            if line.startswith("class "):
                                ctr1=ctr1+1
                            if line.startswith("def "):
                                ctr2=ctr2+1
                                #set_for_def.add(line)
                            #if line.startswith("main()"):
                            #    set_for_def.add(line)
                        #print(set_for_def)
                        #self.l1.append((filename1,ctr1,len(set_for_def),ctr3,num_char))
                        self.files_summary[filename]={"class":ctr1,
                                                      "function":ctr2,
                                                      "line":ctr3,
                                                      "char":num_char}
                        #return self.directory
                    except FileNotFoundError:
                        raise
                    #print(filename)

            #print(self.files_summary)
            return self.files_summary
            #print(self.l1)
        else:
            raise FileNotFoundError

    def pretty_print(self)-> None:
        """This function is used to represent the analyzed files in form of pretty table."""
        p1:PrettyTable=PrettyTable(field_names=['File name','Classes','Functions','Lines','Characters'])
        for fname in self.files_summary.items():
            a:str=fname[0]
            b:int=fname[1]["class"]
            c:int=fname[1]["function"]
            d:int=fname[1]["line"]
            e:int=fname[1]["char"]
            p1.add_row([a,b,c,d,e])
        #print(p1)


#print(list(file_reader("students.txt",3,sep=";", header=True)))
#file_analyzer:FileAnalyzer = FileAnalyzer(r"C:\Users\Hardik\Downloads\SSW 810\Assign 7")
#file_analyzer.pretty_print()
#print(file_analyzer.analyze_files())

#print(list(file_reader("abc.txt", 3, "|", header=True)))