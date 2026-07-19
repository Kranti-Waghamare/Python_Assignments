'''
Q. copy file contents into new file 
write a program which accepts an existing file name through command line arguments
creates new file named Demo.txt and copies all contents from the given file into Demo.txt

Input (command line): ABC.txt
Output : create Demo.txt and copy contents of ABC.txt into Demo.txt
'''

def main():
    try:

        fobj = open("Demo.txt", "r")

        sobj = open("ABC.txt", "w")

        for line in fobj:
            sobj.write(line)
        
        fobj.close()
        sobj.close()

    except FileNotFoundError as fobj:
        print("File is not present in current directory")

if __name__ == "__main__":
    main()