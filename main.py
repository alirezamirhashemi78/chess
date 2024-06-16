from abc import abstractmethod, ABC
import re
import sys
import random
import time

random.seed(time.time())

class CoordinateUtility:
    @staticmethod
    def index_to_cartesian(r, c):
        y = 8 - r
        x = c + 1
        return (x, y)

    @staticmethod
    def cartesian_to_index(x, y):
        r = 8 - y
        c = x - 1
        return (r, c)


class Piece(ABC):
    name = ""
    color = ""
    x = 0
    y = 0

    def __init__(self, name, color, x, y):
        self.name = name
        self.color = color
        self.x = x
        self.y = y

    def __repr__(self):
        return self.name  + self.color 

    @abstractmethod
    def move(self, x, y):
        pass


class Pawn(Piece):

    def __init__(self, color, x, y):
        super().__init__("P", color, x, y)

    def move(self, x, y):
        print("pawn")
        pass


class Rook(Piece):

    def __init__(self, color, x, y):
        super().__init__("R", color, x, y)


    def change_piece_coordination(self, start_r, end_r, start_c, end_c,  board):
        board[end_r][end_c] = board[start_r][start_c]
        board[start_r][start_c] = None
        x, y = CoordinateUtility.index_to_cartesian(end_r, end_c)
        self.x = x
        self.y = y


    def performe_movement(self,  start_r, end_r, start_c, end_c,  board, spots):
        can_move = not any(spots)
        destination_piece = board[end_r][end_c]
        source_piece = board[start_r][start_c]

        if can_move == False:
            print('cannot move to the spot')
            return

        if destination_piece is None:
            self.change_piece_coordination(start_r, end_r, start_c, end_c,  board)
            print('moved')

        if (destination_piece is not None ) and (source_piece.color == destination_piece.color):
            print('cannot move to the spot')

        elif (destination_piece is not None ) and (source_piece.color != destination_piece.color):
            self.change_piece_coordination(start_r, end_r, start_c, end_c,  board)
            print('rival piece destroyed')


    def move_vertical(self, start_r, end_r, start_c, end_c,  board):
        move_range = start_r - end_r
        if move_range > 0:
            spots = [board[start_r - i][start_c] for i in range(1, move_range)]
        else:
            move_range = abs(move_range)
            spots = [board[start_r + i][start_c] for i in range(1, move_range)]

        self.performe_movement(start_r, end_r, start_c, end_c,  board, spots)

    
    def move_horizontal(self, start_r, end_r, start_c, end_c,  board):
        move_range = start_c - end_c
        if move_range > 0:
            spots = [board[start_r][start_c - i] for i in range(1, move_range)]
        else:
            move_range = abs(move_range)
            spots = [board[start_r][start_c + i] for i in range(1, move_range)]

        self.performe_movement(start_r, end_r, start_c, end_c,  board, spots)


    def move(self, x, y, board):
        start_r, start_c = CoordinateUtility.cartesian_to_index(self.x, self.y)
        end_r, end_c = CoordinateUtility.cartesian_to_index(x, y)

        if self.x == x and self.y == y:
            print("cannot move to the spot")

        elif self.x == x:
            self.move_vertical(start_r, end_r, start_c, end_c,  board)

        elif self.y == y:
            self.move_horizontal(start_r, end_r, start_c, end_c,  board)

        else:
            print("cannot move to the spot 5")



class Bishop(Piece):
    def __init__(self, color, x, y):
        super().__init__("B", color, x, y)

    def move(self, x, y):
        start_r, start_c = CoordinateUtility.cartesian_to_index(self.x, self.y)
        end_r, end_c = CoordinateUtility.cartesian_to_index(x, y)

        if self.x == x and self.y == y:
            print("cannot move to the spot")



class Knight(Piece):

    def __init__(self, color, x, y):
        super().__init__("N", color, x, y)


    def move(self, x, y):
        pass



class Queen(Piece):
    def __init__(self, color, x, y):
        super().__init__("Q", color, x, y)

    def move(self, x, y, board):
        pass



class King(Piece):
    def __init__(self, color, x, y):
        super().__init__("K", color, x, y)

    def move(self, x, y):
        pass



