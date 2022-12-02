import enum


class Winner(enum.Enum):
    DRAW = 0
    ME = 1
    OPPONENT = 2

    @classmethod
    def from_intent(cls, s: str) -> "Winner":
        return {"X": cls.OPPONENT, "Y": cls.DRAW, "Z": cls.ME}[s]

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
    def stance_points(cls, stance: "Stance") -> int:
        if stance == cls.ROCK:
            return 1
        elif stance == cls.PAPER:
            return 2
        else:
            return 3


def needed_stance(winner: Winner, opponent_stance: Stance) -> Stance:
    if winner == Winner.DRAW:
        return opponent_stance
    elif winner == Winner.OPPONENT:
        if opponent_stance == Stance.PAPER:
            return Stance.ROCK
        elif opponent_stance == Stance.ROCK:
            return Stance.SCISSORS
        else:
            return Stance.PAPER
    else:
        if opponent_stance == Stance.PAPER:
            return Stance.SCISSORS
        elif opponent_stance == Stance.ROCK:
            return Stance.PAPER
        else:
            return Stance.ROCK


def main():
    with open("input.txt", "r") as f:
        score = 0

        for line in (l.rstrip("\n") for l in f.readlines()):
            opponent, intent_str = line.split(" ")

            opponent_stance = Stance.from_opponent(opponent)
            intent = Winner.from_intent(intent_str)

            score += Stance.stance_points(
                needed_stance(intent, opponent_stance)
            ) + Winner.score(intent)

        print(score)


if __name__ == "__main__":
    main()
