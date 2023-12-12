REDLIMIT = 12
GREENLIMIT = 13
BLUELIMIT = 14
FLAG = False

with open ("input.txt", "r") as f:
    sum=0
    for line in f:
        line = line.strip().split(":")
        game_num = int(line[0].split(" ")[1])
        sets_in_game = line[1].strip().split(";")
        for set in sets_in_game:
            red, green, blue = 0, 0, 0
            FLAG = False
            cols = set.strip().split(",")
            for col in cols:
                col=col.strip()
                if "red" in col:
                    red += int(col.split(" ")[0])
                if "green" in col:
                    green += int(col.split(" ")[0])
                if "blue" in col:
                    blue += int(col.split(" ")[0])
                if red > REDLIMIT or green > GREENLIMIT or blue > BLUELIMIT:
                    FLAG = True
                    break
            if FLAG:
                break
        if not FLAG:
            print(game_num)
            sum += game_num

print(sum)
            