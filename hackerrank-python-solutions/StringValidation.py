def main():
    S = 'qa2'
    
    print(any(map(str.isalnum, S)))
    print(any(map(str.isalpha, S)))
    print(any(map(str.isdigit, S)))
    print(any(map(str.islower, S)))
    print(any(map(str.isupper, S)))


if __name__ == '__main__':
    # s = input()
    # alphanumeric = s.isalnum()
    # alphabetical = s.isalpha()
    # digits = s.isdigit()
    # lowercase = s.islower()
    # uppercase = s.isupper()

    # print(alphanumeric)
    # print(alphabetical)
    # print(digits)
    # print(lowercase)
    # print(uppercase)

    main()
