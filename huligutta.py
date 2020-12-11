'''
file: huligutta.py
Description: Board functionalities
'''

__author__ = "Clyde James Felix"
__email__ = "cjfelix.hawaii.edu"
__status__ = "Dev"

import sys

class Board:
    a = { 1:(), 2:(),3:() }
    f = { 1:(), 2:(),3:() }
    origin = ()
    b = { 0:origin, 1:(),2:(),3:(),4:()}
    c = { 0:origin, 1:(),2:(),3:(),4:()}
    d = { 0:origin, 1:(),2:(),3:(),4:()}
    e = { 0:origin, 1:(),2:(),3:(),4:()}
        
    def __init__(self):
        if not self.b[0]==() :
            self.origin = self.b[0]  
            self.c[0] = self.b[0] 
            self.d[0] = self.b[0] 
            self.e[0] = self.b[0] 
        if not self.c[0]==():
            self.origin = self.c[0]
            self.b[0] = self.b[0] 
            self.d[0] = self.b[0] 
            self.e[0] = self.b[0]
        if not self.d[0]==() :
            self.origin = self.d[0]
            self.c[0] = self.b[0] 
            self.b[0] = self.b[0] 
            self.e[0] = self.b[0]
        if not self.e[0]==() :
            self.origin = self.e[0]
            self.c[0] = self.b[0] 
            self.d[0] = self.b[0] 
            self.b[0] = self.b[0] 

        self.boardPositions = {'b0': self.b[0],'a1': self.a[1],'a2': self.a[2],'a3': self.a[3],
        'b1': self.b[1],'b2': self.b[2],'b3': self.b[3],'b4': self.b[4],
        'c1': self.c[1],'c2': self.c[2],'c3': self.c[3],'c4': self.c[4],
        'd1': self.d[1],'d2': self.d[2],'d3': self.d[3],'d4': self.d[4],
        'e1': self.e[1],'e2': self.e[2],'e3': self.e[3],'e4': self.e[4],
        'f1': self.f[1],'f2': self.f[2],'f3': self.f[3]}

    def clearBoard(self):
        a = { 1:(), 2:(),3:() }
        f = { 1:(), 2:(),3:() }
        origin = ()
        b = { 0:origin, 1:(),2:(),3:(),4:()}
        c = { 0:origin, 1:(),2:(),3:(),4:()}
        d = { 0:origin, 1:(),2:(),3:(),4:()}
        e = { 0:origin, 1:(),2:(),3:(),4:()}
        for i in self.a:
            if Position('a',str(i)).content() != ():
                Position('a',str(i)).place(())
        for i in self.b:
            if Position('b',str(i)).content() != ():
                Position('b',str(i)).place(())
        for i in self.c:
            if Position('c',str(i)).content() != ():
                Position('c',str(i)).place(())
        for i in self.d:
            if Position('d',str(i)).content() != ():
                Position('d',str(i)).place(())
        for i in self.e:
            if Position('e',str(i)).content() != ():
                Position('e',str(i)).place(())
        for i in self.f:
            if Position('f',str(i)).content() != ():
                Position('f',str(i)).place(())                
                       
#         print('Initialized board')

    def printBoard(self):
        print('\t*\t*\t'+str(self.origin)+'\t*\t*\t')
        print(str(self.a[1])+'\t'+str(self.b[1])+'\t'+str(self.c[1])+'\t\t'+str(self.d[1])+'\t'+str(self.e[1])+'\t'+str(self.f[1]))
        print(str(self.a[2])+'\t'+str(self.b[2])+'\t'+str(self.c[2])+'\t\t'+str(self.d[2])+'\t'+str(self.e[2])+'\t'+str(self.f[2]))
        print(str(self.a[3])+'\t'+str(self.b[3])+'\t'+str(self.c[3])+'\t\t'+str(self.d[3])+'\t'+str(self.e[3])+'\t'+str(self.f[3]))
        print('\t'+str(self.b[4])+'\t'+str(self.c[4])+'\t\t'+str(self.d[4])+'\t'+str(self.e[4]))
                
    def isAdjacent(self,pos1,pos2):
        if not (self.isValid(pos1) and self.isValid(pos2)):
#             print('Not valid positions')
            return(-1)
        
        adj = 0
        alph = ('a','b','c','d','e','f')
        if pos1[0] == pos2[0] or (pos1[0] in 'bcde' and pos2[0] in 'bcde' and (pos1[1] == 0 or pos2[1] == 0)):
            if abs(int(pos1[1]) - int(pos2[1])) == 1:
                adj = 1

        if abs(alph.index(pos1[0])-alph.index(pos2[0])) == 1:
            if pos1[1] == pos2[1]:
                adj = 1

        return(adj)
    
    def isValid(self,pos):
        valid = 0
        if isinstance(pos, str):
            if len(pos) ==2:
                if pos[0] in 'af':
                    if pos[1] in '123':
                        valid = 1
                if pos[0] in 'bcde':
                    if pos[1] in '01234':
                        valid = 1
        return(valid)

