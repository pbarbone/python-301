# Use the Pokemon API at https://pokeapi.co/ to assemble a team of your
# six favorite Pokémon.
# Your task is to fetch information about six Pokémon through the
# necessary API calls and include the information in your local script.
# This information should include at least:
# - name
# - number
# - types
#
# You can improve on your project even more by writing the data to a small
# `.html` page which allows you to also display the sprites of each Pokémon.
# Check out the guides they provide: https://pokeapi-how.appspot.com/page5

BASE_URL = "https://pokeapi.co/api/v2/"

import requests

# get the data for the first 6 pokemon using the ability endpoint

for i in range(1, 7):
    response = requests.get(BASE_URL + f"pokemon/{i}")
    data = response.json()
    print(data['name'])
    print(data['id'])
    print(data['types'])
    print("\n")