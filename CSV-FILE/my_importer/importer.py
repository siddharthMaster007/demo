# from classes.department import *
# from classes.employee import *
# from my_importer.report import *
import classes.department as dt
import classes.employee as ep
from my_importer.report import Report

class Importer(Report):
    def __init__(self):
        super().__init__()

    
    
    def import_data(self,data):
        dept_list = dict()
        emp_list = dict()

        for row in data:
            try:
                dept = dt.Department()
                emp = ep.Employee()
                self.total += 1
                if row['DEPARTMENT'] == "":
                    raise ValueError
                #dept_entry = hash(row['DEPARTMENT'])
                if row['DEPARTMENT'] not in dept_list:
                   #inserting department record    
                    dept.name = row['DEPARTMENT']
                    dept.id = dept.insert()
                    dept_list.update({row['DEPARTMENT']:dept.id})
                    

                    #dt.Department.query("insert into dept (NAME) values('"+row['DEPARTMENT']+"')")
                    #record = dt.Department.search({'name':{'=':row['DEPARTMENT']}})
                    #record = dt.Department.query("select * from dept where NAME = '"+row['DEPARTMENT']+"'")
                    #mi= dt.Department.query("select last_insert_id()")
                    #print(mi[0])
                    #dept.id = mi[0]
                    # dept.name = record[1]
                    
                    # print(type(mi))
                    # for dept_row in record:
                    #     dept.id = dept_row[0]
                    #     dept.name = dept_row[1]
                    #     dept_list.update({row['DEPARTMENT']:dept.id})
                else:
                    dept.id = dept_list[row['DEPARTMENT']]
                    #dept.id = int("".join(map(str,s dept_list[dept_entry].keys()))) 
                    
                #inserting employee record
                if row['USER_NAME'] not in emp_list:
                    emp.f_name = row['FIRST_NAME']
                    emp.l_name = row['LAST_NAME']
                    emp.contact = row['CONTACT']    
                    emp.dob = row['DOB']    
                    emp.uname = row['USER_NAME']
                    emp.dept_id = dept.id
                    emp.id = emp.insert()    
                    emp_list.update({row['USER_NAME']:emp.id})
                    self.valid += 1
                    print("{} record inserted successfully.....".format(data.line_num-1))   
                else :
                    self.duplicate += 1

            except Exception :
               self.invalid += 1
        
    

    

        # for row in data:
        #     try:
        #         dept = dt.Department()
        #         emp = ep.Employee()
        #         self.total += 1
        #         dept_entry = dt.Department.search({'name':{'=':row['DEPARTMENT']}})
        #         if dept_entry is None:
        #             #inserting department record    
        #             if row['DEPARTMENT'] == "":
        #                 raise ValueError
        #             dept.name = row['DEPARTMENT']
        #             dept.insert()
        #         else:
        #             for dept_row in dept_entry:
        #                 dept.id = dept_row[0]
        #                 dept.name = dept_row[1]

        #         #inserting employee record
        #         emp_entry = ep.Employee.query("select * from emp where USER_NAME = '"+row['USER_NAME']+"' and "+"DEPT_ID="+str(dept.id))
        #         if emp_entry is None:
        #             emp.f_name = row['FIRST_NAME']
        #             emp.l_name = row['LAST_NAME']
        #             emp.contact = row['CONTACT']
        #             emp.dob = row['DOB']
        #             emp.uname = row['USER_NAME']
        #             emp.dept_id = dept.id
        #             emp.insert()    
        #             self.valid += 1
        #             print("{} record inserted successfully.....".format(data.line_num-1))
        #         else :
        #             self.duplicate += 1

        #     except Exception :
        #         self.invalid += 1
        #         #self.push_record({data.line_num:row})
                
    

             

        



















# self.incorect_data = list()
        # self.error_line = list()
        #self.report()
    # def error_data(self):     
    #     if bool(self.incorect_data):
    #         print("\nIncorrect data: ")
    #         print(''.join(map("{} => {}\n".format,self.error_line,self.incorect_data)))
            







################################### HASH IMPLEMENTATION ############################






#  dept_list = dict()
#         emp_list = list()
#         #my = 0
#         for row in data:
#             try:
#                 dept = dt.Department()
#                 emp = ep.Employee()
#                 self.total += 1
                
#                 #dept_entry = dt.Department.search({'name':{'=':row['DEPARTMENT']}})
#                 if row['DEPARTMENT'] == "":
#                     raise ValueError