class User:

    username: str = ""
    password: str = ""
    limit: int = None
    score = 0
    wins = 0
    draws = 0
    loses = 0
    color: bool = False
    users: list = []    


    def __init__(self, username, password) -> None:
        self.username = username
        self.password = password
        self.score = 0
        self.wins = 0
        self.draws = 0
        self.loses = 0


    def __eq__(self, other: object) -> bool:
        if isinstance(other, User):
            return self.username == other.username and self.password == other.password
        elif isinstance(other, str):
            return self.username == other
        # elif isinstance(other, )
        

    @staticmethod
    def list_users():
        sorted_users = sorted(User.users, key=lambda x:x.username.lower())
        for user in sorted_users:
            print(f"{user.username} {user.password}")
            

    @staticmethod
    def is_valid(string: str):
        if not string.isascii():
            return False
        if re.findall(r"\W", string):
            return False
  
        
    @staticmethod
    def is_username_exist(username):
        return username in User.users


    @staticmethod
    def is_user_exist(user):
        return user in User.users


    @staticmethod
    def check_validations(username="", password=""):

        if username and User.is_valid(username) == False:
            print("username format is invalid")
            return False

        if password and User.is_valid(password) == False:
            print("password format is invalid")
            return False
        
        return True


    @staticmethod
    def add_user(username, password):

        if not User.check_validations(username, password):
            return

        if User.is_username_exist(username):
            print("a user exists with this username")
            return

        u = User(username, password)
        User.users.append(u)
        print("register successful")
    

    @staticmethod
    def login(chess: object, username: str, password: str):
        if not User.check_validations(username, password):
            return

        u = User(username, password)

        if not username in User.users:
            print("no user exists with this username")
            return

        if u in User.users:
            chess.white_user = u
            print("login successful")

        else:
            print("incorrect password")
            

    @staticmethod
    def logout(chess: object):
        chess.white_user = None
        chess.black_user = None
        print("logout successful")
    

    @staticmethod
    def remove_user(username, password):

        if not User.check_validations(username, password):
            return
        
        u = User(username, password)
        if u in User.users:
            User.users.remove(u)
            print(f"removed {username} successfully")
        elif u.username not in User.users:
            print("no user exists with this username")
        elif u.username in User.users and password not in User.users:
            print("incorrect password")


    @staticmethod
    def forfeit(chess: object):
        black_user = User.users[User.users.index(chess.black_user)]
        white_user = User.users[User.users.index(chess.white_user)]

        if chess.white_turn:
            black_user.score += 2
            
            if white_user.score > 0:
                white_user.score -= 1
            print("you have forefit")
            print(f"player {black_user.username} with color black won")
            chess.black_user = None
            return
        white_user.score += 2
        if black_user.score > 0:
            black_user.score -= 1
        print("you have forefit")
        print(f"player {black_user.username} with color black won")

        return


class Chess:

    white_user: User = None
    black_user: User = None
    white_turn: bool = True
    black_turn: bool = False
    selected_piece: object = None
    limit: int = None
    board: list = []

    first_layer_menue: str = """
        register [username] [password]
        login [username] [password]
        remove [username] [password]
        list_users
        help
        exit
        """

    second_layer_menue: str = """
        new_game [username] [limit]
        scoreboard
        list_users
        help
        logout
        """

    game_menue: str = """
        select [x],[y]
        deselect
        move [x],[y]
        next_turn
        show_turn
        undo
        undo_number
        show_moves [-all]
        show_killed [-all]
        show_board
        help 
        forfeit
        """


    def __init__(self, white_user, black_user, limit):
        self.white_user = white_user
        self.black_user = black_user
        self.limit = limit


    def initialize(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]

        # White pieces
        self.board[6] = [Pawn( "w", x, 2) for x in range(1, 9)]
        self.board[7][0] = Rook("w", 1, 1)
        self.board[7][1] = Knight("w", 2, 1)
        self.board[7][2] = Bishop("w", 3, 1)
        self.board[7][3] = Queen("w", 4, 1)
        self.board[7][4] = King("w", 5, 1)
        self.board[7][5] = Bishop( "w", 6, 1)
        self.board[7][6] = Knight("w", 7, 1)
        self.board[7][7] = Rook( "w", 8, 1)

        # Black pieces
        self.board[1] = [Pawn("b", x, 7) for x in range(1, 9)]
        self.board[0][0] = Rook( "b", 1, 8)
        self.board[0][1] = Knight( "b", 2, 8)
        self.board[0][2] = Bishop("b", 3, 8)
        self.board[0][3] = Queen( "b", 4, 8)
        self.board[0][4] = King( "b", 5, 8)
        self.board[0][5] = Bishop( "b", 6, 8)
        self.board[0][6] = Knight( "b", 7, 8)
        self.board[0][7] = Rook( "b", 8, 8)


    def get_free_locations(self) :
        locations = []
        for i in range(8):
            for j in range(8):
                if self.board[j][i] is None:
                    locations.append((i,j))
        return locations


    def random_board(self, count = 10, preferable_piece = Rook):
        self.board = [[None for _ in range(8)] for _ in range(8)]

        for _ in range(count) :
            locations = self.get_free_locations()
            rnd = random.randint(0,len(locations)-1)
            r ,c  = locations[rnd]
            x, y = CoordinateUtility.index_to_cartesian(r,c)
            if random.uniform(0,1) > .3:
                self.board[r][c] = preferable_piece("w" if random.uniform(0,1) > .5 else "b", x, y)
                self.selected_piece = self.board[r][c]
            else :
                self.board[r][c] = Pawn("w" if random.uniform(0,1) > .5 else "b", x, y)
                    

    def print_commands(commands):
        for i, command in enumerate(commands.strip().split("\n")):
            print(f"{i+1}. {command.strip()}")


    @staticmethod
    def get_command_list(chess):
        if chess.white_user == None:
            Chess.print_commands(Chess.first_layer_menue)
        elif chess.white_user != None and chess.black_user == None:
            Chess.print_commands(Chess.second_layer_menue)
        elif chess.white_user != None and chess.black_user != None:
            Chess.print_commands(Chess.game_menue)


    def print_board(self):
        board = [ 
            '|'.join([   "  " if piece is  None else  str(piece) if piece is not self.selected_piece else "\033[0;31m" + str(piece) + "\033[0m" for piece in row ])
            for row in self.board
        ]
        print(*board, sep="|\n", end="|\n")

        
    def check_game_limit(self, limit: int):
        if limit < 0:
            print("number should be positive to have a limit or 0 for no limit")


    def start_new_game(self, username, limit):
        User.check_validations(username)
        self.check_game_limit(int(limit))

        if username == self.white_user.username:
            message = "you must choose another player to start a game"

        if User.is_username_exist(username):
            self.black_user = User.users[User.users.index(username)]
            self.limit = limit
            message = f"new game started successfully between {self.white_user.username} and {self.black_user.username} with limit {self.limit}"

        else:
            message = "no user exists with this username"
        
        print(message)


    def print_scoreboard(self):
        message = f"[username] [score] [wins] [draws] [loses]"
        print(message)
        pass
    

    @staticmethod
    def is_piece_selectable(chess: object, piece: object):
        if chess.white_turn:
            if piece.color != "w":
                message = "you can only select one of your pieces"
                print(message)
                return False
            else:
                return True
        else:
            if piece.color != "b":
                message = "you can only select one of your pieces"
                print(message)
                return False
            else:
                return True
           

    @staticmethod
    def is_cordination_none(piece):
        if piece is None:
            return True
        

    @staticmethod
    def select_position(chess: object, x: int, y: int):

        piece = None
        x, y = CoordinateUtility.cartesian_to_index(x, y)
        x, y = int(x), int(y)
        if (0 <= x <= 7 and 0 <= y <= 7):

            piece = chess.board[x][y]
        else:
            message = "wrong coordination"
            print(message)
            return

        if chess.is_cordination_none(piece):
            message = "no piece on this spot"

        elif chess.is_piece_selectable(chess, piece):
            chess.selected_piece = piece
            message = "selected"

        print(message)
        return
    

    def deselect(self):
        if self.selected_piece is None:
            message = "no piece is selected"
        else:
            self.selected_piece = None
            message = "deselected"

        print(message)
        return
    

    def move(self):
        pass
        

