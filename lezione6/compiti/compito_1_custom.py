from math import fabs
from operator import truediv
import random
import json
import requests
 
def get_random_artists_names ()-> list[str]:
  
  with open("C:\\Users\\gabry\\Desktop\\Code\hard-python\\lezione6\\data\\artists.json", "r") as f:
    f_as_dict = json.load(f)
    artists_list = f_as_dict.keys()
  
  random_artists = random.sample(artists_list, 2)

  return random_artists


def get_random_artists_ids (l : list)-> list[str]:

  artists_ids_by_names = []
  
  with open("C:\\Users\\gabry\\Desktop\\Code\hard-python\\lezione6\\data\\artists.json", "r") as f:
    dict = json.load(f)

    for i in l:
      artists_ids_by_names.append (dict[i]) 

  return artists_ids_by_names  
    

def get_albums(artistid): 
  a_url = "https://api.deezer.com/artist/{}".format(artistid)
  response = requests.get(a_url)
  response_json = response.json()
  a_album = response_json["nb_album"]
  return a_album

  

#main

cont_exec = True

while (cont_exec):

  artists_list_names = get_random_artists_names()
  first_artist_name = artists_list_names[0]
  second_artist_name = artists_list_names[1]

  artists_list_ids = get_random_artists_ids(artists_list_names)
  first_artist_id = artists_list_ids[0]
  second_artist_id = artists_list_ids[1]

  print("\n---------------------------\n")


  user_answer = input("Chi ha pubblicato più album tra {} (1) e {} (2)? ".format(first_artist_name, second_artist_name))


  artist_1_albums_n = get_albums(first_artist_id)
  artist_2_albums_n = get_albums(second_artist_id)


  if user_answer == "1":

    if artist_1_albums_n >= artist_2_albums_n:
      print ("Corretto, {} ha pubblicato {} album, mentre {} ne ha pubblicati {} ".format(first_artist_name, artist_1_albums_n, second_artist_name, artist_2_albums_n))
    else:
      print("Sbagliato, {} ha pubblicato {} album, mentre {} ne ha pubblicati {} ".format(first_artist_name, artist_1_albums_n, second_artist_name, artist_2_albums_n))

  elif user_answer == "2":

    if artist_1_albums_n <= artist_2_albums_n:
      print ("Corretto, {} ha pubblicato {} album, mentre {} ne ha pubblicati {} ".format(first_artist_name, artist_1_albums_n, second_artist_name, artist_2_albums_n))
    else: print("Sbagliato, {} ha pubblicato {} album, mentre {} ne ha pubblicati {} ".format(first_artist_name, artist_1_albums_n, second_artist_name, artist_2_albums_n))

  else:
    raise Exception("Inserisci una risposta valida")
    cont_exec= False

  user_answer = input("Vuoi continuare a giocare? (s/n) ")

  if user_answer.lower() == "n":
    cont_exec=False
  
