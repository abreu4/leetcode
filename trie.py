# https://leetcode.com/problems/implement-trie-prefix-tree/

class Trie:

    def __init__(self, val=None):
        self.val = val
        self.leaves = {}
        self.endOfWord = False

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        # Assert word is of type string

        key = word[0]

        if not key in self.leaves:
            self.leaves[key] = Trie(val=key)

        if len(word) > 1:
            self.leaves[key].insert(word[1:])
        else:
            self.leaves[key].endOfWord = True

        return

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        # Assert word size bigger than 0

        if len(word) == 1: return word in self.leaves and self.leaves[word].endOfWord

        else: 
            try: return self.leaves[word[0]].search(word[1:])
            except: return False
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """

        if len(prefix) == 1: return prefix in self.leaves

        else: 
            try: return self.leaves[prefix[0]].startsWith(prefix[1:])
            except: return False

    def print(self) -> None:

        stack = [leaf for leaf in self.leaves.values()]
        lvl = 1

        while stack:

            tmp = []
            for t in stack:
                tmp.extend([leaf for leaf in t.leaves.values()])
                print(t.val, end=' '*lvl)
            
            print()
            lvl += 1
            stack = tmp


T = Trie()
print(f"Prefix a exists? {T.startsWith('a')}")

T.insert("ananas")
T.insert("sara")
T.insert("dog")

T.print()

print(f"Word sara exists? {T.search('sara')}")
print(f"Word anan exists? {T.search('anan')}")

print(f"Prefix anana exists? {T.startsWith('anan')}")
print(f"Prefix a exists? {T.startsWith('a')}")
