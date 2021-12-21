import itertools

# input_data = (4, 8)
input_data = (8, 7)


class DeterministicDie:

    def __init__(self):
        self.results = iter(range(1, 101))
        self.rolls = 0

    def turn(self, player):
        moves = 0
        for _ in range(3):
            self.rolls += 1
            try:
                moves += next(self.results)
            except StopIteration:
                self.results = iter(range(1, 101))
                moves += next(self.results)
        for _ in range(moves):
            player.position += 1
            if player.position > 10:
                player.position = 1
        player.score += player.position
        return player.score


class QuantumDie:

    def __init__(self):
        self.results = list(itertools.product(*[[1, 2, 3]] * 3))
        self.cache = {}

    def turn(self, player1, player2):
        cache_key = player1, player2
        if cache_key in self.cache:
            return self.cache[cache_key]
        if player1.score >= 21:
            return 1, 0
        elif player2.score >= 21:
            return 0, 1
        p1_wins, p2_wins = 0, 0
        for (i, j, k) in self.results:
            position = player1.position
            for _ in (range(i + j + k)):
                position += 1
                if position > 10:
                    position = 1
            new_p2_wins, new_p1_wins = self.turn(
                player2, Player(position, player1.score + position)
            )
            p1_wins += new_p1_wins
            p2_wins += new_p2_wins
        self.cache[cache_key] = p1_wins, p2_wins
        return p1_wins, p2_wins


class Player:

    def __init__(self, start, score=0):
        self.position = start
        self.score = score

    def __hash__(self):
        return hash((self.position, self.score))

    def __eq__(self, other):
        return self.position == other.position and self.score == other.score

    def __ne__(self, other):
        return self.position != other.position or self.score != other.score

    def __repr__(self):
        return f"<Player p={self.position} s={self.score}>"


def part_1(player_1_start, player_2_start):
    die = DeterministicDie()
    player_1 = Player(player_1_start)
    player_2 = Player(player_2_start)
    while True:
        score = die.turn(player_1)
        if score >= 1000:
            return player_2.score * die.rolls
        score = die.turn(player_2)
        if score >= 1000:
            return player_1.score * die.rolls


def part_2(player_1_start, player_2_start):
    die = QuantumDie()
    player_1 = Player(player_1_start)
    player_2 = Player(player_2_start)
    player_1_wins, player_2_wins = die.turn(player_1, player_2)

    return max(player_1_wins, player_2_wins)


if __name__ == '__main__':
    print(part_1(*input_data))
    print(part_2(*input_data))
