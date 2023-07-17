class Board:
    def __init__(self):
        self.user1='user1'
        self.user2='user2'
        self.positions = {'상1': (self.user1, 11), '왕1': (self.user1, 21), '장1': (self.user1, 31), '자1': (self.user1, 22),
                          '상2':(self.user2, 34), '왕2': (self.user2, 24), '장2': (self.user2, 14), '자2': (self.user2, 23)}
        # key: piece name
        # value: (user_name, xy)

    def __repr__(self) -> str:
        """
        장2|왕2|상2
           |자2|   
           |자1|
        상1|왕1|장1    
        """
        


        return str(self.positions) # TODO 보드 그림 만들기
    
    # def get_piece_by_position(self, position):
    #     for value in self.positions.values():
    #         if position == value:
    #             position=0
    #     return


if __name__ == '__main__':
    board = Board()
    print(board)
