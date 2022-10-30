#!/usr/bin/env python3
from EditDistance import EditDist


def main():
    print("Enter two words:")
    word1 = input("Word #1: ")
    word2 = input("Word #2: ")
    my_edit_dist = EditDist(word1, word2)
    my_edit_dist.calculate()
    print("\nEdit Distance Matrix:")
    my_edit_dist.print_distance_matrix()
    print(f"\nEdit Distance = {my_edit_dist.get_editdistance()}")
    print("\nAlignment:")
    my_edit_dist.print_alignment()
    return


if __name__ == "__main__":
    main()
