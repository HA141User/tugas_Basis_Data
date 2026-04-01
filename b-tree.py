# btree_sim.py

class BTreeNode:
    def __init__(self, leaf=False):
        self.leaf = leaf
        self.keys = []
        self.child = []

class BTree:
    def __init__(self, t):
        self.root = BTreeNode(True)
        self.t = t  # Order/Derajat minimum. Jika t=2, maks key = 3.

    def insert(self, k):
        root = self.root
        # Jika root penuh, lakukan split
        if len(root.keys) == (2 * self.t) - 1:
            temp = BTreeNode()
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
        z = BTreeNode(y.leaf)
        
        # B-Tree: Nilai tengah NAIK dan DIHAPUS dari node asal
        x.child.insert(i + 1, z)
        x.keys.insert(i, y.keys[t - 1])
        
        z.keys = y.keys[t: (2 * t) - 1]
        y.keys = y.keys[0: t - 1]
        
        if not y.leaf:
            z.child = y.child[t: 2 * t]
            y.child = y.child[0: t]

    def print_tree(self, x, level=0):
        print(f"Level {level} | Keys: {x.keys}")
        for child in x.child:
            self.print_tree(child, level + 1)

if __name__ == '__main__':
    btree = BTree(2)
    data_20 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 
               110, 120, 130, 140, 150, 160, 170, 180, 190, 200]
    
    print("=== SIMULASI B-TREE (20 DATA) ===")
    for data in data_20:
        btree.insert(data)
    btree.print_tree(btree.root)