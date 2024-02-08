## A list in python is like an array in javascript 
bicycles = ["trek", "cannondale", "redline", "specialized"]
print(bicycles)
print(bicycles[2].title())


friends = ['joy', 'amara', 'goodness', 'ama', 'jabula', 'tess', 'sue']
##lis exercise 1
print(len(friends))
print(friends[0].title())
print(friends[1].title())
print(friends[2].title())
print(friends[3].title())
print(friends[4].title())
print(friends[5].title())
print(friends[6].title())

##List exercise 3.2
print(f"{friends[2].title()} is one of the most interesting people i know ")
print(f"Although i love all my friends like {friends[1].title()} and i have a lot of fun with {friends[2].title()}, She just does not make my day like {friends[3].title()} does after being stressed out by {friends[4].title()} at work ")


## List exercise 3.3
print(f"I once i ahd a friend named {friends[-1].title()} who loved taking a ride daily during the summer. She and {friends[-2].title()} introduced me to riding")



##Modifying list 
friends[0] = "honda"
friends.insert(0, "Johnny boy")

poppedFriends = friends.pop(2)


print(friends)
print(poppedFriends.title())

dinnerGuests = ["Jimmy", "Chick", "peter", "john", "sonny"]
removedGuest = dinnerGuests.pop(3)
dinnerGuests.append("Kevin")
newGuests = ['tony', "lammy", "urom", "david", "collo"]
dinnerGuests.insert(0, "Keanu Reeves")
dinnerGuests.insert(3, "Middle Camper")
dinnerGuests.append("Omega")
eight = dinnerGuests.pop()
seventh = dinnerGuests.pop()
sixth = dinnerGuests.pop()
fifth = dinnerGuests.pop()
fourth = dinnerGuests.pop()
third = dinnerGuests.pop()
del dinnerGuests[:]

print(eight)

print(removedGuest)
print(dinnerGuests)
print(len(dinnerGuests))
# print(f'Hello {dinnerGuests[0]} ypu are cordially invited to dinner at the Ebuzor Manor on the eve of the superbowl.\n Please feel free to rsvp for as much as two people for the dinner')
# print(f'Hello {dinnerGuests[1]} ypu are cordially invited to dinner at the Ebuzor Manor on the eve of the superbowl.\n Please feel free to rsvp for as much as two people for the dinner')
# print(f'Hello {dinnerGuests[2]} ypu are cordially invited to dinner at the Ebuzor Manor on the eve of the superbowl.\n Please feel free to rsvp for as much as two people for the dinner')
# print(f'Hello {dinnerGuests[3]} ypu are cordially invited to dinner at the Ebuzor Manor on the eve of the superbowl.\n Please feel free to rsvp for as much as two people for the dinner')
# print(f'Hello {dinnerGuests[4]} ypu are cordially invited to dinner at the Ebuzor Manor on the eve of the superbowl.\n Please feel free to rsvp for as much as two people for the dinner')
# print(f'Hello {dinnerGuests[5]} ypu are cordially invited to dinner at the Ebuzor Manor on the eve of the superbowl.\n Please feel free to rsvp for as much as two people for the dinner')
# print(f'Hello {dinnerGuests[6]} ypu are cordially invited to dinner at the Ebuzor Manor on the eve of the superbowl.\n Please feel free to rsvp for as much as two people for the dinner')
# print(f'Hello {dinnerGuests[7]} ypu are cordially invited to dinner at the Ebuzor Manor on the eve of the superbowl.\n Please feel free to rsvp for as much as two people for the dinner')

print(f"Hey {eight}, I'm sorry but i have to uninvite you from the dinner i just invited you for as cYnthia just told me we would not be around for the said date. I'll be sure to let you know when we choose a new date ")
print(f"Hey {seventh}, I'm sorry but i have to uninvite you from the dinner i just invited you for as cYnthia just told me we would not be around for the said date. I'll be sure to let you know when we choose a new date ")
print(f"Hey {fifth}, I'm sorry but i have to uninvite you from the dinner i just invited you for as cYnthia just told me we would not be around for the said date. I'll be sure to let you know when we choose a new date ")
print(f"Hey {fourth}, I'm sorry but i have to uninvite you from the dinner i just invited you for as cYnthia just told me we would not be around for the said date. I'll be sure to let you know when we choose a new date ")
print(f"Hey {third}, I'm sorry but i have to uninvite you from the dinner i just invited you for as cYnthia just told me we would not be around for the said date. I'll be sure to let you know when we choose a new date ")


## Sorting a list
##{/* Permanent Sorting */}
cars = ["audi", "bmw", 'porsche', 'nissan', 'toyota', 'honda', 'tesla', 'ford', 'ivm']
# cars.sort()
print("Here is the original list:")
print(cars)

print("\n Heres is the temporarily sorted list:")
print(sorted(cars))

print("\n Here is the original list once more:")
print(cars)

places = ["banff", "toronto", "paris", "new york", "bali", "thailand", "singapore"]
print(places)
print(sorted(places))
print(places)
places.reverse()
print(places)
places.reverse()
print(places)
places.sort()
print(places)
places.sort()
places.reverse()
print(places)


magicians = ['alice', 'david', 'tony', 'tony']
for magician in magicians:
    print(f"Hey {magician.title()}, what agreat show that was")
    print(f"I can't wait to see what {magician.title()} has in store for us today\n")

print('thank you all for a wonderful show')


pizzas = ['pepperoni', 'cheese', 'bacon', 'hawaiian', 'boston']

for pizza in pizzas:
    print(f"i like {pizza} pizzas")

print("Damn i really love pizza")


animals = ['dog', 'cat', 'horse', 'parrot', 'goldfish']
for animal in animals:
    print(f"A {animal} would make a reallly lovely pet")

print("Any of these animlas would make a great pet")


for number in range(1, 23):
    print(f"Here is number {number}")

numbers =list(range(1,11))
print(numbers)

evenNumbers = list(range(2,21,2))
print(evenNumbers)


squares = []

for square in range(1, 11):
    value = square** 2
    squares.append(value)

print(squares)

raised = []

for raises in range(2, 21):    
    raised.append(raises ** 2)

print(raised)

## List comprehension 
shore = [value**2 for value in range(1, 6)]
print(shore)


twenty = list(range(1,21))
print(twenty)

twentyOne = []
for twenty in range(1,21):
    print(twenty)


millions = list(range(1, 1000001))

# for million in millions:
#     print(million)

# print(millions)
print(min(millions))
print(max(millions))
print(sum(millions))
max(millions)


oddMillions = list(range(1, 21, 2))
print(oddMillions)

threes = []
for three in range(3, 31, 3):
    threes.append(three)

print(threes)

cubes = []

for cube in range(1, 11):
    cubes.append(cube ** 3)

print(cubes)


cubic = [cube**3 for cube in range(1,11)]
print(cubic)