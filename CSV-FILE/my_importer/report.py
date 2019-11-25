class Report:
    def __init__(self):
        self.total = 0
        self.valid = 0
        self.invalid = 0
        self.duplicate = 0
        self.invalid_record = dict()

    def push_record(self,data):
        self.invalid_record.update(data)

    def get_record(self):
        for key,value in self.invalid_record.items():
                print(str(key) +" : "+str(value))
    
    def report(self):
        print("###############################")
        print("Total Record : %d" % self.total)
        print("Total record inserted : %d" % self.valid)
        print("Duplicate record : %d" % self.duplicate)
        print("Total Invalid Record : %d" % self.invalid) 
        print("###############################")
        # if len(self.invalid_record):
        #     self.get_record()


























        # if len(self.invalid_record) > 0:
        #     print("Incorrect data :")
        #     self.get_record()
            
            #print(self.invalid_record)
            # print("Incorrect data : ")
            # for line_no,record in self.invalid_record.items():
            #     print(line_no + ":" + record)
        


    












    