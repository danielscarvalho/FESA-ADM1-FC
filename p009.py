import random

lst = range(100)

file = open("info.csv","w")

for val in lst:
    file.write(str(val) \
    + ";" \
    + str(random.randint(-100,100)) \
    + ";" \
    + str(random.random() * 1000) \
    + ";" \
    + str(random.choice(["Gold","Silver","Silver","Perl","Perl","Perl","Perl"])) \
    + "\n")

file.close()