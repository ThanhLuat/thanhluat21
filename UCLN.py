def UCLN(a,b):
    if b == 0:
        return a
    else:
        return UCLN(b,a%b)
def main():
    e = USCLN(8,12)
    print("UCLN cua 8 va 12:", e)
if __name__ == "__main__":
    main()