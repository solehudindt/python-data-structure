def push(stack, angka):
    if not ismax(stack):
        print("Push angka", angka)
        stack.append(angka)

def pop(stack):
    if not isempty(stack):
        print("pop stack", stack)
        stack.pop()

def ismax(stack):
    if len(stack) > 5:
        print("Stack penuh")
        return True

def isempty(stack):
    if not stack:
        print("Stack kosong")
        return True

def main():
    tumpukan = list()
    push(tumpukan, 10)
    push(tumpukan, 20)
    print("stack: ",tumpukan)
    pop(tumpukan)
    print("stack: ",tumpukan)

if __name__ == "__main__":
    main()