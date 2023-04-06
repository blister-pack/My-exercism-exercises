class Matrix:
    def __init__(self, matrix_string):
        self.rows = []
        self.columns = []

        # gotta make it work for matrixes with single rows or columns
        # think I wrote the code wrong because I assumed the last line also had a /n
        # gotta make this work in a different way
        """
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
        """

        # TODO make it write rows
        # TODO make it write columns
        # TODO make it detect the end of the string and stop

        matrix_length = len(matrix_string)
        new_row = ""
        for index_in_row, i in enumerate(matrix_string, start=1):
            if i == "\n":
                self.rows.append(new_row)
                new_row = ""
            elif matrix_length == index_in_row:
                new_row = new_row + i
                self.rows.append(new_row)
            else:
                new_row = new_row + i

        for row in self.rows:
            for index, num in enumerate(row):
                try:
                    self.columns[index].append(num)
                except Exception:
                    self.columns[index] = self.columns[index] + num

    def row(self, index):
        #  this method returns a row with the selected index
        return self.rows[index - 1]

    def column(self, index):
        #  this method returns a column with the selected index
        return self.columns[index - 1]


# -----------------------------------------------------------------------------------------
matrix = Matrix("9 8 7\n5 3 2\n6 6 7")
matrixz = Matrix("1")
matrixa = Matrix("2 3 4")
matrixb = Matrix("5\n6\n7")

print(matrix.rows)
print(matrix.columns)
print(matrix.row(2))
