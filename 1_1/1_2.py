dict_of_valid_spellings = {"one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}
dict_of_valid_spellings_rev = {}
for item in dict_of_valid_spellings:
    dict_of_valid_spellings_rev[item[::-1]] = dict_of_valid_spellings[item] 
dict_of_valid_spellings.update(dict_of_valid_spellings_rev)

def first_num(line):
    for i in range(0,len(line)):
        if line[i].isdigit():
            return line[i]
        elif line[i:i+3] in dict_of_valid_spellings:
            return dict_of_valid_spellings[line[i:i+3]]
        elif line[i:i+4] in dict_of_valid_spellings:
            return dict_of_valid_spellings[line[i:i+4]]
        elif line[i:i+5] in dict_of_valid_spellings:
            return dict_of_valid_spellings[line[i:i+5]]
        else:
            continue

with open("input.txt", 'r') as f:
    sum=0
    for line in f:
        dig_1 = first_num(line)
        dig_2 = first_num(line[::-1])
        sum += int(dig_1+dig_2)

print(sum)

# correct answer: 54630