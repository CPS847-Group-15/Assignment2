def fb(number):
    if(number % 15 == 0):
        return "fizz buzz"
    if(number % 5 == 0):
        return "buzz"
    if(number % 3 == 0):
        return "fizz"
    return str(number)