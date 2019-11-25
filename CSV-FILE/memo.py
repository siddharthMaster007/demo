import classes.employee as ep
from diskcache import Cache
import time


def sort(my_list):

    my_list.sort()
    small = my_list[0]
    for i in my_list:
        if small == i:
            count = i - small 
            print(i - count)
        else:
            print(small)



if __name__ == "__main__":

    sort([60,40,12,22,33])        
         





# def fibo(n):
#     if n == 0 or n == 1:
#         return 1
#     else :
#         return fibo(n-1) + fibo(n-2)



# cac = Cache()
#    cac.set(10,100)
#help(Cache)

# @lru_cache(maxsize=20)
# def get(no):
#     for i in range(0,no):
#          return ep.Employee.query("select * from emp")

# if __name__ == "__main__":

#     t1 = time.time()
#     cac = Cache()
#     for i in range(20):
#         cac.push(i)
#     print(cac.__len__())

#     t2 = time.time()
#     print("total = %.10f" % (t2-t1) )
    














































































































































# # # from functools import lru_cache
# # # import time


# # # def fibo(n):
# # #     my_dict = list()
# # #     # if n == 0 or n == 1:
# # #     #     return 1
# # #     # else :
# # #     #     return fibo(n-1) + fibo(n-2)
# # #     for i in range(0,1000000):
# # #         my_dict.append(i)
        


