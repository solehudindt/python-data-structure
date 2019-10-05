from collections import deque

def enque(queue, num):
    if not isMax(queue):
        queue.append(num)

def deque(queue):
    if not isEmpty(queue):
        queue.popleft()

def cetak(queue):
    for i in queue:
        print("Antrian: [", i,"]", end='')

def isMax(queue):
    if len(queue) > 4:
        print("Antrian Full")
        return True

def isEmpty(queue):
    if not queue:
        print("Antrian Kosong")
        return True

def main():
    antrian = deque([])
    deque(antrian)
    enque(antrian, 2)
    enque(antrian, 5)
    enque(antrian, 9)
    enque(antrian, 7)
    cetak(antrian)
    enque(antrian, 3)
    enque(antrian, 6)
    cetak(antrian)
    deque(antrian)
    cetak(antrian)

if __name__ == "__main__":
    main()
