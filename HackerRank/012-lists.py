if __name__ == '__main__':
    N = int(input())
    my_list = []
    
    for _ in range(N):
        command, *args = input().split()
        if(command=="insert"):
            my_list.insert(int(args[0]), int(args[1]))
        elif(command=="remove"):
            my_list.remove(int(args[0]))
        elif(command=="append"):
            my_list.append(int(args[0]))
        elif(command=="print"):
            print(my_list)
        else:
            getattr(my_list, command)(*map(int, args))
