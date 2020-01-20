
with open("spi.txt", 'r') as file:
    for line in file.readlines():
        print(line[line.find('<')+1:line.find('+')])
file.close()