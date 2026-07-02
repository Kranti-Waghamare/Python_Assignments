#write a program which accepts one charachter ans checks whether it is vowel or consonant.
# Input : a
# Output : Vowel

# Input : b
# Output : consonant

def ChkVowel(Ch):
    if((Ch == 'a' or Ch == 'A') or (Ch == 'e' or Ch == 'E') or 
       (Ch == 'i' or Ch == 'I') or (Ch == 'o' or Ch == 'O') or (Ch == 'u' or Ch == 'U') ):
        return True
    else:
        return False
    
def main():
    print("Enter the characher ")
    ch = input()

    Ret = ChkVowel(ch)

    if(Ret == True):
        print("It is vowel")
    else:
        print("It is Consonant")

if __name__ == "__main__":
    main()