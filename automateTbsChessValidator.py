# Builds chessboard
def chessboard():
    board = piecesToBoard()
    print(board)

# Sets chessboard coordinates
def columnRows():
    columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    rows = ['8','7','6','5','4','3','2','1']
    coords = {}
    for x in columns:
        for y in rows:
            z = x+y
            coords.setdefault(z)
    return coords

# Puts pieces of board
def piecesToBoard():
    white_pieces = ['rook', 'knight', 'bishop', 'queen', 'king' ,'bishop', 'knight', 'rook' ]
    black_pieces = ['rook', 'knight', 'bishop', 'queen', 'king' ,'bishop', 'knight', 'rook' ]
    pawns = ['pawn','pawn','pawn','pawn','pawn','pawn','pawn','pawn']
    coords = columnRows()
    count = 0 # Black pieces
    count2 = 0 # Black pawns
    count3 = 0 # White pawns
    count4 = 0 # White pieces
    for x in coords:
        if '8' in x:  # Add black pieces    
            y = 'b' + black_pieces[count]
            coords[x] = y
            count += 1
        elif '7' in x: # Add black pawn
            y = 'b' + pawns[count2]
            coords[x] = y
            count2 += 1        
        elif '2' in x: # Add white pieces
            y = 'w' + pawns[count3]
            coords[x] = y
            count3 += 1
        elif '1' in x:  # Add white pawns
            y = 'w' + white_pieces[count4]
            coords[x] = y
            count4 += 1

    return coords

chessboard()