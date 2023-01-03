
try:
    odd_numbers = [1,3,5,9]
    #print(odd_numbers[3]/0)
    print(odd_numbers[4])

except ZeroDivisionError:
    print('Bad News: Cant divide by zero')

except IndexError:
    print('Bad News: Index out of range')

finally:
    print('Good News: The code did not crash and kept on running!')