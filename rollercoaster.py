"""
This program tells a user if they are tall enough to ride a rollercoaster.
"""

def main():
    # Ask user for height in meters. If height is between 1-2 meters, user can ride the rollercoaster.
    height = float(input("Please enter height in meters: "))
    if height < 1 or height > 2:
        print("You can't ride the roller coaster")
    else:
        print("You can ride the roller coaster")


if __name__ == '__main__':
    main()
