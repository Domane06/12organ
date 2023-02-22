import user
from board import Board

def parse(command):
    """ Return (piece, position) """
    piece, position= command.split()
    piece=piece.replace(',','')
    position=position.replace('(','')
    position=position.replace(')','')
    position=position.replace(',','')
    position=int(position)
    return piece, position



user1=user.User('user1')
user1_turn=True
user2=user.User('user2')
board = Board()

gameover = False
while not gameover:
    if user1_turn:
        try:
            command = input("user1 turn: (q: quit) ")
            if command == 'q' or command=='ㅂ': break
            piece, position = parse(command)
            print(piece)
            print(position)
            
        except ValueError as e:
            print('다시 입력해주세요')
            print(e)
        
        print(board)
        user1.move_piece(piece, position, board)
        print(board)
        if board.positions['왕2']==0:
            print('user1 win!')
            gameover = True
        user1_turn=False

    else:
        try:
            command = input("user2 turn: (q: quit) ")
            if command == 'q' or command=='ㅂ': break
            piece, position = parse(command)
            print(piece)
            print(position)
            
        except ValueError as e:
            print('다시 입력해주세요')
            print(e)
        
        print(board)
        user2.move_piece(piece, position, board)
        print(board)
        if board.positions['왕1']==5:
            print('user2 win!')
            gameover = True
            
        user1_turn=True

