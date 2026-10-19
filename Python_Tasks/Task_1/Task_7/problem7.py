# python7
def print_rangoli(size):
    import string
    letters = string.ascii_lowercase
    
    lines = []
    for i in range(size):
        row_letters = letters[i:size]
        
        pattern = row_letters[::-1] + row_letters[1:]
        row_str = "-".join(pattern).center(4 * size - 3, "-")
        lines.append(row_str)
        
    entire_rangoli = lines[::-1] + lines[1:]
    print("\n".join(entire_rangoli))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
