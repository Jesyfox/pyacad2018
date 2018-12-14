class Board(object):

    def __init__(self, size):
        self.matrix = [[0 for x in range(size)] for y in range(size)]
        self.directions = {'UP': (-1, 0), 'DOWN': (1, 0),
                           'LEFT': (0, -1), 'RIGHT': (0, 1)}
        self.isRuning = True

    def __repr__(self):
        return str(self.matrix).replace('], [', '\n'*2).replace(',', '  ')[2:-2]

    def move(self, command):
        """
        moves all elements > 0
        and merges equaled.
        """
        line_move, col_move = self.directions[command]
        for lines in range(len(self.matrix)):
            for element in range(len(self.matrix[0])):
                line = lines + line_move
                col = element + col_move
                try:
                    if line < 0 or col < 0:
                        raise IndexError
                    else:
                        way_element = self.matrix[line][col]
                        moving_element = self.matrix[lines][element]
                        if moving_element and moving_element == way_element:
                            self.matrix[line][col] = moving_element*3
                            self.matrix[lines][element] = 0
                            self.move(command)
                        elif not way_element and moving_element:
                            self.matrix[line][col] = moving_element
                            self.matrix[lines][element] = 0
                            self.move(command)
                        else:
                            pass
                except IndexError:
                    continue

    def random_num(self):
        """
        Generetes random number from 'avalible_nums' var and place it on the matrix
        """
        from random import choice
        avalible_nums = [3, 9]
        avalible_elements = []
        for lines in range(len(self.matrix)):
            for element in range(len(self.matrix[0])):
                if not self.matrix[lines][element]:
                    avalible_elements.append((lines, element))
                else:
                    continue

        if avalible_elements:
            chosen_line, chosen_col = choice(avalible_elements)
            self.matrix[chosen_line][chosen_col] = choice(avalible_nums)
        else:
            self.isRuning = False

    def check(self):
        """
        Check all posible moves on  matrix,
        if its 0 game is ending
        """
        posible_moves = 0
        neibours_index = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for line in range(len(self.matrix)):
            for col in range(len(self.matrix[0])):
                main_element = self.matrix[line][col]
                for index in neibours_index:
                    neibor_line, neibor_col = index
                    try:
                        if main_element == self.matrix[line + neibor_line][col + neibor_col] or main_element is 0:
                            posible_moves += 1
                    except IndexError:
                        continue
        if posible_moves:
            pass
        else:
            self.isRuning = False
            
    def count(self):
        """
        count all elements from matrix
        """
        points = 0
        for line in range(len(self.matrix)):
            for col in range(len(self.matrix[0])):
                points += self.matrix[line][col]
        return points


if __name__ == '__main__':
    size = int(input('Enter a size of a board: '))

    game = Board(size)
    game.random_num()
    commands = {'s': 'DOWN', 'w': 'UP', 'a': 'LEFT', 'd': 'RIGHT'}

    print('type:\n W for UP\n S for DOWN\n  A for LEFT\n D for RIGHT: \n')

    while game.isRuning:
        game.check()
        print(game)
        player_comand = input('comand: ').lower()
        try:
            game.move(commands[player_comand])
        except KeyError:
            print('WRONG COMAND!')
            continue
        game.random_num()

    print('THE END')
    print('your score:', game.count())
