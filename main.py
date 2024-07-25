from abc import abstractmethod, ABC
from dataclasses import replace
import re
import sys
import random
import time
from turtle import right

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


    def replace_piece(self, board, x, y):
        start_r, start_c = CoordinateUtility.cartesian_to_index(self.x, self.y)
        end_r, end_c = CoordinateUtility.cartesian_to_index(x, y)
        # if board[end_r][end_c] != None: 
        #     chess.destroyed_piece.append(board[end_r][end_c])
        board[end_r][end_c] = board[start_r][start_c]
        board[start_r][start_c] = None
        x, y = CoordinateUtility.index_to_cartesian(end_r, end_c)
        self.x = x
        self.y = y


    def move(self, x, y, board):
        # pawn_line = 2 if self.color == "w" else 7
        start_r, start_c = CoordinateUtility.cartesian_to_index(self.x, self.y)
        end_r, end_c = CoordinateUtility.cartesian_to_index(x, y)
        pawn = board[start_r][start_c]
        can_destroy_left = False
        can_destroy_right = False

        if pawn.color == "w":
            # checks pawn going forward
            if y <= self.y:
                print("cannot move to the spot 1")
                return
            if not -1 <= x - self.x <= 1:
                print("cannot move to the spot 2")
                return
            # checks if white pawn can destroy right
            if self.x < 8:
                if (right_side := board[start_r - 1][start_c + 1]) is not None:
                    if right_side.color != pawn.color:
                        can_destroy_right = True
            # checks if white pawn can destroy left
            if self.x > 1:
                if (left_side := board[start_r - 1][start_c - 1]) is not None:
                    if left_side.color != pawn.color:
                        can_destroy_left = True

            # if pawn didnt move
            if self.y == 2:
                if x == self.x:
                    if board[end_r][end_c] is not None:
                        print("cannot move to the spot 3")
                        return
                    elif y - self.y <= 2:
                        self.replace_piece(board, x, y)
                        print('moved')
                        return True
                    else:
                        print("cannot move to the spot 4")
                        return
                elif can_destroy_right and x - self.x == 1:
                    self.replace_piece(board, x, y)
                    print('rival piece destroyed')
                    return True

                elif can_destroy_left and x - self.x == -1:
                    self.replace_piece(board, x, y)
                    print('rival piece destroyed')
                    return True
                else:
                    print("cannot move to the spot 5")
                    return
            # if pawn moved
            else:
                if x == self.x:
                    if board[end_r][end_c] is not None:
                        print("cannot move to the spot 6")
                        return
                    elif y - self.y == 1:
                        self.replace_piece(board, x, y)
                        print('moved')
                        return True
                    else:
                        print("cannot move to the spot 7")
                        return
                elif can_destroy_right and x - self.x == 1:
                    self.replace_piece(board, x, y)
                    print('rival piece destroyed')
                    return True
                elif can_destroy_left and x - self.x == -1:
                    self.replace_piece(board, x, y)
                    print('rival piece destroyed')
                    return True
                else:
                    print("cannot move to the spot 8")
                    return


        elif pawn.color == "b":
            # checks pawn going forward
            if y >= self.y:
                print("cannot move to the spot 9")
                return
            if not -1 <= x - self.x <= 1:
                print(x, self.x)
                print("cannot move to the spot 10")
                return
            # checks if white pawn can destroy right
            if self.x < 8:
                if (right_side := board[start_r + 1][start_c + 1]) is not None:
                    if right_side.color != pawn.color:
                        can_destroy_right = True
            # checks if white pawn can destroy left
            if self.x > 1:
                if (left_side := board[start_r + 1][start_c - 1]) is not None:
                    if left_side.color != pawn.color:
                        can_destroy_left = True


            # if pawn didnt move
            if self.y == 7:
                if x == self.x:
                    if board[end_r][end_c] is not None:
                        print("cannot move to the spot 11")
                        return
                    elif self.y - y <= 2:
                        self.replace_piece(board, x, y)
                        print('moved')
                        return True
                    else:
                        print("cannot move to the spot 12")
                        return
                elif can_destroy_right and x - self.x == 1:
                    self.replace_piece(board, x, y)
                    print('rival piece destroyed')
                    return True
                elif can_destroy_left and x - self.x == -1:
                    self.replace_piece(board, x, y)
                    print('rival piece destroyed')
                    return True
                else:
                    print("cannot move to the spot 13")
                    return
            # if pawn moved
            else:
                if x == self.x:
                    if board[end_r][end_c] is not None:
                        print("cannot move to the spot 14")
                        return
                    elif self.y - y == 1:
                        self.replace_piece(board, x, y)
                        print('moved')
                        return True
                    else:
                        print("cannot move to the spot 15")
                        return
                elif can_destroy_right and x - self.x == 1:
                    self.replace_piece(board, x, y)
                    print('rival piece destroyed')
                    return True
                elif can_destroy_left and x - self.x == -1:
                    self.replace_piece(board, x, y)
                    print('rival piece destroyed')
                    return True
                else:
                    print("cannot move to the spot 16")
                    return


