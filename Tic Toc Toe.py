class logic_of_tictocoe:
    def __init__(self) -> None:
        pass

    def valid_input(self, ply_ch, game_board):
        try:
            ply_ch = int(ply_ch)
            if ply_ch in range(1, 10) and ply_ch in game_board:
                return True
            return False
        except:
            return False

    def is_winner(self, player : tuple, game_map : list) -> bool:
        game_map_possible_winners = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
        for tup in game_map_possible_winners:
            win = True
            for element in tup:
                if game_map[element] != player[1]:
                    win = False
                    break
            if win:
                break
        return win

    def make_game_first_move(self, game_board):
        flage = True
        players = {}
        for i in range(1, 3):
            sign = 'X' if i == 1 else 'O'
            players[f'P{i}'] = (self.get_name(), sign) # TODO : make a dictionary.
        self.show_board(game_board)
        while (game_board.count(['X']) + game_board.count(['O'])) <= 9:
            player , flage = self.give_turn(players, flage)
            if (game_board.count(['X']) + game_board.count(['O'])) == 6 : # TODO : make a func
                return game_board
            inp = input(f'Hello {player[0]} give me your choice, you will be {player[1]}: ') # MAKE A FUNC FOR WRONG INP
            if self.valid_input(inp, game_board):
                inp = int(inp)
                if self.logic(inp, flage, game_board, player):
                    break
            else:
                print('Invalid input!, next player gonna choice... .')
                continue
        return game_board

    def make_move(self, board : list, player_inp : int, ply : tuple) :
        board[player_inp -1] = ply[1]
        if self.is_winner(ply, board):
            return (True, ply[0])
        else:
            return (False, ply[0])

        
    def get_name(self) -> str :
        while True:
            inp = input('Enter your name: ')
            if inp != '' or isinstance(inp, str):
                return inp
            else:
                print('wrong input!, try again...')

    def give_turn(self, plys, flage = True):
            if flage:
                flage = not flage
                return (plys['P1'], flage)
            else:
                flage = not flage
                return (plys['P2'], flage)

    def logic(self, player_choice, flag, game_board, player)-> tuple:
        win, player_name = self.make_move(game_board, player_choice, player)
        if win:
            print(f'{player_name} you won!')
            self.show_board(game_board)
            return True
        else:
            self.show_board(game_board)
        return False


    def show_board(self, board):
        print('<----GAME-MAP---->')
        for line in range(len(board)):
            flage = ' ' if (line + 1) % 3 != 0 else '\n\n'
            print(board[line], end= flage)
        print('<---------------->')

    def main(self):
        game_board = [i for i in range(1,10)]
        game_board = self.make_game_first_move(game_board)

example1 = logic_of_tictocoe()
example1.main()
