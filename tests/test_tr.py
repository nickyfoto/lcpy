from lcpy import Trie

def test_trie():

    trie = Trie()
    trie.insert("apple")
    assert trie.contains("apple") == True
    assert trie.contains("app") == False
    assert trie.startsWith("app") == ['apple']
    trie.insert("app")
    # assert trie.contains("app") == True

    # assert trie.keys() == ['app', 'apple']
    # assert trie.startsWith("") == ['app', 'apple']