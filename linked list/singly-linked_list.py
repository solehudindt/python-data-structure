class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linked_list():
    def __init__(self):
        self.Head = None

    def insert_tail(self, data):
        if self.Head == None:
            self.insert_head(data)
        else:
            temp = self.Head
            while(temp.next != None):
                temp = temp.next
            temp.next = Node(data)

    def insert_head(self, data):
        newNode = Node(data)
        if self.Head != None:
            newNode.next = self.Head
        self.Head = newNode

    def print_list(self):
        tamp = self.Head
        while tamp is not None:
            print(tamp.data, end=' -> ')
            tamp = tamp.next

def main():
    A = Linked_list()
    print("[ ]")
    print("masukan 10 ke-head")
    A.insert_head(10)
    print("[10]")
    print("masukan 0 ke-head")
    print("[0 - 10]")
    A.insert_head(0)
    print("masukan 100 tail")
    print("[0 - 10 - 100]")
    A.insert_tail(100)
    print("masukan 1000 tail")
    A.insert_tail(1000)
    print("[0 - 10 - 100 - 1000]")
    A.print_list()

if __name__ == "__main__":
    main()
        
