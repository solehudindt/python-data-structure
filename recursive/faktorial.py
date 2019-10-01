def fak(a):
    if a < 1:
        return 1
    else:
        return a * fak(a-1)

def main():
    print(fak(3))

if __name__ ==  '__main__':
    main()
