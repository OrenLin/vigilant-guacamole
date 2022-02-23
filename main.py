def greet_user(a,b="123123"):
    c= a + b
    return c

while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")

    a = input("First name: ")
    if a == 'q':
        break

    b = input("Last name: ")
    if b == 'q':
        break

    formatted_name = greet_user(a,b)
    print("\nHello, " + formatted_name + "!")

