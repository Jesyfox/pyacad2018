class Board(object):

    def __init__(self, size):
        self.matrix = [[0 for x in range(size)] for y in range(size)]
        self.directions = {'UP': (-1, 0), 'DOWN': (1, 0),
                           'LEFT': (0, -1), 'RIGHT': (0, 1)}
        self.matrix[1][2] = 2
        self.matrix[0][2] = 2
        self.matrix[2][2] = 2
        self.matrix[3][2] = 2
    def __repr__(self):
        return str(self.matrix).replace('], [', '\n'*2).replace(',', '  ')[2:-2]

    def move(self, command):
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
        pass

if __name__ == '__main__':
    test = Board(4)
    print(test)

    test.move('UP')
    print('\n')

    print(test)