class Rook(Piece):

    def __init__(self, color, x, y):
        super().__init__("R", color, x, y)


    def replace_piece(self, board, x, y):
        start_r, start_c = CoordinateUtility.cartesian_to_index(self.x, self.y)
        end_r, end_c = CoordinateUtility.cartesian_to_index(x, y)
        board[end_r][end_c] = board[start_r][start_c]
        board[start_r][start_c] = None
        x, y = CoordinateUtility.index_to_cartesian(end_r, end_c)
        self.x = x
        self.y = y


    def move(self, x, y, board):
        start_r, start_c = CoordinateUtility.cartesian_to_index(self.x, self.y)
        end_r, end_c = CoordinateUtility.cartesian_to_index(x, y)   
        destination = board[end_r][end_c]

        if self.x == x and self.y == y:
            print("cannot move to the spot 17")

        elif self.x == x:
            move_range = start_r - end_r
            if move_range > 0:
                spots = [board[start_r - i][start_c] for i in range(1, move_range)]
            else:
                move_range = abs(move_range)
                spots = [board[start_r + i][start_c] for i in range(1, move_range)]

        elif self.y == y:
            move_range = start_c - end_c
            if move_range > 0:
                spots = [board[start_r][start_c - i] for i in range(1, move_range)]
            else:
                move_range = abs(move_range)
                spots = [board[start_r][start_c + i] for i in range(1, move_range)]

        else:
            print("cannot move to the spot 18")


        is_path_empty = not any(spots)
        if not is_path_empty:
            print('cannot move to the spot 19')
            return

        if destination == None:
            self.replace_piece(board, x, y)
            print('moved')
            return True

        if destination != None and board[start_r][start_c].color == destination.color:
            print('cannot move to the spot 20')
            
        elif destination != None and board[start_r][start_c].color != destination.color:
            self.replace_piece(board, x, y)
            print('rival piece destroyed')
            return True



class Bishop(Piece):

    def __init__(self, color, x, y):
        super().__init__("B", color, x, y)

    def replace_piece(self, board, x, y):
        start_r, start_c = CoordinateUtility.cartesian_to_index(self.x, self.y)
        end_r, end_c = CoordinateUtility.cartesian_to_index(x, y)
        board[end_r][end_c] = board[start_r][start_c]
        board[start_r][start_c] = None
        x, y = CoordinateUtility.index_to_cartesian(end_r, end_c)
        self.x = x
        self.y = y

    #TODO: functions
    def move(self, x, y, board):
        start_r, start_c = CoordinateUtility.cartesian_to_index(self.x, self.y)
        end_r, end_c = CoordinateUtility.cartesian_to_index(x, y)
        x_range = x - self.x
        y_range = y - self.y
        destination = board[end_r][end_c]
        move_range = abs(x_range)

        if x == self.x or y == self.y:
            print('cannot move to the spot 21')
            return
        elif abs(x_range) != abs(y_range):
            print('cannot move to the spot 22')
            return

        # bala rast
        elif 0 < x_range and 0 < y_range:
            spots = [board[start_r - i][start_c + i] for i in range(1, move_range)]
        # bala chap
        elif x_range < 0 < y_range:
            spots = [board[start_r - i][start_c - i] for i in range(1, move_range)]
        # pain rast
        elif y_range < 0 < x_range:
            spots = [board[start_r + i][start_c + i] for i in range(1, move_range)]
        # pain chap
        elif x_range < 0 and y_range < 0:
            spots = [board[start_r + i][start_c - i] for i in range(1, move_range)]
        else:
            print('cannot move to the spot 23')
            return

        is_path_empty = not any(spots)
        if not is_path_empty:
            print('cannot move to the spot 24')
            return
    
        if destination == None:
            self.replace_piece(board, x, y)
            print('moved')
            return True

        elif destination != None and board[start_r][start_c].color == destination.color:
            print('cannot move to the spot 25')
        elif destination != None and board[start_r][start_c].color != destination.color:
            self.replace_piece(board, x, y)
            print('rival piece destroyed')
            return True

            

