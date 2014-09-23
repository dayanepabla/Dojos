def fizz_buzz(number):

    if number % 15 == 0:
        return "fizzbuzz"

    if number % 3 == 0:
        return "fizz"

    if number % 5 == 0:
        return "buzz"

    return number

for number in range(1,100):
    print (fizz_buzz(number))
