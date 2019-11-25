from sys import exit
from os.path import splitext
import my_importer.importer as im
import my_reader.reader as re
import time
from diskcache import Cache

# from  my_importer.importer import *
# from my_reader.reader import *    


if __name__ == "__main__":    
    try:
        # Taking input as file name
        file_name = input("enter file name : ")
        file_exten = splitext(file_name)[1]

        # check file type and creating object 
        if file_exten == '.csv':
            reader = re.CsvReader(file_name)
        elif file_exten == '.tsv':
            reader = re.TsvReader(file_name)
        importer = im.Importer()

        # check file exist or not   d
        if reader.file_exist(): 
            data = reader.read()
            start = time.time()
            importer.import_data(data)
            end = time.time()
    except Exception as e:
        print(e)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
    finally:
        try:
            reader.file_close()
            #importer.report()
            print("total = %.5f" % (end-start) )
            print("Thank You !!!!")
        except Exception as e:
            print("application terminated......")
        exit(0)
        
    

    
    
        











# fn,fe = path.splitext(file_name)
            # if fe == '.csv':
            #     reader.read_csv(file_name)
            #     data = reader.read_csv(fidatle_name)
            #     importer.import_csv(data)
            # if fe == '.txt':
            #     reader.read_txt(file_name)csd


    # try:

    #     dept = Department()
    #     emp = Employee()
    #     dept_entry = None
    #     with open('data-csv.csv') as fr:
    #         read = csv.DictReader(fr)   

    #         for row in read:
    #             dept_entry = Department.search({'name':{'=':row['DEPARTMENT']}})
    #             if dept_entry is None:
    #                 #inserting department record 
    #                 dept.name = row['DEPARTMENT']
    #                 dept.insert()
    #             else:
    #                 for dept_row in dept_entry:
    #                     dept.id = dept_row[0]
    #                     dept.name = dept_row[1]
    
    #             #inserting employee record
    #             emp.f_name = row['FIRST_NAME']
    #             emp.l_name = row['LAST_NAME']
    #             emp.contact = row['CONTACT']
    #             emp.dob = row['DOB']
    #             emp.uname = row['USER_NAME']
    #             emp.dept_id = dept.id
    #             emp.insert()
                         




                        # print(row2)
                        # print(row['FIRST_NAME'])
                        #emp.dept_id = row2[0]
                        # print(emp.dept_id)
                        #emp.insert()
                    # print('employe inserted none')
                    # print(dept.id)
                    # print(row['FIRST_NAME'])
                    # print("---")
                #print(dept.id)
                #rs += ''.join(map('{}'.format,dept_entry[0]))
                #print(rs) 
                #else:
                    # emp.f_name = row['FIRST_NAME']
                    # emp.l_name = row['LAST_NAME']
                    # emp.contact = row['CONTACT']
                    # emp.dob = row['DOB']
                    # emp.uname = row['USER_NAME']
                    # emp.dept_id = 93
                    # emp.insert()
                   # print('employe inserted')


                    #for row2 in dept_entry:
                        # print("===")
                        # print(row2[0])
                        # print(row['FIRST_NAME'])
                        
            # for row in read:
            #     print(row['EID'])
            #     print(row['FIRST_NAME'])  
                    
            
            #for col in entry :
                    

                    

                    #inserting employee record

                # else:
                #     print("department is already present...")
            # dept_data = set()
            # for row in read:
            #     dept_data.add(row['NAME'])
        #print(data)
            
        #data = set(['test2','test6','test1','test4'])

        
        # for row in dept.all():
        #     dept.id = row [0]
        #     dept.name = row[1]

        #     if dept.name in data:
        #         print(dept.name+'p')
        #     else:
        #         print(dept.name+'a')





            # for col in data:
            #     if dept.name != col:
            #         print(dept.name+' != '+col)
            #         print(col)
            #         print("=========")
            
        
        # for row in dept.all():
        #     dept.id = row[0]
        #     dept.name = row[1]
        #     set_data.add(dept.name)
        # print(set_data)


        #=================finale code ================
        #set_data = set()      
        # for col in data:
        #     for row in dept.all():
        #         dept.id = row[0]
        #         dept.name = row[1]
        #         set_data.add(dept.name)
        #         if col  in set_data:
        #             print(dept.name)
        #         #dept.insert()
        # entry = None
        # for col in data:
        #     entry = dept.search({'name':{'=':col}})
        #     if entry is None:
        #         dept.name = col
        #         dept.insert()

        


        

        # print(set_data)
        # with open('data-csv.csv') as fr:
        #     read = csv.DictReader(fr)
        #     dept.get_detail()
        #     for row in read:
        #         if dept.name == row['DEPARTMENT']:
                    
        
        
        # print("***** DEPARTMENT DETAIL *****")
        # result = Department.all()
        # for row in result:
        #     dept.id = row[0]
        #     dept.name = row[1]
        #     print(dept)
        
        # print("\n")
        # print("***** EMPLOYEE DETAIL *****")
        # result = Employee.all()
        # for row in result:
        #     emp.id = row[0]            
        #     emp.f_name = row[1]
        #     emp.l_name = row[2]
        #     emp.contact = row[3]
        #     emp.dob = row[4]
        #     emp.dept_id = row[6]  
        #     emp.uname = row[5]  
        #     print(emp)  

    # except Exception as e :
    #      print("Exception occured : ",e)

    # finally:
    #     emp.con_close()
    #     dept.con_close()


























#### Department data sample #######
#data_update = { 'NAME':'HR'}, 'condition': {'DID':'500'}}
#delete_data = {'table':'dept','condition': {'DID':'1000'}}
#select_data = {'columns':['DID','NAME'],'where':{'DID':'200'}
#emp.insert({'FIRST_NAME':'AJAY','LAST_NAME':'SALUNKE','CONTACT':'9673858607','DOB':'1997-08-10','DEPT_ID':dept.id,'USER_NAME':'sada@gmail.com'})

# emp.f_name = 'AJAY'
#         emp.l_name = 'SALUNKE'
#         emp.contact = '9673858607'
#         emp.dob = '1997-08-10'
#         emp.dept_id = dept.id
#         emp.uname =  'sada@gmail.com'
#Department.search()

        #searching the record in table    
        # dept2 = Department()
        # dept2.id = 100
        # if dept2.search() == 0:
        #     print("Record is not found ")
        # else:
        #     print("Record is found : ",dept2)  
         
        # #seraching record in table 
        # emp2 = Employee()
        # emp2.f_name='sid'
        # if emp2.search() == 0:
        #     print("Employee Record is  not found")
        # else:
        #     print(" EmployeeRecord is Found : ",emp2)
