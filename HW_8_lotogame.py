from random import randint, choice
from time import sleep


class LottoCard:
    def __init__(self, player_name: str):
        self.name = player_name
        self.nums = []
        self.decades = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.card = ''
        self.rows = 3
        card_row_length = 27
        while len(self.nums) < 15:
            new_num = randint(1, 90)
            decade = new_num // 10
            if self.nums.count(new_num) == 0 and self.decades[decade] < 2:
                self.nums.append(new_num)
                self.decades[decade] += 1
        self.nums.sort()
        lines = [[], [], []]
        place, row = 0, 0
        for line in lines:
            curr_decade = 0
            while len(line) < 5:
                prev_decade = curr_decade
                line.append(self.nums[3 * place + row])
                curr_decade = self.nums[3 * place + row] // 10
                if len(line) == 1:
                    if line[0] > 9 and self.nums[3 * place + row] > 9:
                        self.card += '  '
                if curr_decade == 0:
                    self.card += ' ' + str(self.nums[3 * place + row])
                elif curr_decade == 9:
                    self.card += (3 * (curr_decade - prev_decade - 2) + 1) * ' ' + str(self.nums[3 * place + row])
                else:
                    self.card += (3 * (curr_decade - prev_decade - 1) + 1) * ' ' + str(self.nums[3 * place + row])
                place += 1
            self.card += (8 - curr_decade) * 3 * ' ' + ' \n'
            row += 1
            place = 0
        self.card = self.name + (card_row_length - len(self.name)) * '_' + \
            '\n' + self.card + card_row_length * '~'


class LottoGame:
    def __init__(self, player_name: LottoCard):
        self.player = player_name.card
        print('Take a seat, prepare for a game')
        sleep(5)
        self.comp = LottoCard('Computer').card
        self.num_pool = []
        while len(self.num_pool) < 90:
            self.num_pool.append(len(self.num_pool) + 1)
        self.game()

    def game(self):
        is_ready = input('In this lotto game you should answer on presence of given number in your card'
                         '\nYou should type \"y\" when you got the number in your card'
                         '\nand you should type \"n\" when the number is not in your card.'
                         '\nIf you make a mistake then you loose.'
                         '\nComputer will do it automatically and correctly'
                         '\nSo good luck, have fun! And press Enter to begin')
        if is_ready == '':
            print('Here are Computers\' and your cards')
            player_num, comp_num = 0, 0
            while True:
                print(self.comp)
                print(self.player)
                curr_num = choice(self.num_pool)
                print(f'\nPrepare for the next number')
                sleep(1.5)
                print(f'The next number is {curr_num}')
                answer = input(f'Does your card contain {curr_num}? (y/n) ')
                self.num_pool.remove(curr_num)
                if self.player.find(' ' + str(curr_num) + ' ') != -1 and answer == 'y':
                    self.player = self.player.replace(' ' + str(curr_num), ' ' + len(str(curr_num)) * 'X', 1)
                    player_num += 1
                    print('Nice, it\'s your number. Let\'s move on!')
                    sleep(2)
                elif self.player.find(' ' + str(curr_num) + ' ') != -1 and answer == 'n':
                    print(f'\nSorry, you loose, {curr_num} is in your card\nComputer wins!\nBetter luck next time!')
                    print(self.player)
                    break
                elif self.player.find(' ' + str(curr_num) + ' ') == -1 and answer == 'y':
                    print(f'\nSorry, you loose, {curr_num} is NOT in your card\nComputer wins!\nBetter luck next time!')
                    print(self.player)
                    break
                else:
                    print(f'Right you are. {curr_num} is not in your card, move on')
                    sleep(2)
                if self.comp.find(' ' + str(curr_num) + ' ') != -1:
                    self.comp = self.comp.replace(' ' + str(curr_num), ' ' + len(str(curr_num)) * 'X', 1)
                    comp_num += 1
                    print('Computer got it, damn piece of iron')
                    sleep(2)
                if comp_num == 15 and player_num == 15:
                    print('\nThe game finished with draw')
                    print(self.comp)
                    print(self.player)
                    break
                elif comp_num == 15:
                    print('\nUnfortunately computer wins')
                    print(self.comp)
                    break
                elif player_num == 15:
                    print('\nCongratulations, you win')
                    print(self.player)
                    break
            print('Numbers remained in pool:\n', self.num_pool)


card = LottoCard('Super_player')
lotto_game = LottoGame(card)
