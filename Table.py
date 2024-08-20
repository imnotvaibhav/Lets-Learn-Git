# Table of 9
def table(n=9):
    print("---------------")
    for i in range(1,11):
        print(n,"*",i,"=",n*i)
    print("---------------")
        
    return None

if __name__ == "__main__":
    table()