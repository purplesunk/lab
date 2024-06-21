def split_players_into_teams(players):
    odd_team = players[1::2]
    even_team = players[::2]

    return even_team, odd_team
