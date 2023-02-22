class Board:
    def __init__(self):
        self.positions = {'상1': 11, '왕1': 12, '장1': 13, '자1': 22,
                          '상2': 34, '왕2': 24, '장2': 14, '자2': 23}
        # key: piece name
        # value: xy
        # TODO: brave= 0 or 5

    def __repr__(self) -> str:
        return str(self.positions) # TODO 보드 그림 만들기
    
    # def get_piece_by_position(self, position):
    #     for value in self.positions.values():
    #         if position == value:
    #             position=0
    #     return


if __name__ == '__main__':
    board = Board()
    print(board)
