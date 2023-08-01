# let's say we want to find the sum of a list of numbers
# and we want to use recursion to do it


numbers = [10, 20, 30, 40, 50]
# [1] + sum([2,3,4,5])


# none recursive way
def sum_list(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

# recursively 
# there's always a base case which is in this case, an empty list or a list of 
# one element 

def recursive_sum(numbers):
    if len(numbers) == 0:
        return 0
    elif len(numbers) == 1:
        return numbers[0]
    else:
        # it's the sum of a list of 1 elements + sum of the remaining elements
        total = numbers[0] + recursive_sum(numbers[1:])
        return total
        
# print(recursive_sum(numbers))


# # print every element in the list 
def print_element(numbers):
    # l = len(numbers)
    # print(l)
    # for i in range(l):
    #     print(numbers[i])
    for n in numbers:
        print(n)

#print(nonrecursive_reverse(numbers))
# print_element(numbers)

def reverse_list(nubmers):
    l = len(numbers)
    r = reversed(range(l))
    for n in r:
        print(numbers[n])
    return l

def reverse_list_recu(numbers):
    if len(numbers) == 0 or len(numbers) == 1:
        return numbers
    else:
        sublist = numbers[1:]
        sublist_reversed = reverse_list_recu(sublist)
        sublist_reversed.append(numbers[0])
        return sublist_reversed
    
print(reverse_list_recu(numbers))
