from abc import abstractmethod, ABC
import re

class User:

    username: str = ""
    password: str = ""
    color: bool = False
    users: list = []
    
    def __init__(self, username, password) -> None:
        self.username = username
        self.password = password
    

    def __eq__(self, other: object) -> bool:
        if isinstance(other, User):
            return self.username == other.username
        elif isinstance(other, str):
            return self.username == other


    def print_command_list():
        commands = """
        register [username] [password]
        login [username] [password]
        remove [username] [password]
        list_users
        help
        exit
        """
        print(commands)

    @staticmethod
    def is_valid(string: str):
        if re.match(r'^[\w|\d][A-Za-z0-9_-]+$', string):
            return True

        
    @staticmethod
    def is_username_exist(username):
        return username in User.users


    @staticmethod
    def add_user(username, password):

        if User.is_valid(username) == False:
            print("username format is invalid")
            return
        if User.is_valid(password) == False:
            print("password format is invalid")
            return
        if User.is_username_exist(username):
            print("a user exists with this username")
            return

        u = User(username, password)
        User.users.append(u)
        print("register successful")
    
    
    @staticmethod
    def remove_user(username, password):
        if User.is_valid(username) == False:
            print("username format is invalid")
            return
        if User.is_valid(password) == False:
            print("password format is invalid")
            return

        
class Chess:

    def print_board(self, board):
        row_number = 8
        print("  ", end="")

        for row in board:
            print(row_number, end=" ")
            row_number -= 1
            for cell in row:
                print("| {} ".format(cell), end="")
            print("|")
            print("  ", end="")

        print("  ", end="")
        for letter in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']:
            print("  {}  ".format(letter), end="  ")
        print("")


    def initialize(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.board[1] = [Pawn("P", "B", x, 7) for x in range(1, 9)]
        self.board[6] = [Pawn("P", "W", x, 2) for x in range(1, 9)]
        self.print_board(self.board)


class Piece(ABC):
    name = ""
    color = ""
    x = 0
    y = 0

    def __init__(self,name,color,x,y):
        self.name = name
        self.color = color
        self.x = x
        self.y = y

    def __repr__(self):
        return self.color + self.name

    @abstractmethod
    def move(self, x, y):
        pass


class Pawn(Piece):

    def __init__(self, name, color, x, y):
        super().__init__(name, color, x, y)

    def move(self, x, y):
        print("pawn")
        pass


class Rook(Piece):

    def move(self, x, y):
        print("rook")
        pass


class Knight(Piece):

    def move(self, x, y):
        pass


class Bishop(Piece):

    def move(self, x, y):
        pass


class Queen(Piece):

    def move(self, x, y):
        pass


class King(Piece):

    def move(self, x, y):
        pass


while True:
    user_inp = input("").strip().split()

    if user_inp == "exit":
        break

    if user_inp[0] == "help":
        User.print_command_list()

    if len(user_inp) != 3:
        print("invalid command")
        continue

    if user_inp[0] == "register":
        User.add_user(user_inp[1], user_inp[2])
    else:
        print(f"invalid command <{user_inp[0]}>")


