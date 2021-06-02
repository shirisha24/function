def break_into_words(sentence):
    a=sentence.split()
    return a
sentence="navgurukul is an alternative to higher education reducing the barriers of current formal education system"
print(break_into_words(sentence))
words="navgurukul is great"
c=0
while c<len(words):
    print(words[c])
    c=c+1