class Queen(Piece):
    def __init__(self, color, x, y):
        super().__init__("Q", color, x, y)
        
    def replace_piece(self, board, x, y):
        start_r, start_c = CoordinateUtility.cartesian_to_index(self.x, self.y)
        end_r, end_c = CoordinateUtility.cartesian_to_index(x, y)
        board[end_r][end_c] = board[start_r][start_c]
        board[start_r][start_c] = None
        x, y = CoordinateUtility.index_to_cartesian(end_r, end_c)
        self.x = x
        self.y = y


    def move(self, x, y, board):
        start_r, start_c = CoordinateUtility.cartesian_to_index(self.x, self.y)
        end_r, end_c = CoordinateUtility.cartesian_to_index(x, y)
        x_range = x - self.x
        y_range = y - self.y
        destination = board[end_r][end_c]
        move_range = start_r - end_r

        if destination != None and board[start_r][start_c].color == destination.color:
            print('cannot move to the spot 26')
            return

        if x == self.x and y == self.y:
            print('cannot move to the spot 27')
            return
        
        if self.x == x:
            if move_range > 0:
                spots = [board[start_r - i][start_c] for i in range(1, move_range)]
            else:
                move_range = abs(move_range)
                spots = [board[start_r + i][start_c] for i in range(1, move_range)]
                
        elif self.y == y:
            move_range = start_c - end_c
            if move_range > 0:
                spots = [board[start_r][start_c - i] for i in range(1, move_range)]
            else:
                move_range = abs(move_range)
                spots = [board[start_r][start_c + i] for i in range(1, move_range)]
        
        elif abs(x_range) != abs(y_range):
            print('cannot move to the spot 28')
            return
        
        #set spots for path and check if path is empthy to move 
        # bala rast
        if 0 < x_range and 0 < y_range:
            spots = [board[start_r - i][start_c + i] for i in range(1, move_range)]
        # bala chap
        elif x_range < 0 < y_range:
            spots = [board[start_r - i][start_c - i] for i in range(1, move_range)]
        # pain rast
        elif y_range < 0 < x_range:
            spots = [board[start_r + i][start_c + i] for i in range(1, move_range)]
        # pain chap
        elif x_range < 0 and y_range < 0:
            spots = [board[start_r + i][start_c - i] for i in range(1, move_range)]

        is_path_empty = not any(spots)


        if not is_path_empty:
            print('cannot move to the spot 29')
            return

        if destination == None:
            self.replace_piece(board, x, y)
            print('moved')
            return True

        elif destination != None and board[start_r][start_c].color == destination.color:
            print('cannot move to the spot 30')
            return
        elif destination != None and board[start_r][start_c].color != destination.color:
            self.replace_piece(board, x, y)
            print('rival piece destroyed')
            return True


class King(Piece):
    def __init__(self, color, x, y):
        super().__init__("K", color, x, y)


    def replace_piece(self, board, x, y):
        start_r, start_c = CoordinateUtility.cartesian_to_index(self.x, self.y)
        end_r, end_c = CoordinateUtility.cartesian_to_index(x, y)
        board[end_r][end_c] = board[start_r][start_c]
        board[start_r][start_c] = None
        x, y = CoordinateUtility.index_to_cartesian(end_r, end_c)
        self.x = x
        self.y = y


    def move(self, x, y, board):
        start_r, start_c = CoordinateUtility.cartesian_to_index(self.x, self.y)
        end_r, end_c = CoordinateUtility.cartesian_to_index(x, y)
        destination = board[end_r][end_c]

        if x == self.x and y == self.y:
            print('cannot move to the spot 31')
            return

        if 1 < abs(x-self.x) or 1 < abs(y-self.y):
            print('cannot move to the spot 32')
            return

        if destination != None and board[start_r][start_c].color == destination.color:
            print('cannot move to the spot 33')

        if destination == None:
            self.replace_piece(board, x, y)
            print('moved')
            return True

        if destination != None and board[start_r][start_c].color != destination.color:
            self.replace_piece(board, x, y)
            print('rival piece destroyed')
            return True



class Knight(Piece):

    def __init__(self, color, x, y):
        super().__init__("N", color, x, y)

    def replace_piece(self, board, x, y):
        start_r, start_c = CoordinateUtility.cartesian_to_index(self.x, self.y)
        end_r, end_c = CoordinateUtility.cartesian_to_index(x, y)
        board[end_r][end_c] = board[start_r][start_c]
        board[start_r][start_c] = None
        x, y = CoordinateUtility.index_to_cartesian(end_r, end_c)
        self.x = x
        self.y = y

    def move(self, x, y, board):
        start_r, start_c = CoordinateUtility.cartesian_to_index(self.x, self.y)
        end_r, end_c = CoordinateUtility.cartesian_to_index(x, y)
        destination = board[end_r][end_c]

        legal_spots = [(1, 2), (1, -2), (-1, 2), (-1, -2)]

        if (x - self.x, y - self.y) not in legal_spots:
            print('cannot move to the spot 34')
            return
            
        if destination != None and board[start_r][start_c].color == destination.color:
            print('cannot move to the spot 35')
            return

        if destination == None:
            self.replace_piece(board, x, y)
            print('moved')
            return True

        if destination != None and board[start_r][start_c].color != destination.color:
            self.replace_piece(board, x, y)
            print('rival piece destroyed')



