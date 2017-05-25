class Vector:
    def __init__(self, *args):
        self.dimensions = []
        for value in args:
            if type(value) == int:
                self.dimensions.append(value)
            if type(value) == list:
                for element in value:
                    self.dimensions.append(element)

    def __str__(self):
        return "Vector: " + str(self.dimensions)

    def add_vectors(vector1, vector2):
        output = []
        for i in range(len(vector1.dimensions)):
            output.append(vector1.dimensions[i] + vector2.dimensions[i])
        return output

    def mult_vectors(vector1, vector2):
        product = 0
        for i in range(len(vector1.dimensions)):
            product += (vector1.dimensions[i] * vector2.dimensions[i])
        return product

    def sub_vectors(vector1, vector2):
        output = []
        for i in range(len(vector1.dimensions)):
            output.append(vector1.dimensions[i] - vector2.dimensions[i])
        return output


class Matrix:
    def __init__(self, *args):
        self.matrix = []
        for value in args:
            self.matrix.append(value)

    def __str__(self):
        for x in range(len(self.matrix)):
            print str(self.matrix[x])

    def mult_matrix(m1, m2):



def main():
    matrix1 = Matrix([1, 2, 3], [1, 2, 3], [1, 2, 3])
    print matrix1


if __name__ == "__main__":
    main()