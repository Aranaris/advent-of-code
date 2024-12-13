import os
import re

with open('../inputs/Day4TestInput.txt', 'r') as file:
# with open('../inputs/Day4Input.txt', 'r') as file:
	total = 0
	grid = []
	for line in file:
		grid.append(line.rstrip())
	
	match = 'XMAS'

	for r in range(len(grid)):
		for c in range(len(grid[r])):
			if grid[r][c] == match[0]:
				#check current row
				if len(grid[r]) > c + 3:
					if grid[r][c:c+4] == match:
						total += 1
				if c >= 3:
					if grid[r][c-1:c-4:-1] == match[1:]:
						total += 1
				#check below
				if r + 3 < len(grid):
					if grid[r+1][c] + grid[r+2][c] + grid[r+3][c] == match[1:]:
							total += 1
					if len(grid[r]) > c + 3:
						if grid[r+1][c+1] + grid[r+2][c+2] + grid[r+3][c+3] == match[1:]:
							total += 1
					if c >= 3:
						if grid[r+1][c-1] + grid[r+2][c-2] + grid[r+3][c-3] == match[1:]:
							total += 1
			#check backwards below
			if grid[r][c] == match[-1]:
				if r + 3 < len(grid):
					if grid[r+3][c] + grid[r+2][c] + grid[r+1][c] == match[0:3]:
							total += 1
					if len(grid[r]) > c + 3:
						if grid[r+3][c+3] + grid[r+2][c+2] + grid[r+1][c+1]  == match[0:3]:
							total += 1
					if c >= 3:
						if grid[r+3][c-3] + grid[r+2][c-2] + grid[r+1][c-1]  == match[0:3]:
							total += 1
	print(total)


# with open('../inputs/Day4TestInput.txt', 'r') as file:
with open('../inputs/Day4Input.txt', 'r') as file:
	total = 0
	grid = []
	for line in file:
		grid.append(line.rstrip())

	for r in range(1, len(grid) - 1):
		for c in range(1, len(grid[r]) - 1):
			if grid[r][c] == 'A':
				if grid[r-1][c-1] == 'M' and grid[r+1][c+1] == 'S':
					if (grid[r-1][c+1] == 'M' and grid[r+1][c-1] == 'S') or (grid[r-1][c+1] == 'S' and grid[r+1][c-1] == 'M'):
						total += 1
				if grid[r-1][c-1] == 'S' and grid[r+1][c+1] == 'M':
					if (grid[r-1][c+1] == 'M' and grid[r+1][c-1] == 'S') or (grid[r-1][c+1] == 'S' and grid[r+1][c-1] == 'M'):
						total += 1
	print(total)
