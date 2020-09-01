max = 10

for i in range(0, max):
	print(' ' * i, end='')
	for x_backward in range(max-1-i, -1, -1):
		print(str(x_backward), end='')
	for x_forward in range(1, max-i):
		print(str(x_forward), end='')
	print()
