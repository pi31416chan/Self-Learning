# Input
n = 5
operations = [[1, 2, 100], [2, 5, 100], [3, 4, 100]]



# Variables
subtotal = 0



'''Calculate the cumulative subtotal''' 
def calc_subtotal(operation):
    a,b,k = operation
    global subtotal

    subtotal += (b-a+1) * k



'''Calculate the average'''
for operation in operations:
    calc_subtotal(operation)

average = int(subtotal / n)
print(average)