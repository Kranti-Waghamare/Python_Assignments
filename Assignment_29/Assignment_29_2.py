'''
Q. Display file content

write a program which accepts file name from user, open that file, and display the entire contents on the console. 

Input : Demo.txt
Output : Display contents Demo.txt on console

'''
def main():
    try:
        print("Enter file name : ")
        FileName = input()

        fobj = open(FileName, "r")

        for line in fobj:
            print(line)
        
        fobj.close()

    except FileNotFoundError as fobj:
        print("File is not present in current directory")

if __name__ == "__main__":
    main()