if __name__ == '__main__':
    n = int(input())
    s = set(map(int, input().split()))
    N = int(input())

    for _ in range(N):
        command = input().split()
        if command[0] == 'pop':
            if s:
                s.pop()
        elif command[0] == 'remove':
            if len(command) == 2 and int(command[1]) in s:
                s.remove(int(command[1]))
        elif command[0] == 'discard':
            if len(command) == 2:
                s.discard(int(command[1]))

    print(sum(s))
