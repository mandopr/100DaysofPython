row1 = ["⬜", "⬜", "⬜"]
row2 = ["⬜", "⬜", "⬜"]
row3 = ["⬜", "⬜", "⬜"]

map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

position = input("\nWhere do you want to put the treasure, enter(column and row number) : ")
column_num = int(position[0]) - 1
row_num = int(position[1]) - 1

map[row_num][column_num] = "X"
print(f"{row1}\n{row2}\n{row3}")