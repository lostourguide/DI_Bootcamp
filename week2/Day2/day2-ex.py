#Daily challenge: Solve the Matrix
matrix = [
    ['7,' 'i,' 'i'],
    ['T,' 's', 'x'],
    ['h', '%', '?'],
    ['i', ' ', '#'],
    ['s', 'M', ' '],
    ['$', 'a', ' '],
    ['#', 't', '%'],
    ['^', 'r', '!']
]

message = ""

for col in range(len(matrix[0])):
    for row in range(len(matrix)):
        char = matrix[row][col]

        if char.isalpha():
            message+=char
        else:
            if message and message[-1] !=" ":
                message += " "

final_message = " ".join(message.split())

print(final_message)




