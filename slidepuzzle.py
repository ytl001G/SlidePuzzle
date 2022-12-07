class Puzzle:
    def __init__(self, puzzle: list[int], n: int):
        self.puzzle = puzzle
        self.n = n
        self.fix: list[int] = []
    
    def __repr__(self):
        s: str = ''
        digits = self.n**2 // 10 + 1
        
        for i, v in enumerate(self.puzzle):
            if v != -1:
                s += ' ' * (digits - v // 10) + str(v)
            else:
                s += ' ' * digits + 'X'

            if i % self.n == self.n - 1:
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
    
    def printChanges(self, change1: int, change2: int):
        print('\n================================\n')
        digits = self.n**2 // 10 + 1
        
        for i, v in enumerate(self.puzzle):
            if v != -1:
                print(' ' * (digits - v // 10), end='')
                
                if i == change1 or i == change2:
                    print('\033[91m{}\033[0m'.format(str(v)), end='')
                else:
                    print(v, end='')
                
            else:
                print(' ' * digits + '\033[91mX\033[0m', end='')
                
            if i % self.n == self.n - 1:
                print()
        
    def col(self, index: int):
        return index % self.n
    
    def row(self, index: int):
        return index // self.n

    def canMoveUp(self, index: int):
        return index // self.n > 0
    
    def canMoveDown(self, index: int):
        return index // self.n < n-1
    
    def canMoveLeft(self, index: int):
        return index % self.n > 0
    
    def canMoveRight(self, index: int):
        return index % self.n < n-1
        
    def switch(self, index1: int, index2: int):
        self.puzzle[index1], self.puzzle[index2] = self.puzzle[index2], self.puzzle[index1]
        self.printChanges(index1, index2)

    def moveXUp(self):
        Xindex = self.puzzle.index(-1)
        if not self.canMoveUp(Xindex):
            raise RuntimeError('index {} X cannot move Up'.format(Xindex))
        
        self.switch(Xindex, Xindex - n)
    
    def moveXDown(self):
        Xindex = self.puzzle.index(-1)
        if not self.canMoveDown(Xindex):
            raise RuntimeError('index {} X cannot move Down'.format(Xindex))
        
        self.switch(Xindex, Xindex + n)
        
    def moveXLeft(self):
        Xindex = self.puzzle.index(-1)
        if not self.canMoveLeft(Xindex):
            raise RuntimeError('index {} X cannot move Left'.format(Xindex))
        
        self.switch(Xindex, Xindex - 1)
    
    def moveXRight(self):
        Xindex = self.puzzle.index(-1)
        if not self.canMoveRight(Xindex):
            raise RuntimeError('index {} X cannot move Right'.format(Xindex))
        
        self.switch(Xindex, Xindex + 1)
    
    def moveX(self, x: int, y: int):
        Xindex = self.puzzle.index(-1)
        dx = x - self.col(Xindex)
        dy = y - self.row(Xindex)
        
        for _ in range(abs(dx)):
            if dx > 0:
                self.moveXRight()
            else:
                self.moveXLeft()
        
        for _ in range(abs(dy)):
            if dy > 0:
                self.moveXDown()
            else:
                self.moveXUp()
    
    def moveTileUp(self, index):
        if not self.canMoveUp(index):
            raise RuntimeError('index {} Tile cannot move Up'.format(index))
        
        Xindex = self.puzzle.index(-1)
        
        if self.col(Xindex) > self.col(index):
            direction = (self.col(index) + 1, self.row(index) - 1)
            self.moveX(*direction)
            self.moveXLeft()
            self.moveXDown()
            
        elif self.col(Xindex) < self.col(index):
            direction = (self.col(index) - 1, self.row(index) - 1)
            self.moveX(*direction)
            self.moveXRight()
            self.moveXDown()
            
        else:
            if self.canMoveRight(Xindex):
                self.moveXRight()
            else:
                self.moveXLeft()
            self.moveTileUp(index)

    def moveTileDown(self, index):
        if not self.canMoveDown(index):
            raise RuntimeError('index {} Tile cannot move Down'.format(index))
        
        Xindex = self.puzzle.index(-1)
        
        if self.col(Xindex) > self.col(index):
            direction = (self.col(index) + 1, self.row(index) + 1)
            self.moveX(*direction)
            self.moveXLeft()
            self.moveXUp()
            
        elif self.col(Xindex) < self.col(index):
            direction = (self.col(index) - 1, self.row(index) + 1)
            self.moveX(*direction)
            self.moveXRight()
            self.moveXUp()
            
        else:
            if self.canMoveRight(Xindex):
                self.moveXRight()
            else:
                self.moveXLeft()
            self.moveTileDown(index)

    def moveTileLeft(self, index):
        if not self.canMoveLeft(index):
            raise RuntimeError('index {} Tile cannot move Left'.format(index))
        
        Xindex = self.puzzle.index(-1)
        
        if self.row(Xindex) > self.row(index):
            direction = (self.col(index) - 1, self.row(index) + 1)
            self.moveX(*direction)
            self.moveXUp()
            self.moveXRight()
            
        elif self.row(Xindex) < self.row(index):
            direction = (self.col(index) - 1, self.row(index) - 1)
            self.moveX(*direction)
            self.moveXDown()
            self.moveXRight()
            
        else:
            if self.canMoveUp(Xindex):
                self.moveXUp()
            else:
                self.moveXDown()
            self.moveTileLeft(index)

    def moveTileRight(self, index):
        if not self.canMoveRight(index):
            raise RuntimeError('index {} Tile cannot move Right'.format(index))
        
        Xindex = self.puzzle.index(-1)
        
        if self.row(Xindex) > self.row(index):
            direction = (self.col(index) + 1, self.row(index) + 1)
            self.moveX(*direction)
            self.moveXUp()
            self.moveXLeft()
            
        elif self.row(Xindex) < self.row(index):
            direction = (self.col(index) + 1, self.row(index) - 1)
            self.moveX(*direction)
            self.moveXDown()
            self.moveXLeft()
            
        else:
            if self.canMoveUp(Xindex):
                self.moveXUp()
            else:
                self.moveXDown()
            self.moveTileRight(index)
    
    def moveTile(self, N: int, x: int, y: int):
        Nindex = self.puzzle.index(N)
        dx = x - self.col(Nindex)
        dy = y - self.row(Nindex)
        
        for _ in range(abs(dx)):
            Nindex = self.puzzle.index(N)
            
            if dx > 0:
                self.moveTileRight(Nindex)
            else:
                self.moveTileLeft(Nindex)
        
        for _ in range(abs(dy)):
            Nindex = self.puzzle.index(N)
        
            if dy > 0:
                self.moveTileDown(Nindex)
            else:
                self.moveTileUp(Nindex)
    
    def solve(self):
        if not self.canSolve():
            raise RuntimeError('puzzle is not solvable')
        
        self.moveTile(1, 0, 0)
        self.moveTile(2, 2, 0)
        self.moveTile(3, 2, 1)
        self.moveX(1, 0)
        self.moveXRight()
        self.moveXDown()
        self.moveTile(4, 0, 2)
        self.moveTile(7, 1, 2)
        self.moveX(0, 1)
        self.moveXDown()
        self.moveXRight()
        self.moveTile(5, 1, 2)
        self.moveTile(8, 2, 2)
        self.moveX(1, 1)
        self.moveXDown()
        self.moveXRight()

puzzle: list[int] = []
n: int = 3

for _ in range(n):
    puzzle.extend(map(int, input().split()))

p = Puzzle(puzzle, n)
p.solve()

'''
1 8 2
-1 4 3
7 6 5
'''