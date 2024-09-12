restaurants = []
def restaurant_ranker():
   while True:
      asking = input("What are some of your favorite restaurants?")
      restaurants.append(asking)
      if asking == "stop":
         break
restaurant_ranker()
print("So your favorite restaurants are " + str(restaurants) + " , neat.")
