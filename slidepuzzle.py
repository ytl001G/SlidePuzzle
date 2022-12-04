class Puzzle:
    def __init__(self, puzzle: list[int], n: int):
        self.puzzle = puzzle
        self.n = n
    
    def __repr__(self):
        s: str = ''
        digits = self.n**2 // 10 + 1
        
        for i, v in enumerate(self.puzzle):
            if v != -1:
                s += ' ' * (digits - v // 10) + str(v)
            else:
                s += ' ' * digits + 'X'

            if i % 4 == 3:
                s += '\n'
        
        return s
                
    def canSolve(self) -> bool:
        inversion: int = 0
        
        Xindex = self.puzzle.index(-1)
        Xpos = self.n - Xindex // self.n
        
        for p1 in range(self.n**2):
            for p2 in range(p1, self.n**2):
                if p1 == Xindex or p2 == Xindex:
                    continue
                inversion += int(self.puzzle[p1] > self.puzzle[p2])
                
        if self.n % 2:
            return not(inversion % 2)
        else:
            if Xpos % 2:
                return not(inversion % 2)
            else:
                return bool(inversion % 2)
    
    def printChanges(self, change: int):
        digits = self.n**2 // 10 + 1
        
        for i, v in enumerate(self.puzzle):
            if v != -1:
                print(' ' * (digits - v // 10), end='')
                
                if i == change:
                    print('\033[91m{}\033[0m'.format(str(v)), end='')
                else:
                    print(v, end='')
                
            else:
                print(' ' * digits + '\033[91mX\033[0m', end='')
                
            if i % 4 == 3:
                print()

puzzle: list[int] = []
n: int = 4

for _ in range(n):
    puzzle.extend(map(int, input().split()))

p = Puzzle(puzzle, n)
print(p)
p.printChanges(1)
