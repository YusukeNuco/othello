def main():

    for i in range(8):
        print("- " * 8)

    row_lis_2 = [0, 0, 0, 0, 0, 0, 0, 0]

    for i in range(len(row_lis_2)):
        if row_lis_2[i] == 0:
            row_lis_2[i] = "- "
    print(row_lis_2)

    print("\n")


    for i in range(len(row_lis_2)):
        if row_lis_2[i] == 0:
            row_lis_2[i] = "- "
        print(row_lis_2)

print(f"__name__: {__name__}")

if __name__ == '__main__':
    main()
