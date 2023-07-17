class User:
    def __init__(self, name: str) -> None:
        self.name = name

    def move_piece(self, piece_name, new_position, board):
        """
        Update position dictionary
        
        params:
        - piece (str): piece name
        - new_position (int): 움직이고 난 뒤에 피스 위치
        - board (Board class): 보드 클래스입니다

        return:
        - True, False: piece가 new_position으로 이동할 수 있는지      
        """

        if not piece_name in board.positions: #피스네임이 딕셔너리 키 안에 없을때:
            print('잘못된 이름입니다')
            return False
        current_position=board.positions[piece_name][1]

        # 자기턴에 자기 말만 움직임 가능
        if self.name != board.positions[piece_name][0]:
            print('다른팀 말을 선택했습니다')
            return False
        
        
        # y축은 5이상, 0이하의 수를 입력할 수 없음, x축은 4이상, 0이하의 수를 입력할 수 없음, 상대진영에 못놓음
        if new_position%10>=5 or new_position//10>=4 or new_position%10<=0 or new_position//10<=0:
            print('보드 밖입니다')
            return False
        
        if self.name== 'user1':
            if new_position%10==4:
                if current_position==0:
                    return False
                elif piece_name=='자1':
                    piece_name='후1'
                    board.positions['후1'] = board.positions.pop('자1')
                elif piece_name=='자2':
                    piece_name='후2'
                    board.positions['후2'] = board.positions.pop('자2')

        else:
            if new_position%10==1:
                if current_position==5:
                    return False
                elif piece_name=='자1':
                    piece_name='후1'
                    board.positions['후1'] = board.positions.pop('자1')
                elif piece_name=='자2':
                    piece_name='후2'
                    board.positions['후2'] = board.positions.pop('자2')



        # if piece_name.startswith('자'):
        if self.name == 'user1' and board.positions[piece_name][1]%5!=0:
            if piece_name =='자1':
                자1_xposition=board.positions['자1'][1]//10
                자1_yposition=board.positions['자1'][1]%10
                if new_position%10-자1_yposition != 1:
                    print("Invalid y position!")
                    return False
                if 자1_xposition != new_position//10:
                    print("Invalid x position!")
                    return False
            if piece_name =='자2':
                자2_xposition=board.positions['자2'][1]//10
                자2_yposition=board.positions['자2'][1]%10
                if new_position%10-자2_yposition != 1:
                    print("Invalid y position!")
                    return False
                if 자2_xposition != new_position//10:
                    print("Invalid x position!")
                    return False
            if piece_name == '왕1':
                왕1_xposition=board.positions['왕1'][1]//10
                왕1_yposition=board.positions['왕1'][1]%10
                if abs(new_position%10-왕1_yposition) >=2:
                    print("Invalid y position!")
                    return False
                if abs(new_position//10-왕1_xposition) >=2:
                    print("Invalid x position!")
                    return False
            if piece_name == '왕2':
                왕2_xposition=board.positions['왕2'][1]//10
                왕2_yposition=board.positions['왕2'][1]%10
                if abs(new_position%10-왕2_yposition) >=2:
                    print("Invalid y position!")
                    return False
                if abs(new_position//10-왕2_xposition) >=2:
                    print("Invalid x position!")
                    return False
            if piece_name == '장1':
                장1_xposition=board.positions['장1'][1]//10
                장1_yposition=board.positions['장1'][1]%10
                if abs(new_position%10-장1_yposition) >=2:
                    print("Invalid y position!")
                    return False
                if abs(new_position//10-장1_xposition) >=2:
                    print("Invalid x position!")
                    return False
                if  new_position%10-장1_yposition!=0 and new_position//10-장1_xposition!=0:
                    print("Invalid xy position!")
                    return False
            if piece_name == '장2':
                장2_xposition=board.positions['장2'][1]//10
                장2_yposition=board.positions['장2'][1]%10
                if abs(new_position%10-장2_yposition) >=2:
                    print("Invalid y position!")
                    return False
                if abs(new_position//10-장2_xposition) >=2:
                    print("Invalid x position!")
                    return False
                if  new_position%10-장2_yposition!=0 and new_position//10-장2_xposition!=0:
                    print("Invalid xy position!")
                    return False
            if piece_name == '상1':
                상1_xposition=board.positions['상1'][1]//10
                상1_yposition=board.positions['상1'][1]%10
                if abs(new_position%10-상1_yposition) >=2:
                    print("Invalid y position!")
                    return False
                if abs(new_position//10-상1_xposition) >=2:
                    print("Invalid x position!")
                    return False
                if  new_position%10-상1_yposition==0 or new_position//10-상1_xposition==0:
                    print("Invalid xy position!")
                    return False
            if piece_name == '상2':
                상2_xposition=board.positions['상2'][1]//10
                상2_yposition=board.positions['상2'][1]%10
                if abs(new_position%10-상2_yposition) >=2:
                    print("Invalid y position!")
                    return False
                if abs(new_position//10-상2_xposition) >=2:
                    print("Invalid x position!")
                    return False
                if  new_position%10-상2_yposition==0 or new_position//10-상2_xposition==0:
                    print("Invalid xy position!")
                    return False   
            if piece_name == '후1':
                후1_xposition=board.positions['후1'][1]//10
                후1_yposition=board.positions['후1'][1]%10
                if abs(new_position%10-후1_yposition) >=2:
                    print("Invalid y position!")
                    return False
                if abs(new_position//10-후1_xposition) >=2:
                    print("Invalid x position!")
                    return False
                if 후1_yposition - new_position%10 == 1 and 후1_xposition != new_position//10:
                    print("Invalid xy position!")
                    return False  

# TODO: user2 이동 만들기
        
        for k, v in board.positions.items():
            if v[1] == new_position:
                
                # 같은 팀이 있는 곳으로는 못감
                if self.name==v[0]:
                    print("같은 팀 말!")
                    return False
                
                # 말을 잡았을 때 턴에 따라 각자의 무덤으로 말이 이동
                elif self.name=='user1':
                    board.positions[k]=(board.user1, 0)
                    break
                else:
                    board.positions[k]=(board.user2, 5)
                    break
        if k=='후1':
            board.positions['자1'] = board.positions.pop('후1')
        if k=='후2':
            board.positions['자2'] = board.positions.pop('후2')
                
    
        board.positions[piece_name]= (self.name, new_position)
        return True

    

    


        

    def select_grave(self, piece, position):
        #같은 피스가 두개 있을수 있음 주의
        pass