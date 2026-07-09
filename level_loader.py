import os
from arrow import Arrow
from direction import Direction

def load_level(file_path):
    grid = []
    expected_cols = -1

    file_extension = os.path.splitext(file_path)[1].lower()

    with open(file_path, 'r') as f:
        for line_num, line in enumerate(f, 1):
            stripped_line = line.strip()

            if not stripped_line:
                continue

            cells = []
            if file_extension == '.csv':
                cells = stripped_line.split(',')
            elif file_extension == '.txt' or file_extension == '':
                cells = list(stripped_line.split(' '))
            else:
                raise NotImplementedError(f"Unsupported file type: {file_extension}. Only .txt and .csv are supported.")

            if expected_cols == -1:
                expected_cols = len(cells)
            elif len(cells) != expected_cols:
                raise ValueError(f"Inconsistent number of columns in {file_path} at line {line_num}. Expected {expected_cols}, got {len(cells)}.")

            row = []
            for char_index, char_code in enumerate(cells):
                char_code = char_code.strip()
                if char_code == 'L':
                    row.append(Arrow(Direction.LEFT))
                elif char_code == 'R':
                    row.append(Arrow(Direction.RIGHT))
                elif char_code == 'U':
                    row.append(Arrow(Direction.UP))
                elif char_code == 'D':
                    row.append(Arrow(Direction.DOWN))
                elif char_code == '.':
                    row.append(None)
                else:
                    raise ValueError(f"Invalid character '{char_code}' found in {file_path} at line {line_num}, position {char_index + 1}.")
            grid.append(row)

    if not grid:
        raise ValueError(f"The level file {file_path} is empty or contains no valid level data.")
        
    return grid