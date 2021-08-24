import random
import string


chars = string.ascii_letters + string.digits

print(chars)
print(str(string.printable))
# def generateCode(count, length):
#     for x in count:
#         code = ""
#         for y in range(count):
#             print("range(count)" +range(count))
#             code = code + random.choice(chars)
#         yield code
#
# if __name__ == '__main__':
#       codes = generateCode(100, 20)
#       for code in codes:
#           print(code)