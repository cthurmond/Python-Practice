from collections import Counter
 
 # *** MY CODE ***
def most_repeating_word(words):
    max_word = ""
    max_count = 0
    for word in words:
        cnt = Counter()
        for letter in word:
            cnt[letter] += 1
            if cnt[letter] > max_count:
                max_count = cnt[letter]
                max_word = word
    return max_word

print (most_repeating_word(['this', 'is', 'a', 'test', 'program']))

# *** HIS CODE ***
# from collections import Counter
# def most_repeating_word(words):
#     word_counts = {word : max(Counter(word).items(), \
         #key=lambda t: t[1]) for word in words}
    #return max(word_counts, key=lambda w: word_counts[w][1])