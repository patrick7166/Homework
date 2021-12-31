ans = input()
leng = len(ans)
countA = 0
countB = 0
while countA != leng:
    countA = 0
    countB = 0
    arr=[10]
    arr = [0 for i in range(10)]
    out = False
    ges = input('Enter your guess:\n')
    if leng != len(ges):
        print('Invalid, please enter your guess again:\n')
        continue
    for i in range(leng):
        if not ges.isnumeric():
            print('Invalid, please enter your guess again:\n')
            out = True
            break
        arr[int(ges[i])] += 1
        if arr[int(ges[i])] > 1:
            print('Invalid, please enter your guess again:\n')
            out = True
           
    if out:
        continue
    for i in range(leng):
        if ges[i] == ans[i]:
            countA += 1
        if ges[i] in ans:
            countB += 1

    countB -= countA
    if countA == leng:
        print('Your guess is ', ges, '; the result is ', countA,'A', countB, 'B\nFinish!!!\n', sep='')
    else:
        print('Your guess is ', ges, '; the result is ', countA,'A', countB, 'B\n', sep='')
