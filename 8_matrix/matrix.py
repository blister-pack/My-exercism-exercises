from re import split


class Matrix:
    def __init__(self, matrix_string):
        self.rows = []
        self.columns = []

        # gotta make it work for matrixes with single rows or columns
        # think I wrote the code wrong because I assumed the last line also had a /n
        # gotta make this work in a different way

        # TODO make it write rows
        # TODO make it write columns
        # TODO make it detect the end of the string and stop

        rows = matrix_string.split("\n")
        for i in rows:
            split_row = i.split(" ")
            make_int = list(map(int, split_row))
            self.rows.append(make_int)

        def convert_into_list_of_lists(l):
            aux = []
            for member in l:
                aux.append([member])
            return aux

        self.columns.append(
            self.rows[0]
        )  #  this lines gives the column heads from the rows
        self.columns = convert_into_list_of_lists(self.columns[0])

        for index in range(1, len(self.rows)):
            for ind, colmn_number in enumerate(self.rows[index]):
                self.columns[ind].append(colmn_number)

    #  I need these methods to return column and rows in a [] list format

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


matrixF = Matrix(
    "1 2\n10 20"
)  #  this list causes problems because it has values with multiple digits


print(matrix.rows)
print(matrix.columns)
print(matrix.row(2))
print(matrixF.row(2))
