class redblacknode():
    def init(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
        self.color = None
        
class redblacktree():
    def init(self, root):
        self.root = root
        
    def insert(self, key):
        root = self.root
        
        while root:
        
            if root.val < key:
                root = root.left
                
            else:
                root = root.right
            
            
             