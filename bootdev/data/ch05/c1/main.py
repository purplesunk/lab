class BSTNode:
    def search_range(self, lower_bound, upper_bound):
        if self.val >= lower_bound and self.val <= upper_bound:
            arr = []
            if self.left != None:
                arr.extend(self.left.search_range(lower_bound, upper_bound))
            arr.append(self.val)
            if self.right != None:
                arr.extend(self.right.search_range(lower_bound, upper_bound))
            return arr
        if self.val < lower_bound and self.right != None:
            return self.right.search_range(lower_bound, upper_bound)
        if self.val > upper_bound and self.left != None:
            return self.left.search_range(lower_bound, upper_bound)
        return []

    # don't touch below this line

    def exists(self, val):
        if val == self.val:
            return True

        if val < self.val:
            if self.left is None:
                return False
            return self.left.exists(val)

        if self.right is None:
            return False
        return self.right.exists(val)

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
