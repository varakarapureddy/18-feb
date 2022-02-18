def fact(n):
    """returns factorial of n."""
    if n <= 1:
        return 1
    return n * fact(n - 1)


def count_digits(n):
    """Assumes n > 1.
    returns sum of digits of n's factorial."""
    factorial = fact(n)
    total = 0
    for digit in str(factorial):
        total += int(digit)
    return total


if __name__ == '__main__':
    n = int(input("Enter a number : "))
    print(count_digits(n))
