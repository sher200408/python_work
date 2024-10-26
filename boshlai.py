
a = {word:len(word) for word in ["hello","hi","www","hello world"]}
print(a)

date = {
    "h1":"1",
    "h2":"2",
    "h3":"3",
    "h4":"4",
}

b = {
    key.count() for key ,value in date.items()
}
print(b)
