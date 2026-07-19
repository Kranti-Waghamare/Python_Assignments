'''
Q. count lines in a file
write a program which accepts a file name from the user and displays contents of the file line by line on the screen.

input : Demo.txt
Expected output : Display each line of Demo.txt one by one.

'''
def main():
    try:
        print("Enter file name : ")
        FileName = input()

        fobj = open(FileName, "r")

        for line in fobj:
            print(line, end = " ")
        
        fobj.close()

    except FileNotFoundError as fobj:
        print("File is not present in current directory")

if __name__ == "__main__":
    main()