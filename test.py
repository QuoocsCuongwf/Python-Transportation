def main():
    n=int(input("Enter the number of rows: "))
    for i in range(n):
        for j in range(n):
            if (j<i):
                print(" ",end="")
            else:
                print("*",end="")
        print()

if __name__ == "__main__":
    main()

    