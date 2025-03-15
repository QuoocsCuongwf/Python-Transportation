def main():
    n=int(input("Enter the number of rows: "))
    l=[];sum=0
    for i in range(n):
        l.append(int(input("Enter the number: ")))
        sum+=l[i]
    print(5 in l)
    print(sum)
    print(l[len(l)-1])
    for i in range(len(l)-1,-1,-1):
        print(l[i], end=" ")
        
    l.reverse()
    print(l)


if __name__ == "__main__":
    main()

    