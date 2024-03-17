import numpy as np

class NanoReplicatorArray:
    def __init__(self, dimensions):
        self.dimensions = dimensions
        self.array = np.zeros(dimensions, dtype=int)

    def replicate(self, structure, position):
        if not self.is_valid_position(position):
            raise ValueError("Invalid position")

        for i in range(len(structure)):
            for j in range(len(structure[i])):
                self.array[position[0] + i][position[1] + j] = structure[i][j]

    def is_valid_position(self, position):
        return (0 <= position[0] < self.dimensions[0] and
                0 <= position[1] < self.dimensions[1])

    def get_array(self):
        return self.array

# Example usage:

# Define a structure to replicate
structure = [[1, 1, 1],
             [1, 0, 1],
             [1, 1, 1]]

# Create a Nano-Replicator Array with dimensions 10x10
nano_replicator_array = NanoReplicatorArray((10, 10))

# Replicate the structure at position (2, 2)
nano_replicator_array.replicate(structure, (2, 2))

# Print the resulting array
print(nano_replicator_array.get_array())
