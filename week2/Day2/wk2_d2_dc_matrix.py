#Daily challenge: Solve the Matrix

matrix = [
    ['7', 'i', 'i'],
    ['T', 's', 'x'],
    ['h', '%', '?'],
    ['i', ' ', '#'],
    ['s', 'M', ' '],
    ['$', 'a', ' '],
    ['#', 't', '%'],
    ['^', 'r', '!']
]

def decode_matrix(matrix):
    result = ""

    num_columns = len(matrix[0])

    for col in range(num_columns):
        for row in matrix:
            if row[col].isalpha():
                result += row[col]
            else:
                if result and result[-1] != " ":
                    result += " "

    result = ' '.join(result.split())
    return result

decoded_message = decode_matrix(matrix)

print("Decoded message:", decoded_message)