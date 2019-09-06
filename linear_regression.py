import matplotlib.pyplot as plt
import pylib
import sys
import argparse
import time


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
    mileage = []
    price = []
    mileage += [i[0] for i in tab]
    price += [i[1] for i in tab]
    return mileage, price

def plot_D(mileage, price):
    plt.plot(mileage, price, 'x')

def plot_F(theta0, theta1, estimate_price):
    plt.plot([i for i in range(0, 240000, 10)], [estimate_price(i) for i in range(0, 240000, 10)])


def stop_condition(theta0, theta1, oldtheta0, oldtheta1):
    D0 = abs(theta0 - oldtheta0)
    D1 = abs(theta1 - oldtheta1)
    return D0 + D1 > 0.00001


def update_thetas(theta0, theta1, mileage, price, estimate_price):
    l = len(mileage)
    tmptheta0 = 0.001 * (1/l) * sum([estimate_price(mileage[i]) - price[i] for i in range(l)])
    tmptheta1 = 0.0000000000001 * (1/l) * sum([mileage[i] * (estimate_price(mileage[i]) - price[i]) for i in range(l)])
    return theta0 - tmptheta0, theta1 - tmptheta1


def error(theta0, theta1, estimate_price, mileage, price):
    l = len(price)
    return (1/l) * sum([abs(estimate_price(mileage[i]) - price[i]) for i in range(l)])


def run(filename, plot_data, plot_function, show_error):

    mileage, price = file_to_output(filename, plot_data)
    estimate_price = lambda x : theta0 + theta1 * x

    theta0, theta1 = 0, 0
    oldtheta0, oldtheta1 = 1, 1
    while (stop_condition(theta0, theta1, oldtheta0, oldtheta1)):
        oldtheta0, oldtheta1 = theta0, theta1
        theta0, theta1 = update_thetas(theta0, theta1, mileage, price, estimate_price)

    if plot_function == "yes" or plot_data == "yes":
        plt.clf()
        plt.xlabel("mileage")
        plt.ylabel("price")
        if plot_data == "yes":
            plot_D(mileage, price)
        if plot_function == "yes":
            plot_F(theta0, theta1, estimate_price)
        plt.show()

    if show_error == "yes":
        print("the mean of the error of the prediction is " + str(error(theta0, theta1, estimate_price, mileage, price)))

    with open ("thetas.txt", 'w') as f:
        f.write(str(theta0) + " " + str(theta1))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", type=str, help="Path to the csv file to train")
    parser.add_argument("--ShowData", "-d", type=str, help="Plot of data in the csv file (yes or no, default yes)", default="yes")
    parser.add_argument("--ShowFunction", "-f", type=str, help="Plot the linear function found after the training (yes or no, default yes)", default="yes")
    parser.add_argument("--ShowError", "-e", type=str, help="Show the mean error of the prediction (yes or no, default yes)", default="yes")

    args = parser.parse_args()
    if not pylib.check_file(args.filename):
        sys.exit("CSV file not found")
    if args.ShowData != "no" and args.ShowData != 'yes':
        sys.exit("Bad argument regarding the plot of data")
    if args.ShowFunction != "no" and args.ShowFunction != 'yes':
        sys.exit("Bad argument regarding the plot of the function")
    if args.ShowError != "no" and args.ShowError != "yes":
        sys.exit("Bad argument regarding the mean of the error of the prediction")

    run(args.filename, args.ShowData, args.ShowFunction, args.ShowError)
