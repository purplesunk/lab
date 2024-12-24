import inspect
from main import *

def ref_inorder(node, acc):
    if node is not None:
        ref_inorder(node.left, acc)
        acc.append(node.val)
        ref_inorder(node.right, acc)
    return acc

def ref_implementation(rb_tree, user):
    def ref_implementation_node(rb_node, user):
        if rb_node is rb_tree.nil:
            new_node = RBNode(user)
            new_node.left = rb_tree.nil
            new_node.right = rb_tree.nil
            new_node.red = True #not rb_node.red
            return new_node
        if user < rb_node.val:
            if rb_node.left is rb_tree.nil:
                new_node = RBNode(user)
                new_node.left = rb_tree.nil
                new_node.right = rb_tree.nil
                new_node.red = True #not rb_node.red
                new_node.parent = rb_node
                rb_node.left = new_node
            else:
                ref_implementation_node(rb_node.left, user)
        else:
            if rb_node.right is rb_tree.nil:
                new_node = RBNode(user)
                new_node.left = rb_tree.nil
                new_node.right = rb_tree.nil
                new_node.red = True #not rb_node.red
                new_node.parent = rb_node
                rb_node.right = new_node
            else:
                ref_implementation_node(rb_node.right, user)
        return rb_node
    rb_tree.root = ref_implementation_node(rb_tree.root, user)
