#!/usr/bin/env python3
from EditDistance import EditDist


def main():
    print("Enter two words:")
    word1 = input("Word #1: ")
    word2 = input("Word #2: ")
    myEditDist = EditDist(word1, word2)
    myEditDist.calculate()
    print("\nEdit Distance Matrix:")
    myEditDist.printDistanceMatrix()
    print(f"\nEdit Distance = {myEditDist.getEditDistance()}")
    print("\nAlignment:")
    myEditDist.printAlignment()
    return


if __name__ == "__main__":
    main()