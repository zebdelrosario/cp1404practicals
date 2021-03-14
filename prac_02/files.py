# 1.
# user_name = str(input("Enter name: "))
# out_file = open('name.txt', 'w')
# print(user_name, file=out_file)

# 2.
# in_file = open('name.txt', 'r')
# print("Your name is {}".format(in_file.read()))

# 3.
# result = 0
# in_file = open('numbers.txt', 'r')
# for line in in_file.readlines()[:2]:
#     line.strip('\n')
#     result += int(line)
# print(result)

# 4.
# result = 0
# in_file = open('numbers.txt', 'r')
# for line in in_file.readlines():
#     line.strip('\n')
#     result += int(line)
# print(result)