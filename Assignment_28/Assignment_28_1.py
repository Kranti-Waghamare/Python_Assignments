'''
Q. count lines in a file
write a program which accepts a file name from the user and counts how many lines are present in the file.

input : Demo.txt
Expected output : Total number of lines in Demo.txt

'''
def main():
    try:
        print("Enter file name : ")
        FileName = input()

        fobj = open(FileName, "r")

        Count = 0

        for line in fobj:
            Count +=1

        print(f"Total number of lines in {FileName} are : ",Count)
        
        fobj.close()

    except FileNotFoundError as fobj:
        print("File is not present in current directory")

if __name__ == "__main__":
    main()