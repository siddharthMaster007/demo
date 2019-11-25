import MySQLdb
class Database:
    host = 'localhost'
    usr = 'root'
    pwd = 'aloha'
    dbn = 'Demo' 
    con = MySQLdb.connect(host=host,user=usr,passwd=pwd,database=dbn)
    cur = con.cursor()

    def __init__(self):
        #self.con = mysql.connector.connect(host =self.host,user=self.usr,passwd=self.pwd,database = self.dbn)
        #self.cur = self.con.cursor()
        pass

    #inserting operation 
    
    def insert(self,table,data):        
        column_values = ''
        column_names = ''
        column_names += ",".join(data.keys())
        column_values += ','.join(map("'{}'".format, data.values()))
        sql = "INSERT INTO %s (%s) VALUES (%s)" % (table,column_names,column_values)
        self.cur.execute(sql)
        self.con.commit() 
        return self.cur.lastrowid
        #print(self.cur.lastrowid)

    #Upadation operation
    def update(self,table,data):        
        update_data = ''
        where = '' 
        for column_name, column_value in data['update'].items():
            column_value =  "'" + str(column_value)+ "'" 
            if len(update_data) > 0:
                update_data +=','+column_name + '=' + ''.join(column_value)
            else :
                update_data += column_name + '=' + ''.join(column_value)

        where += ' '.join(data['where'].keys()) + "=" + ' '.join(map("'{}'".format, data['where'].values()))
        sql = "UPDATE %s SET %s WHERE %s" % (table,update_data,where)
        print(sql)
        self.cur.execute(sql)
        self.con.commit()    


    #Deletion operation
    def delete(self,table,data):
        where = ''
        where += ' '.join(data.keys()) + "=" + ' '.join(map("'{}'".format, data.values()))
        sql = "DELETE FROM %s WHERE %s" % (table,where) 
        self.cur.execute(sql)
        self.con.commit()

    #selection operation
    @classmethod
    def select(cls,table,data):        
        sql=''
        if data is None:
            sql = "SELECT * FROM %s" % (table)
        else:
            sql = "SELECT * FROM %s WHERE %s %s" % (table,data['filed'],data['condition'])
        cls.cur.execute(sql)
        return cls.cur.fetchall()

    @classmethod
    def query(cls,sql):
        cls.cur.execute(sql)
        return cls.cur.fetchone()

    # closing the connection
    def con_close(self):
        self.con.close() 









"""  def delete(self,data):
        table = data['table']
        condition = ''

        for condition_col,condition_val in data['condition'].items():
            condition_val = "'" + condition_val + "'"
            condition += str(condition_col) + "=" + str(condition_val)
        
        sql = "DELETE FROM %s WHERE %s" % (table,condition) 
        self.cur.execute(sql)
        self.con.commit()
        print("data Deleted Successfully..") 



    def select(self,table,where):
        sql = "SELECT * FROM %s" % (table)
        if where is not None:
        # where = ' '+data['filed']+' '+''.join(data['condition'].keys())+' '
            # val = ''.join(data['condition'].values())
            #sql = "SELECT * FROM %s WHERE %s'%s' " % (table,where,val)   
        self.cur.execute(sql)
        return self.cur.fetchall()
   
  
    
    def select_columns(self,data):

        #columns = data['columns']
        table = data['table']
        column_names = ''
        for column in data['columns']:

            column_names += ',' + str(column) if len(column_names) > 0 else str(column)
        
        sql = "SELECT %s FROM %s" % (column_names,table)
        self.cur.execute(sql)
        return self.cur.fetchall()

        elif 'like' in data:
            sql = "SELECT * FROM %s WHERE %s LIKE '%s'" % (table,data['filed'],data['like'])

"""
        
        
    
   
    


             
        



        




    
        
        