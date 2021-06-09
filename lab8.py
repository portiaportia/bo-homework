# More Arrays
# Author: Bo Rogers
import turtle

t = turtle.Pen()

userAttractions = turtle.textinput("Attractions", "Enter an attraction: ").strip().lower()

attractions = ["fair", "zoo", "mall", "park", "lake"]
locations = ["Long Street", "Coleman Blvd", "Elwood Avenue", "Ten Street", "Shem Drive",]

t.setpos(-300,300)

for attraction in attractions:
    t.write(attraction, font=("Arial", 20,"bold"))
    t.forward(100)

for i in range(len(attractions)):
    if userAttractions == attractions[i]:
        t.write(locations[i], ("Arial", 20,"bold"))


turtle.done()