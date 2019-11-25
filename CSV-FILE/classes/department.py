from mydb.mysql_db import Database
class Department(Database):
    id = None
    name = None
    table = 'dept'  
    column = {'DID':'id','NAME':'name'}

    def __init__(self,id=None):
        super(Department,self).__init__()     
        #self.column = {'DID':self.id,'NAME':self.name}
        
    def __str__(self):
        return "Department Id = "+str(self.id)+" \tDepartment Name = "+str(self.name)

    
    def insert(self):
        return super().insert(self.table,{'NAME':self.name})


    def get_detail(self,data=None):
        result =  super().select(self.table,data)                   
        for row in result:
            self.id = row[0]
            self.name = row[1]     

    def create_dic(self):
        
        nda = {}
        for key,val in self.column.items():
            if val != None:
                nda.update({key:val})
        return nda

    def update(self):
         super().update(self.table,{'update':{'NAME':self.name},'where':{'DID':self.id}})
        

    def delete(self):
        super().delete(self.table,{'DID':self.id})

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
            return None
        else:
            return result
    

