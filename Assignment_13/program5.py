#write a program which accepts marks and display grades.

def DisplayGrades(No):
    Count = 0 

    if(No >= 75):
        print("Distiction")
    elif(No >= 60):
        print("First class")
    elif(No >= 50):
        print("Second class")
    else:
        print("fail")

def main():
    print("Enter the number")
    Value = int(input())

    DisplayGrades(Value)

if __name__ == "__main__":
    main()