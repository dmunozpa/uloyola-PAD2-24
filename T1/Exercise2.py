def factorial(n):
    # Base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    # Recursive case: n! = n * (n-1)!
    else:
        return n * factorial(n - 1)

# Test the function
def main():

    number = int(input("Enter a number: "))
    print(f"Factorial of {number} is {factorial(number)}")


if __name__ ==  "__main__":
    main()