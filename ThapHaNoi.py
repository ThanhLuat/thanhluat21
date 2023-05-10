def thap_ha_noi(n,a,b,c):
    if n == 1:
        print(a,"sang",c)
    else:
        thap_ha_noi(n-1,a,c,b)
        print(a,"sang",c)
        thap_ha_noi(n-1,b,a,c)
def main():
    n = input("Nhập số đĩa:")
    a, b, c = 'A', 'B', 'C'
    thap_ha_noi(3, a, b, c)

if __name__ == "__main__":
    main()
