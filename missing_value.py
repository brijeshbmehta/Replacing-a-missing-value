#Python2

print "Enter you choice of replacement for missing values in the given dataset"
print "1. With user defined global constant"
print "2. With mean value of the attribute"
print "3. With mean value of each attribute class"
try:
	user_input = int(input())
except NameError:
	print "Invalid Choice"
	exit()
if user_input < 1 or user_input > 3:
	print "Invalid Chioce"
	exit()
data = open('automobile_missing.csv','r')
out1 = open('GlobalValue.csv','w')
out2 = open('MeanValue.csv','w')
out3 = open('ClassWiseMeanValue.csv','w')

if user_input == 1:
	for line in data:
		row = line.strip().split(',')
		i = 1
		for ele in row:
			if ele == '?':
				out1.write('MSNG AT' + ' ' + str(i) + ',')
				print i
			else:
				out1.write(ele + ',')
			i += 1
		out1.write('\n')

elif user_input == 2:
	num_of_records = 0
	sum_row = [0]*26
	for line in data:
		#print line
		row = line.strip().split(',')
		for i in range(len(row)):
			try:
				row[i] = float(row[i])
			except ValueError:
				#print "error"
				continue
			sum_row[i] += row[i]
		#print sum_row
		num_of_records += 1
	#print sum_row
	for i in range(len(sum_row)):
		sum_row[i] = sum_row[i]/num_of_records
	print sum_row