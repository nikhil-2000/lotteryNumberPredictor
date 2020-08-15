from operator import itemgetter

res = open('lotteryData/649.csv', 'r', encoding='utf-8-sig')
splitResults = res.read().split('\n')
splitResults.pop()
for i in range(len(splitResults)):
    splitResults[i] = splitResults[i].split(',')

nums = dict([(i, 0) for i in range(0, 50)])

rows = len(splitResults)
cols = len(splitResults[0])

for i in range(1, rows):
    for j in range(4, cols):
        stringNum = splitResults[i][j]
        if stringNum != '':
            drawnNum = int(splitResults[i][j])
            nums[drawnNum] += 1

filledNums = [(k, v) for k, v in nums.items()]
filledNums.sort(key=lambda x: x[1])

for i in range(7):
    print("Number: %d, Count: %d" % filledNums.pop())
