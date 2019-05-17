import matplotlib.pyplot as plt
import pylib


def file_to_output(str, opt):
    if not pylib.check_file(str):
        print("This file does not exist")
        exit()
    else:
        f = open(str, 'r')
        top = f.readline()[:-1]
        top = top.split(',')
        t = f.read()
        if t[-1] == '\n':
            t = t[:-1]
        f.close()
        t = t.split('\n')
        tab =[]
        for i in t:
            i = i.split(',')
            tab.append([float(i[0]), float(i[1])])
        print (tab)
        t1 = []
        t2 = []
        t1 += [i[0] for i in tab]
        t2 += [i[1] for i in tab]
        if opt:
            plt.clf()
            plt.plot(t1, t2, 'x')
            plt.xlabel(top[0])
            plt.ylabel(top[1])
            plt.show()
        return t1,t2


def handle_arg():
    file = str(input())
    print("Would you like to see the data on a graph ? (y) or (n)")
    while 1:
        i = str(input())
        if i == "y":
            viz = 1
            break
        elif i == "n":
            viz = 0
            break
        else:
            print("Please, enter yes (y) or no (n)")

    t1,t2 = file_to_output(file, viz)


def test():
    t = [1, 2, 3, 4, 5]
    for i in range(len(t)):
        t[i] += 1
    print (t)

test()
#handle_arg()
