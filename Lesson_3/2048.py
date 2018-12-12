class Board(object):

    directions = {'UP': (0, 1), 'DOWN': (0, -1),
                  'LEFT': (-1, 0), 'RIGHT': (1, 0)}

    def __init__(self, size):
        self.matrix = [[0 for x in range(size)] for y in range(size)]
        self.matrix[2][2] = 2

    def __repr__(self):
        return str(self.matrix).replace('], [', '\n'*2).replace(',', '  ')[2:-2]

    def move(self, comand):
        line_move, col_move = comand
        pass

    def random_num(self):
        pass

if __name__ == '__main__':
    test = Board(4)
    print(test)

