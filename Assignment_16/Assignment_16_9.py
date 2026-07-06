#write a program which display first 10 even numbers on screen.

def main():
    Count = 1
    while(Count <= 20):
        if((Count % 2) == 0):
            print(Count, end = " ")

        Count += 1
  
if __name__ == "__main__":
    main()