class Position(Board):
        
    def __init__(self,alphabet,number):
    
        address = alphabet + number
        self.alphabet = alphabet
        self.number = number
        
        try:

            assert(self.isValid(address)>0)
            self.location = address
            
        except:
            print('Tried initializing position with invalid location') 
    
    def content(self):
        if self.alphabet == 'a':
            cont = self.a[int(self.number)]
        if self.alphabet == 'b':
            cont = self.b[int(self.number)]
        if self.alphabet == 'c':
            cont = self.c[int(self.number)]
        if self.alphabet == 'd':
            cont = self.d[int(self.number)]
        if self.alphabet == 'e':
            cont = self.e[int(self.number)]
        if self.alphabet == 'f':
            cont = self.f[int(self.number)]

        return cont
    
    def place(self,Animal):
    
        if self.alphabet == 'a':
            self.a[int(self.number)] = Animal
            self.content = Animal
            
        if self.alphabet == 'b': 
            self.b[int(self.number)] = Animal
            self.content = Animal

        if self.alphabet == 'c':            
            self.c[int(self.number)] = Animal
            self.content = Animal
           
        if self.alphabet == 'd':            
            self.d[int(self.number)] = Animal
            self.content = Animal
          
        if self.alphabet == 'e':            
            self.e[int(self.number)] = Animal
            self.content = Animal
          
        if self.alphabet == 'f':            
            self.f[int(self.number)] = Animal    
            self.content = Animal

        if self.number == '0':
            self.b[0] = Animal  
            self.c[0] = Animal  
            self.d[0] = Animal  
            self.e[0] = Animal  
            self.content = Animal  
        pass

    def get_neighbors(self):       
        neighbors = []
        impossibles = ['b4','c0','d0','e0','e4','f4','a4']
        if (self.number == '0' and self.alphabet not in 'af'): 
            neighbors.extend(('b1','c1','d1','e1'))
            
            return neighbors
        for letter in 'abcdef':
            for number in '01234':
                if (self.isValid(self.location) == 1 and self.isAdjacent(self.location,str(letter + number)) == 1):
                    neighbors.append(str(letter + number))
        return [i for i in neighbors if i not in impossibles]

    def get_captures(self):
        captures = []
        impossibles = ['b4','c0','d0','e0','e4','f4','a4']
        for neighbors in self.get_neighbors():
            # print('DEBUG: neighbors',neighbors)
            # neighbor_neighbors = Position(neighbors[0],neighbors[1]).get_neighbors()
            if Position(neighbors[0],neighbors[1]).content() == 'O':
                neighbor_neighbors = Piece(self.location).secondAdjacent(neighbors)
                # print('DEBUG: neighbor_neighbors',neighbor_neighbors)
                if neighbor_neighbors != None:
                    if Position(neighbor_neighbors[0],neighbor_neighbors[1]).content() == ():
                        captures.append(neighbor_neighbors)
        if len(captures) == 0:
            return None
        else:    
            return [i for i in list(set(captures)) if i not in impossibles]

