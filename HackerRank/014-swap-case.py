def swap_case(s):
    return s.swapcase()

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)


# if swapcase didn't exist
# def swap_case(s):
#     str = ""
#     for char in s:
#         if char.isupper():
#             str+=char.lower()
#         else:
#             str+=char.upper()
#     return str

# if __name__ == '__main__':
#     s = input()
#     result = swap_case(s)
#     print(result)


# without using a string, but a list instead
# def swap_case(s):
#     str = []
#     for char in s:
#         if char.isupper():
#             str.append(char.lower())
#         else:
#             str.append(char.upper())
#     return ''.join(str)

# if __name__ == '__main__':
#     s = input()
#     result = swap_case(s)
#     print(result)


# converted into a generator function
# def swap_case(s):
#     return ''.join(char.lower() if char.isupper() else char.upper() for char in s)

# if __name__ == '__main__':
#     s = input()
#     result = swap_case(s)
#     print(result)