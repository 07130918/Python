def run(number):
    if number == 1 or number == 2:
        return 1
    
    return run(number - 1) + run(number - 2)