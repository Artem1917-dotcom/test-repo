def fizz_buzz (n):
    for i in range (1, n+1):
        if i % 17 == 0:
            print ("FizzBuzz")
        elif i % 5 == 0:
            print ("Fizz")
        elif i % 7 == 0:
            print ("Buzz")
        else:
            print (i)

fizz_buzz (21)