def last_early(string):
    new_string = string.lower()
    if new_string[-1] in new_string[:-1]:
        return True
    else:
        return False

def main():
    print(last_early("happy birthday")) # True
    print(last_early("best of luck")) # False
    print(last_early("Wow")) # True
    print(last_early("X")) # False

if __name__ == "__main__" :
    main()