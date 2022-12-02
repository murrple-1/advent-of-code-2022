import enum


class Winner(enum.Enum):
    DRAW = 0
    ME = 1
    OPPONENT = 2

    @classmethod
    def score(cls, winner: "Winner") -> int:
        if winner == cls.DRAW:
            return 3
        elif winner == cls.ME:
            return 6
        else:
            return 0


class Stance(enum.Enum):
    ROCK = 0
    PAPER = 1
    SCISSORS = 2

    @classmethod
    def from_opponent(cls, s: str) -> "Stance":
        return {"A": cls.ROCK, "B": cls.PAPER, "C": cls.SCISSORS}[s]

    @classmethod
    def from_me(cls, s: str) -> "Stance":
        return {"X": cls.ROCK, "Y": cls.PAPER, "Z": cls.SCISSORS}[s]

    @staticmethod
    def who_wins(my_stance: "Stance", opponent_stance: "Stance") -> Winner:
        if my_stance == opponent_stance:
            return Winner.DRAW
        else:
            if my_stance == Stance.ROCK:
                return (
                    Winner.ME if opponent_stance == Stance.SCISSORS else Winner.OPPONENT
                )
            elif my_stance == Stance.PAPER:
                return Winner.ME if opponent_stance == Stance.ROCK else Winner.OPPONENT
            else:
                return Winner.ME if opponent_stance == Stance.PAPER else Winner.OPPONENT

    @classmethod
    def stance_points(cls, stance: "Stance") -> int:
        if stance == cls.ROCK:
            return 1
        elif stance == cls.PAPER:
            return 2
        else:
            return 3


def main():
    with open("input.txt", "r") as f:
        score = 0

        for line in (l.rstrip("\n") for l in f.readlines()):
            opponent, me = line.split(" ")

            opponent_stance = Stance.from_opponent(opponent)
            my_stance = Stance.from_me(me)

            score += Stance.stance_points(my_stance) + Winner.score(
                Stance.who_wins(my_stance, opponent_stance)
            )

        print(score)


if __name__ == "__main__":
    main()
