"""Write a recursive function to determine if a string is a palindrome or not,
assuming the string consists of only uppercase letters."""
# word = "APPLE"
# word_1="abba"
# def palindrome(word):
#   if len(word) <= 1:
#     return True

#   elif word[0] == word[-1]:
#     return palindrome(word[1:-1])

#   else:
#     return False


# print(palindrome(word_1))


"""Write a recursive function to determine whether or not a list is in numerical
order from smallest to largest, assuming there are no repeated numbers."""

# list_1 = [1, 2, 3, 4, 5]
# list_2 = [1, 3, 2, 5, 7]

# def check(example):
#   if len(example) <= 1:
#     return True

#   else:
#     return example[0] < example[1] and check(example[1:])

# print(check(list_1))
# print(check(list_2))

"""Write a recursive function that returns the sum of the digits of a positive integer."""

# def sum_digits(number):
#   if number / 10 < 1:
#     return number

#   else:
#     return number % 10 + sum_digits((number - (number % 10))/10)

# print(sum_digits(20034))

"""Write a recursive function that doubles each element of a list by creating a
new list, not doubling the list in place."""

# def double_with_new(example):
#   a = example[:]

#   if len(example[:]) <= 1:
#     return [a[0] * 2]

#   else:
#     return [a[0] * 2] + double_with_new(a[1:])

# given_list = [1, 2, 3, 4]
# print(double_with_new(given_list))
# print(given_list)

"""● Write a recursive function that counts how many E’s there are in a string."""

# def find_e(example):
#   if len(example) <= 1:
#     if example == "e":
#       return 1
#     else:
#       return 0

#   elif example[0] == "e":
#     return 1 + find_e(example[1:])

#   elif example[0] != "e":
#     return find_e(example[1:])

# print(find_e("apples"))
# print(find_e("elephant"))

"""Write a recursive function that removes the E’s in a string."""

# def remove_e(example):
#   example = example.upper()
#   if len(example) <= 1:
#     if example == "E":
#       return ""
#     else:
#       return example

#   elif example[0] == "E":
#     return "" + remove_e(example[1:])

#   elif example[0] != "E":
#     return example[0] + remove_e(example[1:])

# print(remove_e("Elephant"))
# print(remove_e("elemental"))

"""Write a recursive function that takes in a string, returning True if there are any
instances of the same letter consecutively, false otherwise."""

# def consecutive_letters(example):
#   if len(example) <= 1:
#     return False

#   else:
#     return example[0] == example[1] or consecutive_letters(example[1:])

# # what does or do

"""Write a recursive function that takes a longer string a and shorter string b,
returning True if b is a substring of a. Only use len, slicing and =="""

# def b_in_a(a, b):

#   length = len(b)

#   if len(a) == len(b):
#     if b in a:
#       return True
#     else:
#       return False


#   else:
#     return b in a[:length] or b_in_a(a[1:], b)

# print(b_in_a("esin", "in"))

# """Write a function that takes three inputs, string, character 1 and character 2.
# Replace all instances of character 1 with character 2."""

# def replace_char(userinput, c1, c2):
#   if len(userinput) == 1:
#     if c1 in userinput:
#       return c2
#     elif c1 not in userinput:
#       return userinput

#   else:
#     if c1 in userinput[0]:
#       return c2 + replace_char(userinput[1:], c1, c2)
#     else:
#       return userinput[0] + replace_char(userinput[1:], c1, c2)

# print(replace_char("translate", "t", "e"))



# def power(a, b):
#   if b == 0:
#     return 1

#   else:
#     return a * power(a, b-1)

# print(power(4, 4))


# def create_list(n):
#   if n == 1:
#     return [1]

#   return create_list(n-1) + [n] 

# print(create_list(4))

# def fibonacci(n):
#   if n == 0:
#     return 1
#   elif n == 1:
#     return 1

#   return fibonacci(n-1) + fibonacci(n-2)

# def insert(l, n):
#   if len(l) == 0:
#     return []

#   else:
#     if l[0] < n and l[1] > n :
#       return [l[0]] + [n] + insert(l[1:], n)
#     else:
#       return [l[0]] + insert(l[1:], n)

# print(insert([1, 2, 4, 5], 3))


# def merge_lists(a, b):
#   if not a:
#     return b

#   elif not b:
#     return a

#   else:
#     return [a[0]] + [b[0]] + merge_lists(a[1:], b[1:])

# print(merge_lists([1, 2, 3, 4, 5], [6, 7, 8]))
# print(merge_lists([1, 2, 3], [1, 2, 3, 4, 5])) 

# def substring(inputted, sub, amount):
#   if not inputted:
#     return 0

#   length = len(sub)

#   if inputted[:length] == sub:
#     return 1 + substring(inputted[1:], sub)

#   elif inputted[:length] != sub:
#     return 0 + substring(inputted[1:], sub)

# def group_sum(start, nums, result):
#   if not nums:
#     return []

#   parsing = nums[:]
#   index = 0

#   if parsing[index] + parsing[index + 1] != result:
#     return [parsing[index]] + group_sum([parsing[1:]])


# def find_11s(ints_list):
#   if len(ints_list) == 0:
#     return 0

#   elif ints_list[0] == 11:
#     return 1 + find_11s(ints_list[1:])

#   elif ints_list [0] != 11:
#     return 0 + find_11s(ints_list[1:])

# print(find_11s([1, 2, 4, 5, 6, 11, 22, 3, 4, 5, 11, 11, 1, 1, 1, 1, 11, 2, 3, 4, 11]))

# def power_N(base, n):
#   if n == 0:
#     return 1

#   else:
#     return base * power_N(base, n-1)

# print(power_N(2, 3))

# def change_pi(pi_string):
#   if len(pi_string) < 4:
#     return pi_string

#   elif pi_string[0:4] == "3.14":
#     return "pi" + change_pi(pi_string[4:])

#   else:
#     return pi_string[0] + change_pi(pi_string[1:])

# print(change_pi("3.14.14.3.14.3.14.3.14.12323432432423.14"))

# def paren_bit(input_str):
#   if len(input_str) == 0:
#     return ""

#   elif input_str[0] != "(" or input_str[-1] != ")":
#     if input_str[0] != "(":
#       return paren_bit(input_str[1:])

#     elif input_str[-1] != ")": 
#       return paren_bit(input_str[0:-1])

#   else:
#     return input_str

# print(paren_bit("abc(123)abc"))

# def times_ten(example):
#   if len(example) < 2:
#     return False

#   elif example[1] == example[0] * 10:
#     return True

#   else:
#     return times_ten(example[1:])

# def bunny_ears(ears):
#   if ears == 0:
#     return 0

#   else:
#     return 2 + bunny_ears(ears-1)

def count_hi(example):
  if len(example) < 3:
    return 0

  elif example[0:2] == "hi":
    return 1 + count_hi(example[2:])

  elif example[1:3] == "hi" and example[0] == "x":
    return 0 + count_hi(example[3:])

  else: 
    return 0 + count_hi(example[1:])

print(count_hi("hitherehellohihi"))