# Problem Statement
# Fill out the function get_last_element(lst) which takes in a list lst as a parameter and prints the last element in the list. The list is guaranteed to be non-empty, but there are no guarantees on its length.

# Starter Code

# def get_last_element(lst): """ Prints the last element of the provided list. """

# # Takes the length of the list and minuses 1 since they are zero-indexed (we start counting at 0)
# print(lst[len(lst) - 1])

# # The line below works too!!
# # print(lst[-1]) 

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list[len(list) - 4])
# print(list[-1])