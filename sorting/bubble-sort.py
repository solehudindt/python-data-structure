# a = list()

# # a = [i for i in range(10)]
# print(a)

x = [4,1,3,2]

def bubble(list):
    for i in range(len(list)):
        for j in range(len(list) - 1,i,-1):
            print(i, j)

bubble(x)