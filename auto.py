import os
from config import NAME, STRINGSIZE


def gen_num(a):
    s = ""
    for i in a:
        if i in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
            s += i
        else:
            return s


with open("input.txt", "r", encoding="UTF8") as file:
    tasks = file.readlines()

for i in range(len(tasks)):
    tasks[i] = tasks[i].split("\n")[0]

buf = ""
tasks_list = []
numeric = []
for it in tasks:
    if ")" in it[:4] and it[0] in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
        n = gen_num(it)
        tasks_list.append(buf)
        buf = ""
        numeric.append(n)
    buf += it
tasks_list.append(buf)
PATH = os.getcwd() + "\\" + NAME + " " + str(numeric[0]) + "-" + str(numeric[-1])
os.mkdir(PATH)
file_txt = open(f"{PATH}\\{NAME} {numeric[0]}-{numeric[-1]}.txt", "w")
file_txt.close()
for i in range(len(numeric)):
    file_task = open((PATH + "\\" + numeric[i] + ".py"), "w", encoding="UTF8")
    file_task.write("'''")
    file_task.write("\n")
    count = 0
    for i in tasks_list[i + 1].split():
        file_task.write(i + " ")
        count += len(i) + 1
        if count >= STRINGSIZE:
            count = 0
            file_task.write("\n")
    file_task.write("\n")
    file_task.write("'''")
    file_task.write("\n")
    file_task.write("\n")
    file_task.close()
