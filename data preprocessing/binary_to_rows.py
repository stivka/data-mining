text_file = open("data preprocessing/binary table.txt", "r")
raw_list = text_file.read().splitlines()
print(str(raw_list))
print(str(len(raw_list)) + ' rows of raw data' +'\n')

matrix = []
for line in raw_list:
    matrix.append(line[9:].split(' '))
print(str(matrix))
print('9 rows of addresses with 16 transaction columns' + '\n')

output_file = open("D:\\Program Files\\Apriori\\input.txt", "w")

transactions_for_address = []
for address in range(9):
    line = ""
    #line = ('Address' + str(address + 1) + ': ')
    for transaction in range(16):
        if (matrix[address][transaction] == '1'):
            transaction = 'Transaction' + str(transaction + 1) + ' '
            line += transaction
    output_file.write(line + "\n")
    # print(line)
output_file.close()

output_file = open("D:\\Program Files\\Apriori\\input.txt", "r")
print(output_file.read())

# Also use numpy to transpose the data to have it as addresses for transactions