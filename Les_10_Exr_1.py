class Matrix:
    def __init__(self, mylist):
        self.mylist = mylist

    def __str__(self):
        res = []
        for el in self.mylist:
            _el = ''.join(str(el))
            res.append(_el)
        return '\n'.join(res)

    def __add__(self, other):
        _matrix = []
        if len(self.mylist) == len(other.mylist):
            for i in range(len(self.mylist)):
                _matrix.append([])
                for j in range(len(self.mylist[i])):
                    _matrix[i].append(self.mylist[i][j] + other.mylist[i][j])
                    newnew_matrix = Matrix(_matrix)

        return newnew_matrix


new_matrix = Matrix([[1, 2, 4, 12, 66], [2, 3, 5, 12, 66]])

old_matrix = Matrix([[3, 5, 6, 100, 159], [6, 7, 8, 34, 33]])

new1_matrix = new_matrix + old_matrix

print(new1_matrix)
