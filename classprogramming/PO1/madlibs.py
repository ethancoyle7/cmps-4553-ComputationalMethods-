from random import choice 

f = open("words.txt")

places = f.readline()
adj = f.readline()
pluralnouns = f.readline()
nouns = f.readline()
verbs = f.readline()
title = f.readline()
story = f.read()

places_list = places.split()
adj_list = adj.split()
pluralnouns_list = pluralnouns.split()
nouns_list = nouns.split()
verbs_list = verbs.split()
story_list = story.split()

print (" \n\n               " + title + "\n\n")
print (story)

uniqueStory = ""

for word in story_list:
    subword = word
    if word == "PLACE":
       subword = choice(places_list)
    if word == "ADJECTIVE":
       subword = choice (adj_list)
    if word == "PLURALNOUN":
       subword = choice (pluralnouns_list)
    if word == "NOUN":
       subword = choice (nouns_list)
    if word == "VERB":
       subword = choice (verbs_list)

    uniqueStory = uniqueStory + "  " + subword

print (" \n\n             " + title + "\n\n")
print (uniqueStory)
