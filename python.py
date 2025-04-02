import requests

print('Enter Pokemon name or ID:')
pokemon = input()

def get_posts(pokemon):
    url = 'https://pokeapi.co/api/v2/pokemon/' + pokemon

    try:

        response = requests.get(url)


        if response.status_code == 200:
            posts = response.json()
            return posts
        else:
            print('Error:', response.status_code)
            return None
    finally:
        print(' ')
data = get_posts(pokemon)
hp = data['stats'][0]['base_stat']
attack = data['stats'][1]['base_stat']
defence = data['stats'][2]['base_stat']
special_attack = data['stats'][3]['base_stat']
special_defence = data['stats'][4]['base_stat']
speed = data['stats'][5]['base_stat']
print ('Name: ' + data['name'])

print('Type: ' + data['types'][0]['type']['name'])

print('Ability: ' + data['abilities'][0]['ability']['name'])

print('HP:',hp)

print('Attack:',attack)

print('Defence:',defence)

print('Special Attack:',special_attack)

print('Special Defence:',special_defence)

print('Speed:',speed)


