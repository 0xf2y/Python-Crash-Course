cities={ "paris":
            {
                "country":"france",
                "population":"5 million",
                "fact":"evil tower"
            },
        "london":
            {
                "country":"england",
                "population":"6 million",
                "fact":"bing bang"
            },
        "cairo":
            {
                "country":"egypt",
                "population":"104 million",
                "fact":"cairo tower"

            }
}
for key1, values in cities.items():
    print(f"the name of the city is {key1} and here are some info about it:")
    for key2,value in values.items():
        print(f"{key2}:\n{value}")