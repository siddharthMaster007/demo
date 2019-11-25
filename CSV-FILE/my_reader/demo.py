class MyClass:
    cnt = 0
    cnt += 1
    print(cnt)
    def __init__(self):
        print("hello myclass")
    
    def display(self):
        print("hello display")


if __name__ == "__main__":
    
    obj = MyClass()
    for i in range(0,6):
        obj.display()
    ob2 = MyClass()