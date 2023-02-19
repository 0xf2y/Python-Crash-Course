favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }
ppl=['jen','mark']
for person in favorite_languages.keys():
    if person in ppl:
        print("thanks for responding")
    else:
        print("take the poll.")