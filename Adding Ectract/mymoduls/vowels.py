def search_for_vowels2(word, latters='aeoiu'):
    print(set(latters).intersection(set(word)))  # intersection of two str
