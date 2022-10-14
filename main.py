#!/usr/bin/env python3
from EditDistance import EditDist


def main():
    word1 = input("Enter word #1: ")
    word2 = input("Enter word #2: ")
    meme = EditDist(word1, word2)
    meme.calculateEditDistance()
    meme.printMatrix()
    meme.printAlignment()
    return


if __name__ == "__main__":
    main()