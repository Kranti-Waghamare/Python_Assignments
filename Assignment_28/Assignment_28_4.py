'''
Q. copy file contents into another file 
write a program which accepts a file name from the user 
    - first file is an existing file
    -second file is new file

input : ABC. txt, Demo.txt
Expected output : content of ABC.txt is copied into Demo.txt

'''
def main():
    try:
        print("Enter Source file name : ")
        FileName = input()

        print("Enter the destination file name : ")
        NameFile =input()

        fobj = open(FileName, "r")
        sobj = open(NameFile , "w")

        for line in fobj:
            sobj.write(line)
        
        fobj.close()
        sobj.close()

    except FileNotFoundError as fobj:
        print("File is not present in current directory")

if __name__ == "__main__":
    main()