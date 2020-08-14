class Chess:
    # List of strings. Position = 63 - 8rank + file (Range: 0 - 63)
    board = ['black_rook', 'black_knight', 'black_bishop', 'black_queen', 'black_king', 'black_bishop', 'black_knight', 'black_rook',
             'black_pawn', 'black_pawn', 'black_pawn', 'black_pawn', 'black_pawn', 'black_pawn', 'black_pawn', 'black_pawn',
             'none', 'none', 'none', 'none', 'none', 'none', 'none', 'none',
             'none', 'none', 'none', 'none', 'none', 'none', 'none', 'none',
             'none', 'none', 'none', 'none', 'none', 'none', 'none', 'none',
             'none', 'none', 'none', 'none', 'none', 'none', 'none', 'none',
             'white_pawn', 'white_pawn', 'white_pawn', 'white_pawn', 'white_pawn', 'white_pawn', 'white_pawn', 'white_pawn',
             'white_rook', 'white_knight', 'white_bishop', 'white_queen', 'white_king', 'white_bishop', 'white_knight', 'white_rook']
    #         A             B               C               D              E             F               G               H
    color_board = ['light', 'dark', 'light', 'dark', 'light', 'dark', 'light', 'dark',
                   'dark', 'light', 'dark', 'light', 'dark', 'light', 'dark', 'light',
                   'light', 'dark', 'light', 'dark', 'light', 'dark', 'light', 'dark',
                   'dark', 'light', 'dark', 'light', 'dark', 'light', 'dark', 'light',
                   'light', 'dark', 'light', 'dark', 'light', 'dark', 'light', 'dark',
                   'dark', 'light', 'dark', 'light', 'dark', 'light', 'dark', 'light',
                   'light', 'dark', 'light', 'dark', 'light', 'dark', 'light', 'dark',
                   'dark', 'light', 'dark', 'light', 'dark', 'light', 'dark', 'light']

    rank_list = ["<:1_:721418419924238348>", "<:2_:721418430145888277>", "<:3_:721418439700381757>", "<:4_:721418451222265897>",
                 "<:5_:721418462433378404>", "<:6_:721418473141567558>", "<:7_:721418482817826836>", "<:8_:721418492129181697>"]

    white_files = "<:A_:721418501150998599><:B_:721418513314611221><:C_:721418523297054720><:D_:721418533841666159>"\
        + "<:E_:721418542939111475><:F_:721418552694800435><:G_:721418564514611321><:H_:721418575709077565>"

    black_files = "<:H_:721418575709077565><:G_:721418564514611321><:F_:721418552694800435><:E_:721418542939111475>"\
        + "<:D_:721418533841666159><:C_:721418523297054720><:B_:721418513314611221><:A_:721418501150998599>"

    white_id = ''
    black_id = ''
    in_game = False
    white_turn = bool

    # move validation
    starts = list
    available_moves = list
    valid_move = bool
    white_king_pos = list
    black_king_pos = list
    white_in_check = bool
    black_in_check = bool

    def move(self, start, end, valid_move):
        if valid_move and (self.board[end] != self.board[start]):
            self.board[end] = self.board[start]
            self.board[start] = 'none'
            return True
        else:
            return False

    def filerank_to_integer(self, filerank):  # takes filerank string position and converts to integer position

        files = {
                "a": 1,
                "b": 2,
                "c": 3,
                "d": 4,
                "e": 5,
                "f": 6,
                "g": 7,
                "h": 8
                }

        file = files.get(filerank[0])

        return 63 - (8 * int(filerank[1])) + file

    def format_board(self):

        formatted_board = ''

        if self.white_turn:
            for i in range(64):
                if self.color_board[i].startswith('light'):
                    if self.board[i].startswith('white'):
                        if self.board[i].endswith('pawn'):
                            formatted_board += '<:light_white_pawn:721180422008209419>'
                        if self.board[i].endswith('bishop'):
                            formatted_board += '<:light_white_bishop:721180380065169428>'
                        if self.board[i].endswith('knight'):
                            formatted_board += '<:light_white_knight:721180412046606367>'
                        if self.board[i].endswith('rook'):
                            formatted_board += '<:light_white_rook:721180441662455920>'
                        if self.board[i].endswith('queen'):
                            formatted_board += '<:light_white_queen:721180430459600906>'
                        if self.board[i].endswith('king'):
                            formatted_board += '<:light_white_king:721180402634719254>'
                    elif self.board[i].startswith('black'):
                        if self.board[i].endswith('pawn'):
                            formatted_board += '<:light_black_pawn:721180350566367316>'
                        if self.board[i].endswith('bishop'):
                            formatted_board += '<:light_black_bishop:721180325035769860>'
                        if self.board[i].endswith('knight'):
                            formatted_board += '<:light_black_knight:721180342228353094>'
                        if self.board[i].endswith('rook'):
                            formatted_board += '<:light_black_rook:721180370183258184>'
                        if self.board[i].endswith('queen'):
                            formatted_board += '<:light_black_queen:721180360502935554>'
                        if self.board[i].endswith('king'):
                            formatted_board += '<:light_black_king:721180333885882428>'
                    else:
                        formatted_board += '<:light:721180146001772584>'
                else:
                    if self.board[i].startswith('white'):
                        if self.board[i].endswith('pawn'):
                            formatted_board += '<:dark_white_pawn:721180252776169572>'
                        if self.board[i].endswith('bishop'):
                            formatted_board += '<:dark_white_bishop:721180223630213139>'
                        if self.board[i].endswith('knight'):
                            formatted_board += '<:dark_white_knight:721180243058229290>'
                        if self.board[i].endswith('rook'):
                            formatted_board += '<:dark_white_rook:721180272770678814>'
                        if self.board[i].endswith('queen'):
                            formatted_board += '<:dark_white_queen:721180263274774578>'
                        if self.board[i].endswith('king'):
                            formatted_board += '<:dark_white_king:721180233729966112>'
                    elif self.board[i].startswith('black'):
                        if self.board[i].endswith('pawn'):
                            formatted_board += '<:dark_black_pawn:721180195087712317>'
                        if self.board[i].endswith('bishop'):
                            formatted_board += '<:dark_black_bishop:721180161067974736>'
                        if self.board[i].endswith('knight'):
                            formatted_board += '<:dark_black_knight:721180177953980427>'
                        if self.board[i].endswith('rook'):
                            formatted_board += '<:dark_black_rook:721180214918381618>'
                        if self.board[i].endswith('queen'):
                            formatted_board += '<:dark_black_queen:721180206626242680>'
                        if self.board[i].endswith('king'):
                            formatted_board += '<:dark_black_king:721180169913499689>'
                    else:
                        formatted_board += '<:dark:721180135247577130>'
                if not ((i + 1) % 8):
                    formatted_board += "\n"
        else:
            for i in range(64):
                if self.color_board[i].startswith('light'):
                    if self.board[63 - i].startswith('white'):
                        if self.board[63 - i].endswith('pawn'):
                            formatted_board += '<:light_white_pawn:721180422008209419>'
                        if self.board[63 - i].endswith('bishop'):
                            formatted_board += '<:light_white_bishop:721180380065169428>'
                        if self.board[63 - i].endswith('knight'):
                            formatted_board += '<:light_white_knight:721180412046606367>'
                        if self.board[63 - i].endswith('rook'):
                            formatted_board += '<:light_white_rook:721180441662455920>'
                        if self.board[63 - i].endswith('queen'):
                            formatted_board += '<:light_white_queen:721180430459600906>'
                        if self.board[63 - i].endswith('king'):
                            formatted_board += '<:light_white_king:721180402634719254>'
                    elif self.board[63 - i].startswith('black'):
                        if self.board[63 - i].endswith('pawn'):
                            formatted_board += '<:light_black_pawn:721180350566367316>'
                        if self.board[63 - i].endswith('bishop'):
                            formatted_board += '<:light_black_bishop:721180325035769860>'
                        if self.board[63 - i].endswith('knight'):
                            formatted_board += '<:light_black_knight:721180342228353094>'
                        if self.board[63 - i].endswith('rook'):
                            formatted_board += '<:light_black_rook:721180370183258184>'
                        if self.board[63 - i].endswith('queen'):
                            formatted_board += '<:light_black_queen:721180360502935554>'
                        if self.board[63 - i].endswith('king'):
                            formatted_board += '<:light_black_king:721180333885882428>'
                    else:
                        formatted_board += '<:light:721180146001772584>'
                else:
                    if self.board[63 - i].startswith('white'):
                        if self.board[63 - i].endswith('pawn'):
                            formatted_board += '<:dark_white_pawn:721180252776169572>'
                        if self.board[63 - i].endswith('bishop'):
                            formatted_board += '<:dark_white_bishop:721180223630213139>'
                        if self.board[63 - i].endswith('knight'):
                            formatted_board += '<:dark_white_knight:721180243058229290>'
                        if self.board[63 - i].endswith('rook'):
                            formatted_board += '<:dark_white_rook:721180272770678814>'
                        if self.board[63 - i].endswith('queen'):
                            formatted_board += '<:dark_white_queen:721180263274774578>'
                        if self.board[63 - i].endswith('king'):
                            formatted_board += '<:dark_white_king:721180233729966112>'
                    elif self.board[63 - i].startswith('black'):
                        if self.board[63 - i].endswith('pawn'):
                            formatted_board += '<:dark_black_pawn:721180195087712317>'
                        if self.board[63 - i].endswith('bishop'):
                            formatted_board += '<:dark_black_bishop:721180161067974736>'
                        if self.board[63 - i].endswith('knight'):
                            formatted_board += '<:dark_black_knight:721180177953980427>'
                        if self.board[63 - i].endswith('rook'):
                            formatted_board += '<:dark_black_rook:721180214918381618>'
                        if self.board[63 - i].endswith('queen'):
                            formatted_board += '<:dark_black_queen:721180206626242680>'
                        if self.board[63 - i].endswith('king'):
                            formatted_board += '<:dark_black_king:721180169913499689>'
                    else:
                        formatted_board += '<:dark:721180135247577130>'
                if not ((i + 1) % 8):
                    formatted_board += "\n"

        return formatted_board

    def list_starts(self, white_turn, board):  # list all piece positions that player can start at (same color)
        starts = []
        if white_turn:
            for i in range(64):
                if board[i].startswith('white'):
                    starts.append(i)
        else:
            for i in range(64):
                if board[i].startswith('black'):
                    starts.append(i)
        return starts

    def list_moves(self, starts, white_turn, board):  # list all available moves for piece by movement ability.
        moves = []
        for i in starts:
            if board[i].endswith('pawn'):
                if white_turn:
                    moves.append([i, i - 8])
                    if not (i % 8):
                        moves.append([i, i - 7])
                    elif not ((i + 1) % 8):
                        moves.append([i, i - 9])
                    else:
                        moves.append([i, i - 9])
                        moves.append([i, i - 7])
                else:
                    moves.append([i, i + 8])
                    if not (i % 8):
                        moves.append([i, i + 9])
                    elif not ((i + 1) % 8):
                        moves.append([i, i + 7])
                    else:
                        moves.append([i, i + 9])
                        moves.append([i, i + 7])
            if board[i].endswith('bishop'):
                up_left = i
                while (up_left > 7) and (up_left % 8 != 0):
                    up_left -= 9
                    moves.append([i, up_left])
                up_right = i
                while (up_right > 7) and ((up_right + 1) % 8 != 0):
                    up_right -= 7
                    moves.append([i, up_right])
                down_left = i
                while (down_left < 56) and (down_left % 8 != 0):
                    down_left += 7
                    moves.append([i, down_left])
                down_right = i
                while (down_right < 56) and ((down_right + 1) % 8 != 0):
                    down_right += 9
                    moves.append([i, down_right])
            if board[i].endswith('knight'):
                if i > 15:
                    if not (i % 8):
                        moves.append([i, i - 15])  # up_right
                    elif not ((i + 1) % 8):
                        moves.append([i, i - 17])  # up_left
                    else:
                        moves.append([i, i - 15])
                        moves.append([i, i - 17])
                if i < 48:
                    if not (i % 8):
                        moves.append([i, i + 17])  # down_right
                    elif not ((i + 1) % 8):
                        moves.append([i, i + 15])  # down_left
                    else:
                        moves.append([i, i + 17])
                        moves.append([i, i + 15])
                if (i % 8) and ((i - 1) % 8):
                    if i < 8:
                        moves.append([i, i + 6])  # left_down
                    elif i > 55:
                        moves.append([i, i - 10])  # left_up
                    else:
                        moves.append([i, i + 6])
                        moves.append([i, i - 10])
                if ((i + 1) % 8) and ((i + 2) % 8):
                    if i < 8:
                        moves.append([i, i + 10])  # right_down
                    elif i > 55:
                        moves.append([i, i - 6])  # right_up
                    else:
                        moves.append([i, i + 10])
                        moves.append([i, i - 6])
            if board[i].endswith('rook'):
                edge = i
                while edge > 7:
                    edge -= 8
                for r in range(8):
                    moves.append([i, edge + (8 * r)])
                edge = i
                while edge % 8 != 0:
                    edge -= 1
                for c in range(8):
                    moves.append([i, edge + c])
            if board[i].endswith('king'):
                if i < 8:
                    if not (i % 8):
                        moves.append([i, 1])
                        moves.append([i, 8])
                        moves.append([i, 9])
                    elif not ((i + 1) % 8):
                        moves.append([i, 6])
                        moves.append([i, 14])
                        moves.append([i, 15])
                    else:
                        moves.append(i, i - 1)
                        moves.append(i, i + 1)
                        moves.append(i, i + 7)
                        moves.append(i, i + 8)
                        moves.append(i, i + 9)
                if i > 55:
                    if not (i % 8):
                        moves.append([i, 48])
                        moves.append([i, 49])
                        moves.append([i, 57])
                    elif not ((i + 1) % 8):
                        moves.append([i, 54])
                        moves.append([i, 55])
                        moves.append([i, 62])
                    else:
                        moves.append(i, i - 1)
                        moves.append(i, i + 1)
                        moves.append(i, i - 7)
                        moves.append(i, i - 8)
                        moves.append(i, i - 9)
                else:
                    if not (i % 8):
                        moves.append(i, i - 8)
                        moves.append(i, i - 7)
                        moves.append(i, i + 1)
                        moves.append(i, i + 8)
                        moves.append(i, i + 9)
                    elif not ((i + 1) % 8):
                        moves.append(i, i - 9)
                        moves.append(i, i - 8)
                        moves.append(i, i - 1)
                        moves.append(i, i + 7)
                        moves.append(i, i + 8)
                    else:
                        moves.append(i, i - 9)
                        moves.append(i, i - 8)
                        moves.append(i, i - 7)
                        moves.append(i, i - 1)
                        moves.append(i, i + 1)
                        moves.append(i, i + 7)
                        moves.append(i, i + 8)
                        moves.append(i, i + 9)
            if board[i].endswith('queen'): # I'm 99% sure there is literally nothing stopping me from just copy-pasting rook and bishop code.
                edge = i
                while edge > 7:
                    edge -= 8
                for r in range(8):
                    moves.append([i, edge + (8 * r)])
                edge = i
                while edge % 8 != 0:
                    edge -= 1
                for c in range(8):
                    moves.append([i, edge + c])
                up_left = i
                while (up_left > 7) and (up_left % 8 != 0):
                    up_left -= 9
                    moves.append([i, up_left])
                up_right = i
                while (up_right > 7) and ((up_right + 1) % 8 != 0):
                    up_right -= 7
                    moves.append([i, up_right])
                down_left = i
                while (down_left < 56) and (down_left % 8 != 0):
                    down_left += 7
                    moves.append([i, down_left])
                down_right = i
                while (down_right < 56) and ((down_right + 1) % 8 != 0):
                    down_right += 9
                    moves.append([i, down_right])
        for i in moves:  # removes "moves" to same position
            if i[0] == i[1]:
                moves.remove(i)
        return moves

    # def list_spaces_before_obstacle: remove spaces after obstacle in way

    # def list_protect_king(self): (in case of check) list all

    def check_king_in_check(self, king_pos, available_moves): #check whether king is in check by comparing position of king to all possible positions of pieces
        for i in available_moves:
            return True if king_pos == available_moves[i] else False

    # def check_final_space: if same color, cant move. if different or no color, can move.

    # def check_move_valid(self):


    # miscellaneous

    def print_board(self):
        for i in range(64):
            print(self.board[i], end=" ")
            if not (i + 1) % 8:
                print('\n')

    def empty_board(self):
        for i in range(64):
            self.board[i] = 'none'


