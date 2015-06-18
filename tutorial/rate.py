__author__ = 'sheldon'
zero_num = 0
num = 0
result = open('rate.txt', 'wb')
for i in range(0, 1000):
    open_file = 'goose/' + str(i) + '.txt'
    f = open(open_file, 'r')
    string = f.read()
    f.close()
    if len(string) == 0:
        zero_num += 1
    else:
        num += 1
result.write(str(zero_num) + '/' + str(zero_num + num))
result.write('\n')
zero_num = 0
num = 0
for i in range(0, 1000):
    open_file = 'boilerpipe/' + str(i) + '.txt'
    f = open(open_file, 'r')
    string = f.read()
    f.close()
    if len(string) == 0:
        zero_num += 1
    else:
        num += 1
result.write(str(zero_num) + '/' + str(zero_num + num))
result.write('\n')
zero_num = 0
num = 0
for i in range(0, 1000):
    open_file = 'dragnet/' + str(i) + '.txt'
    f = open(open_file, 'r')
    string = f.read()
    f.close()
    if len(string) == 0:
        zero_num += 1
    else:
        num += 1
result.write(str(zero_num) + '/' + str(zero_num + num))
result.write('\n')
result.close()
