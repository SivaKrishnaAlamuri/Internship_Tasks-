# problem_3

def marsExploration(s):
    changes = 0

    for i in range(len(s)):
        if s[i] != "SOS"[i % 3]:
            changes += 1

    return changes


s = input().strip()
print(marsExploration(s))
