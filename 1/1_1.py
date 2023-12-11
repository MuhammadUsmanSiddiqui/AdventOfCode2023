def first_num(line):
    for i in range(len(line)):
        if line[i].isdigit():
            return [i, line[i]]

with open("input.txt", 'r') as f:
    sum=0
    for line in f:
        dig_1 = first_num(line)[1]
        if first_num(line[::-1])[0] != dig_1[0]:
            dig_2 = first_num(line[::-1])[1]
            sum += int(dig_1+dig_2)
        else:
            sum += int(dig_1)

print(sum)

# correct answer: 54630