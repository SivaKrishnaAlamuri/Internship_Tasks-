# problem13:-Nested Lists

if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
        
    grades = sorted(list(set(score for name, score in students)))
    second_lowest = grades[1]
    
    second_lowest_students = [name for name, score in students if score == second_lowest]
    
    for name in sorted(second_lowest_students):
        print(name)
