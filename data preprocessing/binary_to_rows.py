text_file = open("binary table.txt", "r")
raw_list = text_file.read().splitlines()
print(str(raw_list))
print(str(len(raw_list)) + ' rows of raw data' +'\n')

matrix = []
for line in raw_list:
    matrix.append(line[9:].split(' '))
print(str(matrix))
print('9 rows of addresses with 16 transaction columns' + '\n')

transactions_for_address = []
for address in range(9):
    line = ('Address' + str(address + 1) + ': ')
    for transaction in range(16):
        if (matrix[address][transaction] == '1'):
            transaction = 'Transaction' + str(transaction + 1) + ' '
            line += transaction
    print(line)

# Also use numpy to transpose the data to have it as addresses for transactions