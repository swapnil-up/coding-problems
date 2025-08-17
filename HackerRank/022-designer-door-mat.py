# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == '__main__':
    n, m = map(int, input().split())

    # Top 
    for i in range(1, n, 2):
        print(('.|.' * i).center(m, '-'))

    # Middle
    print('WELCOME'.center(m, '-'))

    # Bottom 
    for i in range(n-2, 0, -2):
        print(('.|.' * i).center(m, '-'))
