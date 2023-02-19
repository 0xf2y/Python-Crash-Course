from turtle import title


fav_nums={"gabi":[5,6],
           "ben":[4,24],
           "william":[3,2],
           "leo":[19,10,18],
           "gabriel":[2,3,4]
        }
for key, values in fav_nums.items():
        print(f"{key} favoirite numbers are:")
        for value in values:
                print(value)