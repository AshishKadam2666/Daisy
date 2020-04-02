# Taking user inputs:
x = input('Enter value of x: ')
y = input('Enter value of y: ')

# creating a temporary variable to swap the values
temp = x
x = y
y = temp

print('The value of x after swapping: {}'.format(x))
print('The value of y after swapping: {}'.format(y))
