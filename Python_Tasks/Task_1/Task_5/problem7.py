
# problem7:-Symmetric Difference

if __name__ == '__main__':
    m = int(input())
    a = set(map(int, input().split()))
    
    n = int(input())
    b = set(map(int, input().split()))
    
    sym_diff = sorted(a.symmetric_difference(b))
    
    for num in sym_diff:
        print(num)
