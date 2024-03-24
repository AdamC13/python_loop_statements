#1
import random
moods = ["Happy", "Sad", "Energetic", "Calm"]
week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
for i in range(len(week)):
    mood = random.choice(moods)
    print(f"On {week[i]} you were feeling {mood}")

#2
moods = ["Happy", "Sad", "Energetic", "Calm"]
week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
times = ["morning", "afternoon", "evening"]
for day in week:
    print("\n")
    for time in times:
        print(f"On {day} {time} you were feeling {random.choice(moods)}")

#3
c = 0   
while c < 5:
    print("This loop will go five times")
    c += 1
    
#4
options = ["car", "house", "dog"]
while True:
    answer = random.choice(options)
    guess = input("Choose either car, house, or dog (or quit) ")
    if guess == "quit":
        break
    elif guess == answer:
        print("You got it correct!")
    else:
        print("Wrong!")

#5
genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']
t = 0
for genre in genres:
    t += 1
    print(f"Now playing {genre} track: {t}")

c = 0
while c < len(genres) and genres[c] != "Hip-hop":
    print(f"Now playing {genres[c]} track: {c + 1}")
    c += 1

for i in range(len(genres)):
    print(f"Now playing {genres[i]} track: {i + 1}")
    if genres[i] == "Rock" or genres[i] == "Hip-hop":
        print("The light show is ready!")

#6 upbeat top hits

for genre in genres[1:4]:
    print(genre)
    genres[genres.index(genre)] = [genre, "Upbeat", "Top hits"]
print(genres)

music = []
for genre in genres:
    if type(genre) == list:
        for s_genre in genre:
            music.append(s_genre + " Music")
    else:
        music.append(genre + " Music")
print(music)

for c in range(10, 0, -1):
    print(c)
    if c == 1:
        print("The beat drops now!")