#                 dept_entry = hash(row['DEPARTMENT'])
#                 if dept_entry not in dept_list:
#                    #inserting department record    
#                     dept.name = row['DEPARTMENT']
#                     dept.insert()
#                     record = dt.Department.search({'name':{'=':row['DEPARTMENT']}})
#                     for dept_row in record:
#                         dept.id = dept_row[0]
#                         dept.name = dept_row[1]
#                         dept_list.update({dept_entry:{dept.id:dept.name}})
#                         #my +=1
#                 else:
#                     #for id,name in dept_list(dept_entry).items():
#                     dept.id = int("".join(map(str, dept_list[dept_entry].keys()))) 
#                     #dept.id = dept_list[dept_entry][dept.name]

#                 #inserting employee record
#                 #emp_entry = ep.Employee.query("select * from emp where USER_NAME = '"+row['USER_NAME']+"' and "+"DEPT_ID="+str(dept.id))
#                 emp_entry = hash(row['USER_NAME'])
#                 if emp_entry not in emp_list:
#                     emp.f_name = row['FIRST_NAME']
#                     emp.l_name = row['LAST_NAME']
#                     emp.contact = row['CONTACT']
#                     emp.dob = row['DOB']
#                     emp.uname = row['USER_NAME']
#                     emp.dept_id = dept.id
#                     emp.insert()    
#                     emp_list.append(emp_entry)
#                     self.valid += 1
#                     print("{} record inserted successfully.....".format(data.line_num-1))
                    
#                 else :
#                     self.duplicate += 1

#             except Exception :
#                 self.invalid += 1
#                 #self.push_record({data.line_num:row})
#             #print(my)    
       










#inserting employee record
            # emp_entry = Employee.query("select count(*) from emp where USER_NAME = 'sid@gmail.com' and DEPT_ID = 100")
            # res = "".join(map(str, emp_entry))
            # print(int(res))
            #print(type(emp_entry))


# print("\nIncorrect data")
#         print(':'.join(map("{}".format,error_line))+" ")
#         print(''.join(map("{}\n".format,incorect_data)))
# from classes.department import *
# from classes.employee import *
# from my_importer.report import *
# import classes.department as dt
# import classes.employee as ep
# from my_importer.report import Report

# class Importer(Report):
#     def __init__(self):
#         super().__init__()

#     def import_data(self,data):
#         for row in data:
#             try:
#                 dept = dt.Department()
#                 emp = ep.Employee()
#                 self.total += 1
#                 dept_entry = dt.Department.search({'name':{'=':row['DEPARTMENT']}})
#                 if dept_entry is None:
#                     #inserting department record    
#                     if row['DEPARTMENT'] == "":
#                         raise ValueError
#                     dept.name = row['DEPARTMENT']
#                     dept.insert()
#                 else:
#                     for dept_row in dept_entry:
#                         dept.id = dept_row[0]
#                         dept.name = dept_row[1]

#                 #inserting employee record
#                 emp_entry = ep.Employee.query("select * from emp where USER_NAME = '"+row['USER_NAME']+"' and "+"DEPT_ID="+str(dept.id))
#                 if emp_entry is None:
#                     emp.f_name = row['FIRST_NAME']
#                     emp.l_name = row['LAST_NAME']
#                     emp.contact = row['CONTACT']
#                     emp.dob = row['DOB']
#                     emp.uname = row['USER_NAME']
#                     emp.dept_id = dept.id
#                     emp.insert()    
#                     self.valid += 1
#                     print("{} record inserted successfully.....".format(data.line_num-1))
#                 else :
#                     self.duplicate += 1

#             except Exception :
#                 self.invalid += 1
#                 self.push_record({data.line_num:row})
                
    




















# self.incorect_data = list()
        # self.error_line = list()
        #self.report()
    # def error_data(self):     
    #     if bool(self.incorect_data):
    #         print("\nIncorrect data: ")
    #         print(''.join(map("{} => {}\n".format,self.error_line,self.incorect_data)))
            

























#inserting employee record
            # emp_entry = Employee.query("select count(*) from emp where USER_NAME = 'sid@gmail.com' and DEPT_ID = 100")
            # res = "".join(map(str, emp_entry))
            # print(int(res))
            #print(type(emp_entry))


# print("\nIncorrect data")
#         print(':'.join(map("{}".format,error_line))+" ")
#         print(''.join(map("{}\n".format,incorect_data)))