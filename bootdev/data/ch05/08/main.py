class BSTNode:
    def delete(self, val):
        if self.val == None:
            return None
        if val < self.val:
            if self.left != None:
                self.left = self.left.delete(val)
            return self
        if val > self.val:
            if self.right != None:
                self.right = self.right.delete(val)
            return self
        if self.val == val:
            if self.right == None:
                return self.left
            if self.left == None:
                return self.right
            if self.right and self.left:
                min_larger_node = self.right
                while min_larger_node.left is not None:
                    min_larger_node = min_larger_node.left

                self.val = min_larger_node.val
                self.right = self.right.delete(min_larger_node.val)
                return self

                

    # don't touch below this line

    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

    def insert(self, val):
        if not self.val:
            self.val = val
            return

        if self.val == val:
            return

        if val < self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left = BSTNode(val)
            return

        if self.right:
            self.right.insert(val)
            return
        self.right = BSTNode(val)
