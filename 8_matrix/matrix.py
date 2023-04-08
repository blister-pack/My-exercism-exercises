from hmac import new


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
        """ 
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
        """

        num_rows = matrix_string.count("\n") + 1
        split_rows = matrix_string.split()
        num_elements_per_row = len(split_rows) / num_rows
        #  need a counter that would make a new row every tine the row has
        #  the right number of elements
        new_row = ""
        end_of_row = 0
        for num in split_rows:
            end_of_row += 1
            if end_of_row == num_elements_per_row:
                new_row += f"{num} "
                self.rows.append(new_row.strip())
                new_row = ""
                end_of_row = 0
            else:
                new_row += f"{num} "

        for row in self.rows:
            a = row.split()  # should have used this earlier - live and learn
            index = -1
            for num in a:
                index += 1
                try:
                    self.columns[index] = self.columns[index] + f" {num}"
                except Exception:
                    self.columns.append(num)

    #  I need these methods to return column and rows in a [] list format

    def row(self, index):
        #  this method returns a row with the selected index
        row_list = []
        for a in self.rows[index - 1].split():
            if a != " ":
                row_list.append(int(a))
        return row_list

    def column(self, index):
        #  this method returns a column with the selected index
        column_list = []
        for a in self.columns[index - 1].split():
            if a != " ":
                column_list.append(int(a))
        return column_list


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
