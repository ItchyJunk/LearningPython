from pathlib import Path

file_name = input('Enter Filename:')
p = Path(file_name)

with p.open() as f:
	for line in f:
		print(line,end='')
