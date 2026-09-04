class Node:

    def __init__(self, letter):
        self.letter = letter
        self.is_terminal = False
        self.children = {}
    
    def add(self, child):
        if child not in self.children:
            self.children[child] = Node(child)
    
    def getChild(self, child):
        if child not in self.children:
            return None
        return self.children[child]
    
    def makeTerminal(self):
        self.is_terminal = True

    def isTerminal(self):
        return self.is_terminal

class PrefixTree:

    def __init__(self):
        self.root = Node("")
        self.root.makeTerminal()

    def insert(self, word: str) -> None:
        current = self.root
        for idx, letter in enumerate(word): 
            current.add(letter)
            current = current.getChild(letter)
            if idx == len(word)-1:
                current.makeTerminal()

    def search(self, word: str) -> bool:
        current = self.root
        for idx, letter in enumerate(word):
            current = current.getChild(letter)
            if current == None: 
                return False
            if idx == len(word)-1 and not current.isTerminal():
                return False
        return True

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for idx, letter in enumerate(prefix):
            current = current.getChild(letter)
            if current == None: 
                return False
        return True



        
        