#!/usr/bin/python3

class MyList(list):
    def print_sorted(self):
        """
        Prints the list in sorted (ascending) order.
        Args:
            None
        Returns:
            None
        """
        # Implementation of a simple sorting algorithm (Bubble Sort)
        for i in range(len(self)):
            for j in range(i + 1, len(self)):
                # Compare adjacent elements and swap if out of order
                if self[i] > self[j]:
                    self[i], self[j] = self[j], self[i]

        # Print the sorted list
        # print(selfi)

        return self
