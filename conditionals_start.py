#
# Example file for working with conditional statements
# LinkedIn Learning Python course by Joe Marini
#



def main():
    x, y = 1000, 100

    # conditional flow uses if, elif, else
    # if x < y:
    #  result="x is smaller than y"
    # #  print(result)
    # elif x==y: 
    #  result="x = y"
    # #  print(result)
    # else:
    #  result="x > y"
    # print(result)
    # conditional statements let you use "a if C else b"
    # print("x is greater than y") if x>y else print("x=y or less than y")
    # match-case makes it easy to compare multiple values
    value=input("Input value \n")
    match value:
        case "one":
            result=1
        case "two":
            result=2
        case "three":
            result=(3,4)
        case _ :
            result=-1
    print(result)                    

if __name__ == "__main__":
    main()
