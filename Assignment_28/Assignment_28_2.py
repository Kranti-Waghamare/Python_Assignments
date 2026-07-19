'''
Q. count words in a file
write a program which accepts a file name from the user and counts total number of words in that file.

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
            Words = line.split()

            Count = Count + len(Words)

        print("Total number of words are : ",Count)
        
        fobj.close()

    except FileNotFoundError as fobj:
        print("File is not present in current directory")

if __name__ == "__main__":
    main()