class Piece(Board):

    def __init__(self, position):
        self.position = position
        content = ''
        
    def adjacent(self, newposition):
        # Returns adjacent position given the adjacent position after that
        ans = None
        alph = ('a','b','c','d','e','f')
        if self.position[0] == newposition[0] or int(self.position[1]) + int(newposition[1]) - 2 == 0:
            if abs(int(self.position[1]) > int(newposition[1])) and int(newposition[1]) >= 0:
                ans = self.position[0] + str(int(newposition[1])+1) 
            elif abs(int(self.position[1]) < int(newposition[1])) and int(newposition[1])+1 <= 5:
                ans = newposition[0] + str(int(newposition[1])-1)
            else: 
                ans = None

        if self.position[1] == newposition[1]:
            if alph.index(self.position[0]) > alph.index(newposition[0]) and alph.index(newposition[0]) >= 0:
                ans =  alph[alph.index(newposition[0])+1] + newposition[1]
            elif alph.index(self.position[0]) < alph.index(newposition[0]) and alph.index(newposition[0]) <= len(alph):
                ans = alph[alph.index(newposition[0])-1] + newposition[1]
            else:
                ans = None
        if ans != None:
            if int(self.position[1]) == 0 and int(ans[1]) == 0:
                return None
            if int(ans[1]) >= 4 and ans[0] in 'af': 
                return None
        return ans

    def secondAdjacent(self, newposition):
        ans = None
        alph = ('a','b','c','d','e','f')
        
        if self.position[0] == newposition[0] or int(self.position[1]) + int(newposition[1]) - 1 == 0:
            if abs(int(self.position[1]) > int(newposition[1])) and int(newposition[1])-1 >= 0:
                ans = newposition[0] + str(int(newposition[1])-1) 
            elif abs(int(self.position[1]) < int(newposition[1])) and int(newposition[1])+1 < 5:
                ans = newposition[0] + str(int(newposition[1])+1)
            else: 
                ans = None

        elif self.position[1] == newposition[1]:
                if alph.index(self.position[0]) > alph.index(newposition[0]) and alph.index(newposition[0]) - 1 >= 0:
                    ans =  alph[alph.index(newposition[0])-1] + newposition[1]
                elif alph.index(self.position[0]) < alph.index(newposition[0]) and alph.index(newposition[0])+1 < len(alph):
                    ans = alph[alph.index(newposition[0])+1] + newposition[1]
                else:
                    ans = None
        if ans != None:
            if ans[0] in 'bcde' and int(ans[1]) == 0:
                return 'b0'
            if int(self.position[1]) == 0 and int(ans[1]) == 0:
                return None
            if (int(ans[1]) == 0 or int(ans[1]) >= 4) and ans[0] in 'af': 
                return None
        return ans

    def possibleMoves(self):
        # Generates possible positions given tiger position
        ans = []
        positions = Position(self.position[0],self.position[1]).get_neighbors()
        captures = Position(self.position[0],self.position[1]).get_captures()
        # print('DEBUG: captures ',captures)
        for i in range(len(positions)):
            # print(positions[i])
            if positions[i] in ['c0','d0','e0'] and Position(positions[i][0],positions[i][1]).content() == ():
                ans.append('b0')
            if positions[i] not in ['c0','d0','e0'] and Position(positions[i][0],positions[i][1]).content() == ():
                ans.append(positions[i])
        if captures != None :
            for i in captures:
                ans.append(i)
                # capturesPos = Piece(self.position).secondAdjacent(i)
                # if i != None or capturesPos != None:
                    # ans.append(capturesPos)
        if self.position in ans:
            ans.remove(self.position)
        return list(set(ans))        

class Tiger(Piece):
    def place(self):
        if Position(self.position[0],self.position[1]).content() == (): 
           Position(self.position[0],self.position[1]).place('X')
        pass 

    def move(self,newposition):
        if Position(self.position[0],self.position[1]).content() == 'X' and Position(newposition[0],newposition[1]).content() == ():
            Position(newposition[0],newposition[1]).place('X')
            Position(self.position[0],self.position[1]).place(())
        else:
            print('DEBUG: Tiger cannot go there')
            return -1 
        return 1

    def capture(self,newposition):
        new = self.adjacent(newposition)
        if new == self.position or new == None or Position(self.position[0],self.position[1]).get_captures() == None:
            return -1
        # print('DEBUG: Position(self.position[0],self.position[1]).get_captures() ',Position(self.position[0],self.position[1]).get_captures())
        if new not in Position(self.position[0],self.position[1]).get_captures() and Position(self.position[0],self.position[1]).content() == 'X' and Position(newposition[0],newposition[1]).content() != ():
            print('DEBUG: error on capture')
            return -1
        Position(self.position[0],self.position[1]).place(())
        Position(new[0],new[1]).place(())
        
        new = self.adjacent(newposition)
        Position(newposition[0],newposition[1]).place('X')
        return 1

class Goat(Piece):
    inplay = 0
        
    def move(self,newposition):
        # print('DEBUG: self.position ',self.position)
        # print('DEBUG: newposition ', newposition)
        if Position(self.position[0],self.position[1]).content() == 'O' and Position(newposition[0],newposition[1]).content() == ():
            Position(newposition[0],newposition[1]).place('O')   
            Position(self.position[0],self.position[1]).place(())
            
        else:
            print("Goat cannot go there")
            return -1
        return 1

    def place(self):
        if Position(self.position[0],self.position[1]).content() == (): 
            Position(self.position[0],self.position[1]).place('O')
        pass 

if __name__ == "__main__":
    from functions import *
    # Game Flow
    # Board().clearBoard()
    # Tiger('a1').place()
    # Tiger('c1').place()
    # Tiger('d1').place()
    # Goat('e1').place()
    # Goat('c1').place()
    # Goat('e1').place()
    # Board().printBoard()

    # print(Tiger('d1').secondA())  
    # print(Position('d','1').get_captures())
    # print(Tiger('f1').possibleMoves())
    # Board().printBoard()
    
    # print(Piece('a1').secondAdjacent('a2'))