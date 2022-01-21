favorite_language={
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
}
people=['jen','sarah','edward','phil','Tom']
#flag=0
for p in people:
    flag=0
    for join_people in favorite_language:
        if p==join_people:
            flag=1
            print('thanks')
            break
    if flag==0:
        print('I want to invite you to join in a activity!')
