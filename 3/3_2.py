my_dic={}

def adjacent_symbol_present(a,b,n,lines):
    for i in range(a-1, a+2):
        for j in range(b-1, b+1+n):
            if i<0 or i>=len(lines) or j<0 or j>=len(lines[i]):
                continue
            if (not lines[i][j].isdigit()) and (lines[i][j] != "."):
                if lines[i][j]=="*":
                    if (i,j) in my_dic:
                        my_dic[(i,j)].append(lines[a][b:b+n])
                    else:
                        my_dic[(i,j)] = [lines[a][b:b+n]]
                return True
    return False

with open("input.txt", "r") as f:
    sum=0
    lines = f.readlines()
    lines = [line.strip() for line in lines]
    for i in range(len(lines)):
        n=1
        j=0
        while j<len(lines[i]):
            n=1
            if lines[i][j].isdigit():
                while lines[i][j+n].isdigit():
                    n+=1
                    if j+n>=len(lines[i]):
                        break
                if adjacent_symbol_present(i,j,n,lines):
                    sum += int(lines[i][j:j+n])
            j+=n

new_dic = {}
for key in my_dic:
    if len(my_dic[key])>1:
        new_dic[key] = [int(my_dic[key][0]), int(my_dic[key][1])]

this = 0
for key in new_dic:
    this = this + (int(new_dic[key][0])*int(new_dic[key][1]))
print(this)