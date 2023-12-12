import math

with open ("input.txt", "r") as f:
    prod=0
    for line in f:
        line = line.strip().split(":")
        game_num = int(line[0].split(" ")[1])
        sets_in_game = line[1].strip().split(";")
        red, green, blue = 0,0,0
        for set in sets_in_game:
            FLAG = False
            cols = set.strip().split(",")
            for col in cols:
                col=col.strip()
                if "red" in col:
                    if int(col.split(" ")[0])>red:
                        red = int(col.split(" ")[0])
                if "green" in col:
                    if int(col.split(" ")[0])>green:
                        green = int(col.split(" ")[0])
                if "blue" in col:
                    if int(col.split(" ")[0])>blue:
                        blue = int(col.split(" ")[0])
        prod += red*green*blue

print(prod)
            