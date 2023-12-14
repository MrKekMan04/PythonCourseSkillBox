class Player:
    def __init__(self, name: str, symbol: str) -> None:
        self.name = name
        self.wins_count = 0
        self.symbol = symbol

    def make_move(self) -> (int, int):
        while True:
            move = tuple(map(int, input(
                f"{self.get_name()}, введите индексы клетки чарез пробел в формате (строка столбец): ").split()))

            if len(move) == 2:
                return move
            else:
                print("Попробуйте снова!")

    def increment_win(self) -> None:
        self.wins_count += 1

    def get_name(self) -> str:
        return self.name

    def get_symbol(self) -> str:
        return self.symbol

    def get_wins(self) -> int:
        return self.wins_count


class Cell:
    def __init__(self) -> None:
        self.symbol = " "

    def is_empty(self) -> bool:
        return self.symbol == " "

    def place(self, symbol) -> bool:
        if self.is_empty():
            self.symbol = symbol
            return True
        return False

    def get_symbol(self) -> str:
        return self.symbol


class Board:
    def __init__(self, size: int, streak_for_win: int) -> None:
        self.size = size
        self.symbols_to_win = streak_for_win
        self.cells = self.generate_board()

    def generate_board(self) -> list[list[Cell]]:
        return [[Cell() for _ in range(self.size)] for _ in range(self.size)]

    def clear(self) -> None:
        self.cells = self.generate_board()

    def put_symbol(self, symbol: str, row: int, column: int) -> bool:
        if self.size > row >= 0 or self.size > column <= 0:
            return self.cells[row][column].place(symbol)
        return False

    def check_win(self, symbol: str, row: int, column: int) -> bool:
        return (all([self.cells[row][column + k].get_symbol() == symbol for k in range(self.symbols_to_win)])
                or all([self.cells[row + k][column].get_symbol() == symbol for k in range(self.symbols_to_win)])
                or all([self.cells[row + k][column + k].get_symbol() == symbol for k in range(self.symbols_to_win)]))

    def is_win(self, symbol: str) -> bool:
        for i in range(self.size - self.symbols_to_win + 1):
            for j in range(self.size - self.symbols_to_win + 1 - i):
                if (self.check_win(symbol, i + j, i)
                        or self.check_win(symbol, i, i + j)
                        or self.check_win(symbol, i + j, i + j)):
                    return True
        return False

    def has_empty_cell(self) -> bool:
        return any(self.cells[row][column].is_empty() for row in range(self.size) for column in range(self.size))


class Game:
    def __init__(self, players: list[Player], board_size: int = 3, streak_for_win: int = 3) -> None:
        self.state = "Created"
        self.players = players
        self.board = Board(board_size, streak_for_win)
        self.current_player_move = 0
        self.move = 0

    def run_move(self) -> bool:
        current_player = self.players[self.current_player_move]
        player_symbol = current_player.get_symbol()
        move = current_player.make_move()

        if self.board.put_symbol(player_symbol, *move):
            self.current_player_move = (self.current_player_move + 1) % len(self.players)
            self.move += 1
            self.state = f"Playing. Move: {self.move}"
            if self.board.is_win(player_symbol):
                current_player.increment_win()
                self.state = f"Ended. {current_player.name} Win!"
                return True
            return False
        print(f"Сделан неправильный ход! Следующий ход остается за {current_player.name}")
        return False

    def run_game(self) -> bool:
        self.board.clear()

        while True:
            if self.run_move():
                return True
            if not self.board.has_empty_cell():
                self.state = "Draw!"
                return False

    def get_state(self) -> str:
        return self.state

    def get_players(self) -> list[Player]:
        return self.players
