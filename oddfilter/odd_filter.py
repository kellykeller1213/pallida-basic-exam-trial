# Create a function that takes a list as a parameter,
# and returns a new list with every odd number from the orignal list
# example: [1, 2, 3, 4, 5] should produce [1, 3, 5]

#print(odd_filter([1, 2, 3, 4, 5]))  # should print [1, 3, 5]

number = list(range(1, 100))
odd_list = []

def odd_filter():
    odd_list = number[0::2]
    print(odd_list)
odd_filter()