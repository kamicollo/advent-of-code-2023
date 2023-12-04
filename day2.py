import re

game_id_pattern = re.compile('Game (\d+)')
game_detail_pattern = re.compile('\s*(\d+) ((green)|(blue)|(red))')

def parse_round(game):
    r = {'red': 0, 'blue': 0, 'green': 0}
    for balls in game.split(','):
        m = game_detail_pattern.match(balls) 
        r[m[2]] = int(m[1])    
    r['invalid'] = r['red'] > 12 or r['green'] > 13 or r['blue'] > 14            
    return r
    
def parse_games(text):
    game_text, game_details = text.split(":")
    game_id = game_id_pattern.match(game_text).group(1)
    rounds = game_details.split(';')
    parsed_rounds = [parse_round(r) for r in rounds]    
    r, b, g, _ = zip(*[r.values() for r in parsed_rounds])
    power = max(r) * max(b) * max(g)
    return {
        'id': int(game_id),
        'rounds': parsed_rounds,
        'power': power
    }    

with open('data/day2.txt', 'r') as f:
    games = [parse_games(line) for line in f.readlines()]


#part 1
valid_games_ids = [game['id'] for game in games if not any([r['invalid'] for r in game['rounds']])]    
print(sum(valid_games_ids))

#part 2
powers = [game['power'] for game in games]    
print(sum(powers))