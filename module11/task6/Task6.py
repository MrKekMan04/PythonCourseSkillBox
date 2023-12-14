from Entities import *


class Program:
    @staticmethod
    def main():
        player1 = Player("First Player", "X")
        player2 = Player("Second Player", "O")
        game = Game([player1, player2])

        while True:
            game.run_game()
            print(game.get_state())
            print("\n".join([f"{player.get_name()} has wins: {player.get_wins()}" for player in game.get_players()]))

            if input("Хотите продолжить? (y/n)").lower() != "y":
                break


if __name__ == '__main__':
    Program.main()
