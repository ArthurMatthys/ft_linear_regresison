import argparse
import sys


def run(filename):
    if filename != None:
        try:
            with open(filename, 'r') as f:
                theta0, theta1 = list(map(lambda x : float(x), f.readline().split(' ')))
        except FileNotFoundError:
            sys.exit("The input file doesn't exist")
    else:
        theta0, theta1 = 0, 0

    estimate_price = lambda x : theta0 + theta1 * x

    print("Give the mileage of the car we need to estimate the price")
    mileage = float(input())
    if mileage < 0:
        sys.exit("Mileage not valid")
    price = estimate_price(mileage)
    if price < 0:
        print("The estimate price is negative, so we will assume the milage is too high to sell the car.")
        print("price = 0")
    else:
        print("The price of the car is : " + str(price))
    return


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--filename", "-f", type=str, help="Path to the theta's file")

    args = parser.parse_args()

    run(args.filename)
