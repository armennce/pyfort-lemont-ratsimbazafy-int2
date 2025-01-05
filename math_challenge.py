import random

def maths_challenge():
    list_challenges = [math_challenge_factorial(), nearest_prime(random.randint(10, 20)), linear_equation_test()]
    challenge = random.choice(list_challenges)

    res = challenge
    print(f"You'll play to {res}.")

def factorial(n):
    """
    arguments --> n: a positive integer.
    returns --> the factorial of n
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def math_challenge_factorial():
    import random
    """
    returns --> True if correct, else False
    """
    n = random.randint(1, 10)
    print(f"Math Challenge: Calculate the factorial of {n}.")
    user_answer = int(input("Your answer: "))
    correct_answer = factorial(n)

    if user_answer == correct_answer:
        print("Correct! You win a key.")
        return True
    else:
        print("Incorrect.")
        return False

def is_prime(n):
    """Check if n is prime
    arguments --> n: integer

    returns --> True if n is prime, else False
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def nearest_prime(n):
    """Finding the nearest prime number greater or equal to n
    arguments --> n : integer

    returns --> nearest prime number to n
    """
    while not is_prime(n):
        n += 1
    return n

def math_challenge_prime():
    """
    returns --> True if it's the right answer/ else False
    """
    number = random.randint(10, 20)
    print(f"Math Challenge: Find the nearest prime to {number}.")
    user_answer = int(input("Your answer: "))
    correct_answer = nearest_prime(number)

    if user_answer == correct_answer:
        print("Correct! You win a key.")
        return True
    else:
        print("Incorrect.")
        return False

import random

def solve_linear_equation():
    """
    returns --> a tuple (a, b, solution) where a and are the coefficients and solution is the value of x
    """

    a = random.randint(1, 10)
    b = random.randint(1, 10)
    solution = -b / a
    return a, b, solution

def linear_equation_test():
    """
    returns --> True if the answer is correct, else False
    """
    a, b, solution = solve_linear_equation()
    print(f"Math Challenge: Solve the equation {a}x + {b} = 0.")
    user_answer = float(input("What is the value of x: "))  # we use floats because we accept decimal values

    if abs(user_answer - solution) < 1e-6:  # for rounded values
        print("Correct! You win a key.")
        return True
    else:
        print("Incorrect.")
        return False
