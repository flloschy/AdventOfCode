import time

start = time.perf_counter()
###
endsum = 0
for line in open("./2021/Day8/input.txt"):
    nums = []
    order = {'1': False, '2': False, '3': False, '4': False, '5': False, '6': False, '7': False, '8': False, '9': False, '0': False}
    for num in  line.strip().split(' | ')[0].split(' '):
        le = len(num)
        if le == 2: order['1'] = "".join([str(i) for i in num])
        elif le == 3: order['7'] = "".join([str(i) for i in num])
        elif le == 4: order['4'] = "".join([str(i) for i in num])
        elif le == 7: order['8'] = "".join([str(i) for i in num])
        if order['1'] and order['4'] and order['7'] and order['8']:
            break

    for num in  line.strip().split(' | ')[0].split(' '):
        le = len(num)
        if le == 5:
            if all([bool(i in num) for i in order['4']]) and not order['9']: order['9'] = "".join([str(i) for i in num])
            elif all([bool(i in num) for i in order['1']]) and not order['0']: order['0'] = "".join([str(i) for i in num])
            else: order['6'] = "".join([str(i) for i in num])
        elif le == 6:
            if all([bool(i in num) for i in order['1']]) and not order['3']: order['3'] = "".join([str(i) for i in num])
            elif len([int(x) for x in [bool(i in num) for i in order['4']] if x]) == 3 and not order['5']: order['5'] = "".join([str(i) for i in num])
            else: order['2'] = "".join([str(i) for i in num])

    print(order)
    for num in  line.strip().split(' | ')[1].split(' '):
        if all([bool(i in num) for i in order['0']]): nums.append("0")
        elif all([bool(i in num) for i in order['1']]): nums.append("1")
        elif all([bool(i in num) for i in order['2']]): nums.append("2")
        elif all([bool(i in num) for i in order['3']]): nums.append("3")
        elif all([bool(i in num) for i in order['4']]): nums.append("4")
        elif all([bool(i in num) for i in order['5']]): nums.append("5")
        elif all([bool(i in num) for i in order['6']]): nums.append("6")
        elif all([bool(i in num) for i in order['7']]): nums.append("7")
        elif all([bool(i in num) for i in order['8']]): nums.append("8")
        elif all([bool(i in num) for i in order['9']]): nums.append("9")
    print(nums)
    endsum += int("".join(nums))

print(endsum)
###
print(f"Time Taken: {time.perf_counter()-start}s")