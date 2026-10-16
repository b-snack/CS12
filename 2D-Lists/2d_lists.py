# # new_list = []
# # newer_list= [[1, 2, 3], [1, 2, 3, 4], ["a", "b"]]

# # for i in newer_list:
# #   for _ in i:
# #     new_list.append(_)

# # print(new_list)

# new_list = []
# newer_list= [[1, 2, 3], [1, 2, 3, 4]]

# for i in newer_list:
#   summ = 0
#   for _ in i:
#     summ += _

#   new_list.append(summ)

# print(new_list)

# total = 0
# for i in newer_list:
#   for _ in i:
#     total += _

# print(total)


final= []
new_list = []
counter = 0

for i in range(1, 26):

  new_list.append(i)
  if len(new_list) == 5:
    final.append(new_list)
    new_list = []
  else:
    pass


  final.append(new_list)
print(final)