class User:

    username: str = ""
    password: str = ""
    undo_limit = 2
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
        undo_limit = 2


    def __eq__(self, other: object) -> bool:
        if isinstance(other, User):
            return self.username == other.username and self.password == other.password
        elif isinstance(other, str):
            return self.username == other
        # elif isinstance(other, )
        

    def print_board(self):
        print(*["|".join([str(cell) if cell is not None else "  " for cell in row]) for row in self.board], sep="|\n",
              end="|\n")

    @staticmethod
    def list_users():
        sorted_users = sorted(User.users, key=lambda x:x.username.lower())
        for user in sorted_users:
            print(f"{user.username}")
            

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
            return False
        
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
    cnt = 1
    white_user: User = None
    black_user: User = None
    white_turn: bool = True
    black_turn: bool = False
    did_undo: bool = False
    moved = False
    selected_piece: object = None
    limit: int = None
    board: list = []

    all_moves = []

    last_destroyed_piece = None
    last_piece_coordination = []
    moved_piece_coordination = []



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
        self.selected_piece = None
        self.moved = False
        self.did_undo = False
        self.all_moves = []
        self.last_destroyed_piece = None
        self.last_piece_coordination = []
        self.moved_piece_coordination = []

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
        for command in commands.strip().split("\n"):
            print(command.strip())


    @staticmethod
    def get_command_list(chess):
        if chess.white_user == None:
            Chess.print_commands(Chess.first_layer_menue)
        elif chess.white_user != None and chess.black_user == None:
            Chess.print_commands(Chess.second_layer_menue)
        elif chess.white_user != None and chess.black_user != None:
            Chess.print_commands(Chess.game_menue)


    def print_board(self):
        # board = [ 
        #     '|'.join([   "  " if piece is  None else  str(piece) if piece is not self.selected_piece else "\033[0;31m" + str(piece) + "\033[0m" for piece in row ])
        #     for row in self.board
        # ]
        board = [ 
            '|'.join([   "  " if piece is  None else  str(piece) if piece is not self.selected_piece else str(piece) for piece in row ])
            for row in self.board
        ]
        print(*board, sep="|\n", end="|\n")

        
    # def check_game_limit(self, limit: int):
    #     if limit < 0:
    #         print("number should be positive to have a limit or 0 for no limit")
    #         return False


    def start_new_game(self, username, limit):
        self.cnt += 1
        if User.check_validations(username) == False:
            return

        if int(limit) < 0:
            print("number should be positive to have a limit or 0 for no limit")
            return False

        if username == self.white_user.username:
            message = "you must choose another player to start a game"
            print(message)
            return False

        if User.is_username_exist(username):
            self.black_user = User.users[User.users.index(username)]
            self.limit = limit
            message = f"new game started successfully between {self.white_user.username} and {self.black_user.username} with limit {self.limit}"
            print(message)
            return

        else:
            message = "no user exists with this username"
            print(message)


    def print_scoreboard(self, chess):
        active_user = chess.white_user if chess.white_turn else chess.black_user
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
    def select_piece(chess: object, x: int, y: int):

        piece = None
        x, y = CoordinateUtility.cartesian_to_index(x, y)
        x, y = int(x), int(y)

        if (0 <= x <= 7 and 0 <= y <= 7):
            piece = chess.board[x][y]
        else:
            print("wrong coordination")
            return

        if chess.is_cordination_none(piece):
            print("no piece on this spot")

        elif chess.is_piece_selectable(chess, piece):
            chess.selected_piece = piece
            chess.last_piece_coordination = [y, x]
            print("selected")

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


