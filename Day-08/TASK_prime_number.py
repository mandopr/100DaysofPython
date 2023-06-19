def prime_checker(number):
    is_prime = True
    for x in range(2, number):
        if number % x == 0:
            is_prime = False

    if is_prime:
        print(f"\n{num} is a prime number")
    else:
        print(f"\n{num} is not a prime number")


num = int(input("\n\nEnter number to check whether it is prime or not : "))
prime_checker(num)
