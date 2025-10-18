from games import *

class GameOfNim(Game):
    """Play Game of Nim with first player 'MAX'.
    A state has the player to move, a cached utility, a list of moves in
    the form of a list of (x, y) positions, and a board, in the form of
    a list with number of objects in each row."""

    def __init__(self, board=[3,1]):  
        self.board = board
        moves = []
        for row, count in enumerate(board):
            for match in range(1, count+1):
                moves.append((row, match))
        self.initial = GameState(to_move='MAX', utility=0, board=board, moves=moves)

    def actions(self, state):
        """Legal moves are at least one object, all from the same row."""
        return state.moves

    def result(self, state, move):
        if move not in state.moves:
            return state
        row, match=move; board=list(state.board); board[row] = board[row] - match
        if state.to_move == 'MAX': next_player = 'MIN'
        else: next_player = 'MAX'
        moves = [(r, n) for r, count in enumerate(board) for n in range(1, count + 1)]

        new_state = GameState(next_player, 0, board, moves)
        if self.terminal_test(new_state):
            utility = self.utility(new_state, state.to_move)
        else:
            utility = 0

        return GameState(to_move=next_player, utility=utility, board=board, moves=moves)

         

    def utility(self, state, player):
        """Return the value to player; 1 for win, -1 for loss, 0 otherwise."""
        if self.terminal_test(state):
            if state.to_move == player:
                return -1
            else : return 1
        return 0

    def terminal_test(self, state):
        """A state is terminal if there are no objects left"""
        return max(state.board) == 0
        

    def display(self, state):
        board = state.board
        print("board: ", board)


if __name__ == "__main__":
    nim = GameOfNim(board=[0, 5, 3, 1]) # Creating the game instance
    #nim = GameOfNim(board=[7, 5, 3, 1]) # a much larger tree to search
    print(nim.initial.board) # must be [0, 5, 3, 1]
    print(nim.initial.moves) # must be [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 2), (2, 3), (3, 1)]
    print(nim.result(nim.initial, (1,3) ))
    utility = nim.play_game(alpha_beta_player, query_player) # computer moves first 
    if (utility < 0):
        print("MIN won the game")
    else:
        print("MAX won the game")
