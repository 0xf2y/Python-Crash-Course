pet1={
    "kind":"dog",
    "owner":"albert"
}
pet2={
    "kind":"cat",
    "owner":"martin"
}
pet3={
    "kind":"fish",
    "owner":"kevin"
}
pets=[pet1,pet2,pet3]
for pet in pets:
    print(f'{pet["kind"]}\n{pet["owner"]}')