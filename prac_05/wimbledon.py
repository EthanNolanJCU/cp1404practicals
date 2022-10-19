"""
Practical 05
Wimbledon.py
Takes .csv file as input, stores data from it and displays player
"""
SCORES_INDEX = 1



def main():
    file_name = "wimbledon.csv"
    all_wimbledon_data = getData(file_name)
    players_to_wins = playerWins(all_wimbledon_data)
    winning_countries = winningCountries(all_wimbledon_data)
    output(players_to_wins, winning_countries)


def getData(file_name):
    file_handler = open(file_name, 'r', encoding="utf-8-sig")
    file_handler.readline()  # Remove header
    data = []
    for line in file_handler.readlines():
        line = line.strip().split('"')
        score = line[SCORES_INDEX]
        line = line[0].split(",") # Splits starting data and adds scores onto end
        line[-1] = score # Replace empty
        data.append(line)
    file_handler.close()
    print(data)
    return data


def playerWins(data):
    player_to_wins = dict()
    for line in data:
        try:
            player_to_wins[line[2]] += 1
        except:
            player_to_wins[line[2]] = 1
    return player_to_wins


def winningCountries(data):
    winning_countries = set()
    for line in data:
        winning_countries.add(line[1])
    return winning_countries


def output(player_to_wins, winning_countries):
    max_name_length = max(len(name) for name in player_to_wins.keys())
    for name, win in player_to_wins.items():
        print(f"{name:<{max_name_length}} : {win}")
    print(f"\nThese {len(winning_countries)} have won wimbledon: ")
    print(f"{', '.join(winning_countries)}")


main()
