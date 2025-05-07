def main(input_table):
    non_empty_cols = [
        i for i in range(len(input_table[0]))
        if any(row[i] is not None for row in input_table)
    ]

    table = [
        [row[i] for i in non_empty_cols]
        for row in input_table
    ]

    unique_rows = process_rows(table)
    table = unique_rows
    split_col_index = make_split(table)
    table = split_col(split_col_index, table)
    table = table_process(table)

    if not table:
        return []
    transposed = list(zip(*table))
    transposed = [list(row) for row in transposed]

    return transposed


def process_rows(table):
    seen = set()
    unique_rows = []
    for row in table:
        row_tuple = tuple(row)
        if row_tuple not in seen:
            seen.add(row_tuple)
            unique_rows.append(row)
    return unique_rows


def make_split(table):
    split_col_index = None
    for i in range(len(table[0])):
        split_col_index = make_split_if_statement(i, table)
    return split_col_index


def make_split_if_statement(i, table):
    if any(';' in str(cell)
           for cell in [row[i]
                        for row in table if row[i] is not None]):
        return i


def split_col(split_col_index, table):
    if split_col_index is not None:
        new_table = []
        for row in table:
            if row[split_col_index] and ';' in row[split_col_index]:
                parts = row[split_col_index].split(';')
                new_row = (row[:split_col_index]
                           + parts
                           + row[split_col_index + 1:])
            else:
                new_row = row.copy()
            new_table.append(new_row)
        return new_table


def table_process(table):
    for i in range(len(table)):
        for j in range(len(table[i])):
            cell = table[i][j]

            table = table_process_statements(i, j, cell, table)

    table.sort(key=lambda x: x[1])
    return table


def table_process_statements(i, j, cell, table):
    if j == 0 and cell.startswith('+7('):
        table[i][j] = ''.join(c for c in cell if c.isdigit())[1:]

    if j == 1 and '[at]' in cell:
        table[i][j] = cell.replace('[at]', '@')

    if j == 3 and cell.replace('.', '').isdigit():
        percent = round(float(cell) * 100)
        table[i][j] = f"{percent}%"

    table = table_process_Y_N(cell, table, i, j)

    return table


def table_process_Y_N(cell, table, i, j):
    if cell == 'Нет':
        table[i][j] = "N"

    if cell == 'Да':
        table[i][j] = "Y"

    return table
