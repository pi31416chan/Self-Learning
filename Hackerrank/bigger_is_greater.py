# import json

"""Reference table from 0 to 9 then a to z
Expandable by adding more character:index pair into this table"""
sequence_ref = {
    '0':1,'1':2,'2':3,'3':4,'4':5,'5':6,'6':7,'7':8,'8':9,'9':10,
    'a':11,'b':12,'c':13,'d':14,'e':15,'f':16,'g':17,'h':18,
    'i':19,'j':20,'k':21,'l':22,'m':23,'n':24,'o':25,'p':26,
    'q':27,'r':28,'s':29,'t':30,'u':31,'v':32,'w':33,'x':34,
    'y':35,'z':36,
}

# Function to compare and swap characters for lowest bigger string
def smallest_bigger(string):
    end_char = len(string)
    i = -1
    min_idx = 0
    min_char = '0'
    list_w = [ _ for _ in string ]
    sorted_compared = []

    while True:
        sorted_compared.append((list_w[i],i))
        sorted_compared.sort()
        # print(i)

        if end_char == 1:
            string = 'no answer'
            return string
            break

        if sequence_ref[list_w[i-1]] < sequence_ref[list_w[i]]:
            # print(sorted_compared)
            for n,ni in sorted_compared:
                if sequence_ref[list_w[i-1]] >= sequence_ref[n]:
                    # print('greater than',n)
                    continue
                elif sequence_ref[list_w[i-1]] < sequence_ref[n]:
                    # print('lesser than',n)
                    sorted_compared.append((list_w[i-1],i-1))
                    # sorted_compared.sort(reverse=True)
                    # print(sorted_compared)
                    list_w[i-1] = n
                    sorted_compared.remove((n,ni))
                    # print(sorted_compared)
                    break

            sorted_compared.sort()
            list_w[i:] = [a for a,b in sorted_compared]
            # print(list_w)
            string = ''.join(list_w)
            return string
            break

        elif sequence_ref[list_w[i-1]] >= sequence_ref[list_w[i]]:        
            i -= 1

            if i == -end_char:
                string = 'no answer'
                return string
                break

#Input Section
for num in range(int(input())):
    w = input().strip()

    with open('output.txt','a') as output:
        output.write(f"{smallest_bigger(w)}\n")

# smallest_bigger('c')








