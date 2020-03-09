class SuffixTree:
    alphabet = {}
    def __init__(self, s='', terminal='$'):
        alphabet = {c:i for i,c in enumerate(set(s))}
        if terminal in alphabet: terminal = max(alphabet)+1
        alphabet[terminal] = len(alphabet)
