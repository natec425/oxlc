def new_board():
    return {
        (x, y): None
        for x in range(3)
        for y in range(3)
    }

def new_state():
    return {
    	'board': new_board(),
    	'player1_turn': True
    }

def place(state, x, y):
    next_board = board_place(state['board'], x, y, state['player1_turn'])
    if next_board is not None:
        return {
            'board': next_board,
            'player1_turn': not state['player1_turn']
        }

def board_place(board, x, y, marker):
    if board[(x, y)] is None:
        return {
        	(bx, by): marker if (x, y) == (bx, by) else board[(bx, by)]
        	for bx in range(3)
        	for by in range(3)
         }

def show(state):
    return f'''Turn: {int(not state['player1_turn'])}
{show_board(state['board'])}'''

def show_board(board):
    return '\n'.join(
        ' | '.join(show_cell(board[(x, y)]) for x in range(3))
        for y in range(3)
    )


def show_cell(cell):
    if cell is None:
        return '-'
    elif cell:
        return 'X'
    else:
        return 'O'

ROWS = [
    [(x, y) for x in range(3)]
    for y in range(3)
]

COLUMNS = [
    [(x, y) for y in range(3)]
    for x in range(3)
]

DIAGONALS = [
    [(0, 0), (1, 1), (2, 2)],
    [(0, 2), (1, 1), (2, 0)]
]

WINNING_POSITIONS = ROWS + COLUMNS + DIAGONALS

def winner(state):
    try:
        return next(
            positions
            for positions in WINNING_POSITIONS
            if {not state['player1_turn']} == set(state['board'][(x, y)] for x, y in positions)
        )
    except StopIteration:
        return None

def get_action(state):
    while True:
        s = input('x, y: ')
        try:
            x_s, y_s = s.split(', ')
            x, y = int(x_s), int(y_s)
            if x in range(3) and y in range(3):
                return x, y
        except ValueError:
            pass
        print('Please provide a valid x, y')

def main():
    state = new_state()
    while True:
        print(show(state))
        x, y = get_action(state)
        state = place(state, x, y)
        if winner(state):
            break
    print(f"{show_cell(not state['player1_turn'])} wins!")

if __name__ == '__main__':
    main()
