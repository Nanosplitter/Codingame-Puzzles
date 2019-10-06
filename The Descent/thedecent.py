while True:
    highest = 0
    m = 0
    for i in range(8):
        mountain_h = int(input())
        if mountain_h > highest:
            highest = mountain_h
            m = i
    print(m)