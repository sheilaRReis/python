import time
from player import HumanPlayer, RandomComputerPlayer

class TicTacToe :
    def __init__(self) :
        self.board = [" " for _ in range(9)]
        self.current_winner = None

    def print_board(self) :
        for row in [self.board[i*3:(i+1)*3] for i in range(3)] :
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_numbers() :
        number_board = [[str(i) for i in range(j*3, (j+1)* 3)] for j in range(3)]
        for row in number_board :
            print('| '+ ' | '.join(row) + ' |')

    def available_moves(self) :
        
        # enumerate retorna lista indexada 
        #   ['x', 'x', 'o'] => [(0, 'x'), (1, 'x'), (2, 'x')]
        return [i for i, spot in enumerate(self.board) if spot == ' ']
        #código + curto, funciona igual ao código abaixo
        # moves = []
        # for (i, spot) in enumerate(self.board) :
        #     if spot == " " :
        #         moves.append(i)
        # return moves

    def empty_spaces(self) :
        return ' ' in self.board

    def count_empty_spaces(self):
        # Como  return self.board.count(' ')
        return self.board.count(' ')

    def make_move(self, square, letter) :
        if(self.board[square] == ' '):
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False
    def winner(self, square, letter):
        row_index = square // 3
        row = self.board[row_index*3 : (row_index + 1) * 3]
        if all([spot == letter for spot in row]):
            return True
        
        column_index = square % 3
        column = self.board[column_index*3 : (column_index + 1) * 3]
        if all([spot==letter for spot in column]):
            return True
        if square % 2 == 0 :
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True
        return False
def play(game, x_player, o_player, print_game = True) :
    if print_game:
        game.print_board_numbers()

    letter = "X"

    while game.empty_spaces() and not game.current_winner:
        if letter == 'O' :
            square = o_player.get_move(game)
        else :
            square = x_player.get_move(game)

        if game.make_move(square, letter) :
            if print_game :
                print(letter + f" marcou a posição {square}")
                game.print_board()
                print('')
                
            if game.current_winner :
                if print_game :
                    print (letter + ' venceu!')
                    
            
            letter = 'O' if letter=='X' else 'X'
       
        time.sleep(0.8)

    if print_game and not game.current_winner :
        print('Empate!  ')

if __name__ == '__main__' :
    x_player = HumanPlayer('X')
    o_player = RandomComputerPlayer('O')
    game = TicTacToe()
    play(game, x_player, o_player, print_game=True)