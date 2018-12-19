__author__ = 'Bogdan.S'


def starting_options():
    """
    start player dialog:
        the number of armies (2 <= n)
        the choice of attack strategy per army  (pick |random|weakest|strongest| army)
        the number of squads per army (2 <= n)
        the number of units per squad (5 <= n <= 10)

    its all returns the dict file
    example:
    dict = {'army_1':{
                'armies': {
                    'alpha': {'srategy': 'random', units: 6},
                    'beta': {'srategy': 'weakest', units: 8}
                    }
                'vehicles': {
                    'T-34': {'srategy': 'random', units: 3},
                    }
            'army_2':{
                'armies': {
                    'alpha': {'srategy': 'random', units: 6},
                    'beta': {'srategy': 'strongest', units: 10}
                    }
            }
    """
    pass


if __name__ == '__main__':
    starting_options()

