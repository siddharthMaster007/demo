from csv import reader,DictReader
import os.path as path

class Reader:
    def __init__(self,file_nm):
        self.file_nm = file_nm
        self.file = None
        self.header = ['USER_NAME','CONTACT','DEPARTMENT','DOB','LAST_NAME','FIRST_NAME']
        self.invalid_header = ''

    def file_exist(self):
        if path.exists(self.file_nm):
            return True
        else :
            return False

    def check_header(self,delmter):
        with open(self.file_nm) as fr:
            read = reader(fr,delimiter=delmter)
            columns = read.__next__()
            status = True
            for column in columns:
                if column not in self.header:
                    self.invalid_header += column + ', '
                    status = False
            return status         
   
    def read(self,delimiter_char):
        self.file = open(self.file_nm)
        read = DictReader(self.file,delimiter=delimiter_char)    
        #check header is valid or not     
        if self.check_header(delimiter_char):
            return read 
        else :            
            raise ValueError('Header information Incorrect : ' + self.invalid_header)

    def file_close(self):
        self.file.close()


class CsvReader(Reader):
    def __init__(self,file_name):
        super().__init__(file_name)
       
    def read(self):
        return super().read(',')


class TsvReader(Reader):
    def __init__(self,file_name):
        super().__init__(file_name)

    def read(self):
        return super().read('\t')
































 # if delimiter_char is None:
        #     print("csv")
        #     read = csv.DictReader(self.file)
        # else:
        #     print("tsv")



    # def read(self):
    #     self.file = open(self.file_nm)
    #     read = csv.DictReader(self.file,delimiter='\t')        
    #     if self.check_header('\t'):
    #         return read 
    #     else :            
    #         header = ','.join(map("{}".format,self.filed))
    #         raise ValueError('Header information Incorrect : ' + header)
   

















































# class CsvReader:

#     def __init__(self):
#         self.header = ['USER_NAME','CONTACT','DEPARTMENT','DOB','LAST_NAME','FIRST_NAME']
#         self.column = list()

#     def is_valid_file(self,file_name):
#         if path.exists(file_name):
#             return True
#         else:
#             print("file not exist")
 
#     def read(self,file_name):
#         fe = path.splitext(file_name)[1]
#         if fe == '.csv':
#             return self.read_csv(file_name)        
#         if fe == '.txt':
#             return self.read_txt(file_name)

    
#     def read_csv(self,file_name):
#         fr = open(file_name)
#         read = csv.DictReader(fr)
#         #filed = list(read.__next__().keys())
        
#         if self.check_header(file_name):
#             return read 
#         else :
#             print("Header Information Incorrect : "+','.join(map("{}".format,self.column)))     
    

#     def check_header(self,file_name):
#         with open(file_name) as fr_check:
#             read = csv.reader(fr_check)
#             filed = read.__next__()
#         status = True
#         for col in filed:
#             if col not in self.header:
#                 self.column.append(col)
#                 status = False
#         return status


#     def read_txt(self,file_name):
#         return "reading from read_txt method"

#     def default_file(self): 
#         fr = open('test-data.csv')
#         read = csv.DictReader(fr)
#         return read
























#def is_valid_file(file_name):
#     if path.exists(file_name):
#         if file_name.endswith('.csv'):
#             return True
#         else :
#             print("enter csv file only...")
#     else :
#         print("file not exist")
