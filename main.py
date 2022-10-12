#!/usr/bin/env python3

class EditDist:
    def __init__(self, word1: str, word2: str):
        self.word1 = word1
        self.word2 = word2
        self.matrix = [len(word1)][len(word2)]


def main():
    word1 = input("Enter word #1: ")
    word2 = input("Enter word #2: ")
    print(f"Word 1 is: {word1}")
    print(f"Word 2 is: {word2}")
    return


if __name__ == "__main__":
    main()
