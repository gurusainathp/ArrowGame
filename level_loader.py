from arrow import Arrow
from direction import Direction

def load_level(file):
    with open(file, 'r') as f:
        lines = f.readlines()
        grid = [[] for _ in range(len(lines))]
        for i in range(len(lines)):
            line = list(lines[i].strip())
            for j in range(len(line)):
                d = line[j]
                if d == 'L':
                    grid[i].append(Arrow(Direction.LEFT))
                elif d == 'R':
                    grid[i].append(Arrow(Direction.RIGHT))
                elif d == 'U':
                    grid[i].append(Arrow(Direction.UP))
                elif d == 'D':
                    grid[i].append(Arrow(Direction.DOWN))
                elif d == '.':
                    grid[i].append(None)
        return grid