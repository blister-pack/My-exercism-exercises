class Matrix:
    def __init__(self, matrix_string):
        self.rows = []
        self.columns = []

        new_row = ""
        index = -1
        for i in matrix_string:
            if i == "\n":
                self.rows.append(new_row)
                new_row = ""
                index = -1
            else:
                new_row = new_row + i
                if i != " ":
                    index += 1
                    try:
                        self.columns[index] = self.columns[index] + (
                            " " + i
                        )  #  not sure why this isn't working as expected
                    except:
                        self.columns.append(i)

    def row(self, index):
        #  this method returns a row with the selected index
        return self.rows[index]

    def column(self, index):
        #  this method returns a column with the selected index
        return self.columns[index]


# -----------------------------------------------------------------------------------------
matrixz = Matrix("1")
matrix = Matrix("9 8 7\n5 3 2\n6 6 7\n")
print(matrix.rows)
print(matrix.columns)
print(matrix.row(2))
