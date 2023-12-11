with open ("input.txt", "r") as f:
    sum=0
    for line in f:
        line = line.strip()
        line = line.split(":")
        game_num = int(line[0].split(" ")[1])
        line = line[1].strip()
        line = line.split(" ")