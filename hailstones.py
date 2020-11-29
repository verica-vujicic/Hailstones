"""
File: hailstones.py
Pick some positive integer and call it n.
If n is even, divide it by two.
If n is odd, multiply it by three and add one. Continue this process until n is equal to one.
"""

def main():

    count = 0
    num = int(input("Enter a number: "))
    
    while num != 1:
        if num % 2 == 0:
            result = num / 2
            print(str(num) + " is even, so I take half: " + str(int(result)))
            num = result
            count += 1
        else:
            result = 3 * num + 1
            print(str(num) + " is odd, so I make 3n + 1: " + str(int(result)))
            num = result
            count += 1
            
    print("The process took " + str(count) + " steps to reach 1")

if __name__ == '__main__':
    main()
