#!/usr/bin/python3
"""2D matrix rotation module.
"""


def rotate_2d_matrix(matrix):
   """
    Rotate a 2D matrix 90 degrees clockwise.
    """
     n = len(matrix)
    # Iterate through each layer of the matrix
    for layer in range(n // 2):
        first = layer
        last = n - 1 - layer
        # Iterate through each element in the current layer
        for i in range(first, last):
            # Store the current element in a temporary variable
            temp = matrix[layer][i]
            # Move values from right to top
            matrix[layer][i] = matrix[-i - 1][layer]
            # Move values from bottom to right
            matrix[-i - 1][layer] = matrix[-layer - 1][-i - 1]
            # Move values from left to bottom
            matrix[-layer - 1][-i - 1] = matrix[i][-layer - 1]
            # Move values from top to left
            matrix[i][-layer - 1] = temp
