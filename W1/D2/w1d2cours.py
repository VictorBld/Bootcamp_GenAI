
# # d={
# #     'first_name' : 'John',
# #     'last_name' : 'Doe',
# #     'favorite_hobby' : 'Python',
# #     'sports_hobby' : 'gym',
# #     'age' : 82,
# # }

# # print(d)

# playlist = {
#     'title': "Hello World",
#     'author': "Planet",
#     'songs': [
#         {
#             'song_title': "Song One",
#             'artist': ['Artist 1', 'Artist 2'],
#             'duration': 4.31,
#         },
#         {
#             'song_title': "Song Two",
#             'artist': ['Artist 1'],
#             'duration': 2.53,
#         },
#         {
#             'song_title': "Song Three",
#             'artist': ['Artist 1', 'Artist 2', 'Artist 3'],
#             'duration': 3.43,
#         }
#     ]
# }

# total_duration= 0
# for song in playlist['songs']:
#   total_duration += song['duration']
# print(f"La somme des durées est : {total_duration}. ")

# words = ['PYTHON', 'JOHN', 'chEEse', 'hAm', 'DOE', '123']
# new_words=[]
# for i in range(len(words)) :
#     if words[i].isupper()== True:
#         new_words.append(words[i])

# print(new_words)

def average_length_of_words(string):
   words=string.split()
   total_length = sum(len(word)for word in words)
   average_length = total_length / len(words)
   return round(average_length)


average_length_of_words("Je m'appelle Victor Blondeau")
   