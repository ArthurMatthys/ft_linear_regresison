import matplotlib.pyplot as plt
import pylib
import sys
import argparse


def file_to_output(filename, opt):
    with open(filename, 'r') as f:
        top = f.readline().replace("\n", "")
        top = top.split(',')
        t = f.read()
        if t[-1] == '\n':
            t = t[:-1]
    t = t.split('\n')
    tab =[]
    for i in t:
        i = i.split(',')
        tab.append([float(i[0]), float(i[1])])
    t1 = []
    t2 = []
    t1 += [i[0] for i in tab]
    t2 += [i[1] for i in tab]
    if opt == "yes":
        plt.clf()
        plt.plot(t1, t2, 'x')
        plt.xlabel(top[0])
        plt.ylabel(top[1])
        plt.show()
    return t1,t2


def run(filename, plot_data, plot_function):

    t1,t2 = file_to_output(filename, plot_data)

    print(t1)
    print(t2)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", type=str, help="Path to the csv file to train")
    parser.add_argument("--ShowData", "-d", type=str, help="Plot of data in the csv file (yes or no, default yes)", default="yes")
    parser.add_argument("--ShowFunction", "-f", type=str, help="Plot the linear function found after the training (yes or no, default yes)", default="yes")

    args = parser.parse_args()
    if not pylib.check_file(args.filename):
        sys.exit("CSV file not found")
    if args.ShowData != "no" and args.ShowData != 'yes':
        sys.exit("Bad argument regarding the plot of data")
    if args.ShowFunction != "no" and args.ShowFunction != 'yes':
        sys.exit("Bad argument regarding the plot of the function")

    run(args.filename, args.ShowData, args.ShowFunction)

