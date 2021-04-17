
friends = ['ahmet', 'mehmet', 'ebru', 'mahmut', 'ayşe']

x = 0
while (x < len(friends)):
    friend = friends[x]
    x = x + 1
    if friend == 'mahmut':
        continue
    print(friend)
    