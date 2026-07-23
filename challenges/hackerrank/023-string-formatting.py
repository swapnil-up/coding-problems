def print_formatted(number):
    list=[]
    for i in range(number):
        width = len(bin(number)) -2
        print(f"{i+1:>{width}} {i+1:>{width}o} {i+1:>{width}X} {i+1:>{width}b}")

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)