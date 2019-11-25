from mydb.mysql_db import Database
class Employee(Database):
    id = None
    f_name = None
    l_name = None
    contact= None
    dob = None
    dept_id = None
    uname = None
    table = 'emp'
    column = None
    #column = {'EID':'id','FIRST_NAME':'f_name','LAST_NAME':'l_name','CONTACT':'contact','DOB':'dob','USER_NAME':'uname','DEPT_ID':'dept_id'}
    

    def __init__(self,id=None):
        super(Employee,self).__init__()           
        #self.id = id 
        
        
    def __str__(self):
        return "employee id ="+str(self.id)+"  user name ="+self.uname+"  first name= "+self.f_name+"  last name= "+self.l_name+"  contact= "+self.contact+"  DOB= "+str(self.dob)+"  department= "+str(self.dept_id)

    def create_dic(self):
        self.column = {'EID':self.id,'FIRST_NAME':self.f_name,'LAST_NAME':self.l_name,'CONTACT':self.contact,'DOB':self.dob,'USER_NAME':self.uname,'DEPT_ID':self.dept_id}
        nda = {}
        for key,val in self.column.items():
            if val != None:
                nda.update({key:val})
        return nda


    def insert(self):
        return super().insert(self.table,self.create_dic())
        #self.get_detail()

    def get_detail(self,data=None):
        
        result =  super().select(self.table,data)
        for row in result:
            self.id = row[0]           
            self.f_name = row[1]
            self.l_name = row[2]
            self.contact = row[3]
            self.dob = row[4]
            self.uname = row[5]
            self.dept_id = row[6] 
        

    def update(self):
        data ={}
        data = self.create_dic()
        self.get_detail()
        super().update(self.table,{'update':data,'where':{'EID':self.id}})
        #self.get_detail({'EID':self.id})
        

    def delete(self):
        self.get_detail()   
        super().delete(self.table,{'EID':self.id})
           
                
    @classmethod
    def all(cls):
        return super().select(cls.table,None)

    
    @classmethod
    def search(cls,data):
        res = ''
        where =''
        
        new_data = data.fromkeys('C',data.keys())       
        filed = ''.join(new_data['C'])
        where += ' '.join(data[filed].keys()) + "'" + ' '.join(data[filed].values()) + "'"
        for key,val in cls.column.items():
            if filed in val:
                res = key
        result = super().select(cls.table,{'filed':res,'condition':where})
        if len(result) == 0:
            return "Employee record not found.."
        else:
            return result

    @classmethod
    def query(cls,sql):
        result = super().query(sql)
        if len(result) == 0: 
            #return "Department record not found.."
            return None
        else:
            return result
         

    

        
    
    
            

    
        





# res = ''
#         for key,val in cls.column.items():
#             if data['filed'] in val:
#                 res = key
#         data['filed'] = res
#         result = super().select(cls.table,data)
#         if len(result) == 0:
#             return "Employee record not found.."
#         else:
#             return result
