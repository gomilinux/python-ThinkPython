#Think Python Exercise 2.4.3

#leave 6:52

print('What is your easy pace?')
easyPace = input()
print('How many miles at an easy pace?')
easyMiles = input()

print('What is your tempo pace?')
tempoPace = input()
print('How many miles at a tempo pace?')
tempoMiles = input()

easyTime = easyMiles * easyPace
tempoTime = tempoMiles * tempoPace

TotalTime = easyTime + tempoTime

print (TotalTime)

