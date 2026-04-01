# bplustree_sim.py

class BPlusTreeNode:
    def __init__(self, leaf=False):
        self.leaf = leaf
        self.keys = []
        self.child = []
        self.next_leaf = None  

class BPlusTree:
    def __init__(self, t):
        self.root = BPlusTreeNode(True)
        self.t = t

    def insert(self, k):
        root = self.root
        if len(root.keys) == (2 * self.t) - 1:
            temp = BPlusTreeNode()
            self.root = temp
            temp.child.insert(0, root)
            self.split_child(temp, 0)
            self.insert_non_full(temp, k)
        else:
            self.insert_non_full(root, k)

    def insert_non_full(self, x, k):
        i = len(x.keys) - 1
        if x.leaf:
            x.keys.append(None)
            while i >= 0 and k < x.keys[i]:
                i -= 1
            x.keys.insert(i + 1, k)
            x.keys.pop()
        else:
            while i >= 0 and k < x.keys[i]:
                i -= 1
            i += 1
            if len(x.child[i].keys) == (2 * self.t) - 1:
                self.split_child(x, i)
                if k > x.keys[i]:
                    i += 1
            self.insert_non_full(x.child[i], k)

    def split_child(self, x, i):
        t = self.t
        y = x.child[i]
        z = BPlusTreeNode(y.leaf)
        x.child.insert(i + 1, z)
        
        if y.leaf:
            # B+ Tree: Jika Leaf, nilai tengah DIDUPLIKASI ke parent
            x.keys.insert(i, y.keys[t - 1])
            z.keys = y.keys[t - 1: (2 * t) - 1]
            y.keys = y.keys[0: t - 1]
            
            # Menyambungkan Linked List
            z.next_leaf = y.next_leaf
            y.next_leaf = z
        else:
            # Jika Internal Node, sifat split sama seperti B-Tree biasa
            x.keys.insert(i, y.keys[t - 1])
            z.keys = y.keys[t: (2 * t) - 1]
            y.keys = y.keys[0: t - 1]
            z.child = y.child[t: 2 * t]
            y.child = y.child[0: t]

    def print_tree(self, x, level=0):
        if x.leaf:
            print(f"Level {level} (LEAF) | Keys: {x.keys}")
        else:
            print(f"Level {level} (INDEX)| Keys: {x.keys}")
            for child in x.child:
                self.print_tree(child, level + 1)

    def print_linked_list(self):
        print("\n--- Linked List pada Daun (B+ Tree) ---")
        # Mencari leaf paling kiri
        curr = self.root
        while not curr.leaf:
            curr = curr.child[0]
        
        # Menelusuri semua leaf melalui pointer next_leaf
        leaves = []
        while curr is not None:
            leaves.append(str(curr.keys))
            curr = curr.next_leaf
        print(" -> ".join(leaves))

if __name__ == '__main__':
    bplus_tree = BPlusTree(2)
    data_20 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 
               110, 120, 130, 140, 150, 160, 170, 180, 190, 200]
    
    print("=== SIMULASI B+ TREE (20 DATA) ===")
    for data in data_20:
        bplus_tree.insert(data)
        
    bplus_tree.print_tree(bplus_tree.root)
    bplus_tree.print_linked_list()