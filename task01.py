def user_input():
    num = list(input("Please enter a number for palindrome check: "))
    return num


def check_palindrome(number):
    number_test = number[::-1]

    return number == number_test


def check_palindrome(num):
    if isinstance(num, bool) or not isinstance(num, list):
        return -1

    num_copy = 0;

    while num > 0:
        num_copy *= 10
        num_copy += num % 10
        num //= 10

    return num == num_copy


def user_output(result):
    msg = f"The number you've entered is {result}"
    return msg


def main():
    num = user_input()
    result = check_palindrome(num)
    msg = user_output(result)
    print(msg)


main()


def palindrom(number):
    if number <= 0:
        return -1
    ls = []
    while number > 0:
        last_digit = number % 10
        ls.append(last_digit)
        number = number // 10

    while len(ls) != 0:
        if ls[0] != ls[len(ls) - 1]:
            return False
        ls = ls[1:len(ls) - 1]

    return True


def main():
    number = int(input("Input your number: "))

    result = palindrom(number)

    msg = (f"Enter a natural number." if result == -1
           else "Your number is a palindrome." if result
    else f"Your number is not a palindrome.")

    print(msg)


main()
