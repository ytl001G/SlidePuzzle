puzzle: list[int] = []
n: int = 4

for _ in range(n):
    puzzle.extend(map(int, input().split()))
    
def canSolve(puzzle: list, n: int) -> bool:
    inversion: int = 0
    
    Xindex = puzzle.index(-1)
    Xpos = n - Xindex // n
    
    for p1 in range(n**2):
        for p2 in range(p1, n**2):
            if p1 == Xindex or p2 == Xindex:
                continue
            inversion += int(puzzle[p1] > puzzle[p2])
            
    if n % 2:
        return not(inversion % 2)
    else:
        if Xpos % 2:
            return not(inversion % 2)
        else:
            return bool(inversion % 2)
    
def printPuzzle(puzzle: list, n: int):
    digits = n**2 // 10 + 1
    
    for i, v in enumerate(puzzle):
        if v != -1:
            print(' ' * (digits - v // 10), end='')
        else:
            print(' ' * (digits - 1), end='')
            
        print(v, end='')
        if i % 4 == 3:
            print()


print(canSolve(puzzle, n))
printPuzzle(puzzle, n)
    

