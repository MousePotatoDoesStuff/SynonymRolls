def swc_test(n):
    match n:
        case 0:
            print('Even')
        case 1:
            print('Odd')
        case c:
            print(f'Number {c} too large or small')
def main():
    swc_test(0)
    swc_test(1)
    swc_test(2)
    return


if __name__ == "__main__":
    main()
