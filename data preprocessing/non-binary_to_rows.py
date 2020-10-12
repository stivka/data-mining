import codecs

text_file = codecs.open("data preprocessing/non-binary table.txt", "r")
raw_list = text_file.read().splitlines()
print(str(raw_list))
#print(str(len(raw_list)) +  "rows of raw data" +"\n")

# \xe2\x80\xa6 = HORIZONTAL ELLIPSIS

matrix = []
for line in raw_list:
    matrix.append(line.split(" "))
print(str(matrix))
print(str(len(matrix)) + " rows of " + "6 columns.\n")

# 8 columns for 14 transactions
transaction = []
dormant_less_than_30 = []
dormant_between_30_360 = []
dormant_more_than_360 = []
value_10_plus = []

value_less_than_1 = []
More_than_50_transaction = []
first_transaction_over_year_ago = []
suspicious_Transaction = []

#for row in matrix:
#    for col in row:
#        if  