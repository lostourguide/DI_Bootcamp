#Exercise 4: Floats
#floats are decimal numbers

sequence = []
start = 1.5
end = 5
step = 0.5

while start <= end:
    sequence.append(int(start) if start.is_integer() else start)
    start += step

print(sequence)

