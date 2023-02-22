class User:
    def __init__(self, name) -> None:
        self.name = name

    def move_piece(self, piece, new_position, board) -> None:
        """ Update position dictionary """
        current_position=board.positions[piece]
        # TODO: 각 피스별로 움직일수 있는 경로 및 선택
        # 같은 팀이 있는 곳으로는 못감
        for k, v in board.positions.items():
            if v == new_position:
                if self.name=='user1':
                    board.positions[k]=0
                else:
                    board.positions[k]=5
                
            
    
        board.positions[piece]= new_position

    

    


        

    def select_grave(self, piece, position):
        #같은 피스가 두개 있을수 있음 주의
        pass