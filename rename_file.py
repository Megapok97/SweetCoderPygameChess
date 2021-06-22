import os

y = os.listdir("assets/images/fantasy/")
x = {
    'bB.png': 'b_bishop.png',
    'bK.png': 'b_king.png',
    'bN.png': 'b_knight.png',
    'bP.png': 'b_pawn.png',
    'bQ.png': 'b_queen.png',
    'bR.png': 'b_rook.png',
    'wB.png': 'w_bishop.png',
    'wK.png': 'w_king.png',
    'wN.png': 'w_knight.png',
    'wP.png': 'w_pawn.png',
    'wQ.png': 'w_queen.png',
    'wR.png': 'w_rook.png',
}

for file in y:
    if file in x:
        os.rename(f'assets/images/fantasy/{file}', f'assets/images/fantasy/{x[file]}')