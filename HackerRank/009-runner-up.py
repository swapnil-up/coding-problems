if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    runner = sorted(set(arr), reverse=True)
    print(runner[1])
