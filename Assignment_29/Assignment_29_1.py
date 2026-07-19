'''
Q. check file is Exist in current directory 

write a program which accepts file name from user and checks wheather that file exist in the current directory or not 

Input : Demo.txt
Output : Display wheater Demo.txt exists or not

'''
import os

def main():

    print("Enter the file name : ")
    FileName = input()

    Ret = os.path.exists(FileName)

    if(Ret == True):
        print("File is present in current directory")
    else:
        print("There is no such file")

if __name__ == "__main__":
    main()