prev_position = ()
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
        
        elif user_inp[0] == "scoreboard":
            chess.print_scoreboard(chess=chess)
        
        elif user_inp[0] == "logout":
            User.logout(chess)

        # game menu
        elif user_inp[0] == "select":
            x, y = user_inp[1].split(",")
            chess.select_piece(chess, y=int(x), x=int(y))
        

        elif user_inp[0] == "move":
            if chess.moved:
                print("already moved")
            else:
                moves = user_inp[1].split(",")
                x = int(moves[0])
                y = int(moves[1])
                if not (1 <= x <= 8 and 1 <= y <= 8):
                    print("wrong coordination")
                elif chess.selected_piece is None:
                    print("do not have any selected piece")
                else:
                    x, y = user_inp[1].split(",")
                    x, y = int(x), int(y)
                    
                    #TODO: x, y?? (maybe have to use Coordi....)
                    xx, yy = CoordinateUtility.cartesian_to_index(y,x)
                    chess.last_destroyed_piece = chess.board[xx][yy]
                    move = chess.selected_piece.move(y=int(x), x=int(y), board=chess.board)
                    chess.moved = True

                    if move:
                        last_x, last_y = CoordinateUtility.index_to_cartesian(chess.last_piece_coordination[0],chess.last_piece_coordination[1])
                        moved_x, moved_y = CoordinateUtility.index_to_cartesian(8 - y, x - 1)
                        chess.all_moves.append([chess.selected_piece, (last_y, last_x), (moved_y, moved_x), chess.last_destroyed_piece])
                        
                        chess.moved_piece_coordination = [xx, yy]

            chess.print_board()


        elif user_inp[0] == "deselect":
            if len(user_inp) == 1:
                chess.deselect()
            else:
                print("invalid command")




        elif user_inp[0] == "forfeit":
            if len(user_inp) == 1:
                User.forfeit(chess)
            else:
                print("invalid command")


        elif user_inp[0] == "show_board":
            if len(user_inp) == 1:
                chess.print_board()
            else:
                print("invalid command")
                

        elif user_inp[0] == "next_turn": 
            if len(user_inp) == 1:
                if not chess.moved:
                    print("you must move then proceed to next turn")
                else:
                    chess.white_turn = not chess.white_turn
                    chess.moved = False
                    chess.did_undo = False
                    print("turn completed")
            else:
                print("invalid command")


        elif user_inp[0] == "show_turn":
            if len(user_inp) == 1:
                active_user = chess.white_user if chess.white_turn else chess.black_user
                active_user_color = "white" if chess.white_turn else "black" 
                message = f"it is player {active_user.username} turn with color {active_user_color}" 
                print(message)
                pass
            else:
                print("invalid command")


        elif user_inp[0] == "undo":
            if len(user_inp) == 1:
                active_user = chess.white_user if chess.white_turn else chess.black_user
                if active_user.undo_limit == 0:
                    print("you cannot undo anymore")
                else:
                    if not chess.moved:
                        print("you must move before undo")
                    else:
                        if chess.did_undo:
                            print("you have used your undo for this turn")
                        else:
                            chess.did_undo = True
                            active_user.undo_limit -= 1

                            last_row, last_col = chess.last_piece_coordination[1], chess.last_piece_coordination[0]
                            
                            moved_row, moved_col = chess.moved_piece_coordination[0], chess.moved_piece_coordination[1]
                            

                            piece = chess.board[moved_row][moved_col]
      
                            x, y = CoordinateUtility.index_to_cartesian(last_row, last_col)
                            print("last_row, last_col ",last_row, last_col)
                            print("moved_row, moved_col ", moved_row, moved_col )
                            print("X, Y: ", piece.x, piece.y)
                            piece.x = last_row
                            piece.y = last_col

                            print("PIECE : ", piece)
                            print("LAST DESTROYED: ", chess.last_destroyed_piece)
                            chess.board[last_row][last_col] = piece
                            chess.board[moved_row][moved_col] = chess.last_destroyed_piece

                            piece.x = x
                            piece.y = y
                            print(piece.x, piece.y)
                            chess.moved = False
                            chess.all_moves.pop()

                            print("undo completed")
            else:
                print("invalid command")

            chess.print_board()
        
        elif user_inp[0] == "undo_number":
            if len(user_inp) == 1:
                active_user = chess.white_user if chess.white_turn else chess.black_user
                message = f"you have {active_user.undo_limit} undo moves"
                print(message)
        
        elif user_inp[0] == "show_moves":
            if len(user_inp) == 1:
                active_user = chess.white_user if chess.white_turn else chess.black_user
                active_user_color = "w" if chess.white_turn else "b" 
                for item in chess.all_moves:
                    if item[0].color == active_user_color:
                        if item[3] == None:
                            print(f"{item[0]} {str(item[1])[1:-1]} to {str(item[2])[1:-1]}")
                        else:
                            print(f"{item[0]} {str(item[1])[1:-1]} to {str(item[2])[1:-1]} destroyed {item[3]}")
