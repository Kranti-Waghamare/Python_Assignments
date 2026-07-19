'''
Q. search a word in file
write a program which accepts a file name and a word from the user and checks wheather that word is present in the file or not. 

input : Demo.txt Marvellous
Expected output : display wheather the word Marvellous is found in Demo.txt or not
'''
def main():
    try:
        print("Enter Source file name : ")
        FileName = input()

        print("Enter the word : ")
        Search = input()

        fobj = open(FileName, "r")
        
        Ret = False

        for line in fobj:
           if(line.find(Search)):
               Ret = True
               break

        if(Ret == True):
            print("Word is found")
        else:
            print("Word is not found")
        
        fobj.close()

    except FileNotFoundError as fobj:
        print("File is not present in current directory")

if __name__ == "__main__":
    main()