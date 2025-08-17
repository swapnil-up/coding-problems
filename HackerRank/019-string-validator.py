if __name__ == '__main__':
    s = input()
    alnum = False
    alpha = False
    digit = False
    lower = False
    upper = False
    for char in s:
        if char.isalnum():
            alnum = True
        if char.isalpha():
            alpha = True
        if char.isdigit():
            digit = True
        if char.islower():
            lower = True
        if char.isupper():
            upper = True
        
    print(alnum)
    print(alpha)
    print(digit)
    print(lower)
    print(upper)


# using a enerator would've been better
# checks = [
#     str.isalnum,
#     str.isalpha,
#     str.isdigit,
#     str.islower,
#     str.isupper
# ]

# if __name__ == '__main__':
#     s = input()
#     for check in checks:
#         print(any(check(c) for c in s))
