def main():
    #write your code below this line
    print("Greatest:", greatest(2,7,9))

def greatest(number1, number2, number3):
    greatest = number1

    if number2 > greatest:
        greatest = number2
    
    if number3 > greatest:
        greatest = number3

    return greatest

if __name__ == '__main__':
    main()