first_layer_menu = ["register", "login", "remove", "list_users", "help", "exit"]
second_layer_menu = ["new_game", "scoreboard", "list_users", "help", "logout"]


chess = Chess(None, None, limit=0)
# chess.random_board()
# chess.print_board()
# while True:
#     parts = input().strip().split()
#     if parts[0] == "move" :

#         x , y = list(map (int , parts[1:]))

#         if chess.selected_piece == None:
#             print("do not have any selected piece")

#         if (1 <= x <= 8 and 1 <= y <= 8):
#             chess.selected_piece.move(x, y, chess.board)
#         else:
#             print("wrong coordination")


#         chess.print_board()
#     elif parts[0] =="randomize" :
#         chess.random_board()
#     elif parts[0] == "print" :
#         chess.print_board()
#     elif parts[0] == "end" :
#         break


chess.initialize()
chess.print_board()

args = sys.argv[1:]

if "in" in args:
    fin = open("inputs.txt")
    sys.stdin = fin

elif "out" in args:
    fout = open("results", "wt")
    sys.stdout = fout



while True:

    user_inp = input("").strip().split()

    # global menu
    if user_inp[0] == "list_users":
        User.list_users()

    if user_inp[0].strip() == "exit":
        print("program ended")
        break

    if user_inp[0] == "help":
        Chess.get_command_list(chess)
    
    if user_inp[0] in ["register", "login", "remove"] and len(user_inp) != 3:
        print("invalid command")
        continue

    if not isinstance(chess.white_user, User):
        # first layer menu

        if user_inp[0] not in first_layer_menu:
            print("invalid command")

        if user_inp[0] == "register" and len(user_inp) == 3:
            User.add_user(user_inp[1], user_inp[2])

        if user_inp[0] == "login":
            User.login(chess, user_inp[1], user_inp[2])
    
        if user_inp[0] == "remove":
            User.remove_user(user_inp[1], user_inp[2])


    elif isinstance(chess.white_user, User):
        # second layer menu
        if user_inp[0] == "new_game":
            chess.start_new_game(user_inp[1], user_inp[2])
        
        if user_inp[0] == "scoreboard":
            chess.print_scoreboard()
        
        if user_inp[0] == "logout":
            User.logout(chess)

        # game menu
        if user_inp[0] == "select":
            x, y = user_inp[1].split(",")
            print(x, "Y: ", y)
            chess.select_position(chess, x=int(x), y=int(y))
        
        if user_inp[0] == "move":
            # x, y = CoordinateUtility.cartesian_to_index(int(user_inp[1]), int(user_inp[2]))

            x, y = user_inp[1].split(",")
            print("X: ", x, y)
            chess.selected_piece.move(int(x), int(y), chess.board)
            
        if user_inp[0] == "deselect":
            chess.deselect()

        if user_inp[0] == "forfeit":
            User.forfeit(chess)
        
    


