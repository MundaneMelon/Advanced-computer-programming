import numpy as np

class OBJ:
    def __init__(self, filename):
        self.vertices = []
        self.faces = []
        self.load(filename)

    def load(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                if line.startswith('v '):
                    vertex = list(map(float, line.split()[1:4]))
                    self.vertices.append(vertex)
                elif line.startswith('f '):
                    face = [int(vertex.split('/')[0]) - 1 for vertex in line.split()[1:]]
                    self.faces.append(face)

        self.vertices = np.array(self.vertices)
        self.faces = np.array(self.faces)
