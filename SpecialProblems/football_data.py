football_data = [
  { 'winner': 'Alice', 'loser': 'Bob',   'loser_points': 3 },
  { 'winner': 'Carol', 'loser': 'Dean',  'loser_points': 1 },
  { 'winner': 'Elise', 'loser': 'Bob',   'loser_points': 2 },
  { 'winner': 'Elise', 'loser': 'Carol', 'loser_points': 4 },
  { 'winner': 'Alice', 'loser': 'Carol', 'loser_points': 2 },
  { 'winner': 'Carol', 'loser': 'Dean',  'loser_points': 3 },
  { 'winner': 'Dean',  'loser': 'Elise', 'loser_points': 2 },
]

def list_players():
    players = []
    for line in football_data:
        if line['winner'] not in players:
            players.append(line['winner'])
        if line['loser'] not in players:
            players.append(line['loser'])
    return players

def participant_wins(players):
    wins = {}
    for player in players:
        wins[player] = []
    print(wins)

    for line in football_data:
        value_win = line['winner']
        value_loser = line['loser']
        if value_loser not in wins[value_win]:
            wins[value_win].append(value_loser)

    print(wins)

if __name__ == '__main__':
    players = list_players()
    participant_wins(players)