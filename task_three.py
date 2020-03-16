
number_of_sides = [4, 6, 8, 12, 20]

# Looking for probabilities.
for i in number_of_sides:
	p = ((int(i >= 5) * 1/i) * 0.2)/(0.2 * (0 + 1/6 + 1/8 + 1/12 + 1/20))
	print(p)

