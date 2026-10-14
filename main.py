# ─────────────────────────────────────────────────────────────
# SDE Escape Room
#
# This file grows across SDE lessons 5–9 and is polished in L10.
#   L5  Input & If/Else      — print intro + ask the player's name
#   L6  Random & While Loops — random rooms + a main game loop
#   L7  2D Maps & Movement   — grid map + N/S/E/W movement
#   L8  Puzzle Functions     — refactor puzzles into functions + walls
#   L9  Final Customization  — theme, story, win/lose screens
#   L10 Polish & Stretch     — pick from key item, time limit,
#                              hunger, math puzzle, etc.
#
# Keep working in this single file unless your instructor says
# otherwise. Save often — your work persists between lessons.
# ─────────────────────────────────────────────────────────────
import random

print("You wake up, alone, not knowing anything except for your name, in a maze filled with what seems like darkness... ")
# TODO (L5): ask the player for their name and greet them.
name = input('Then you here a whisper emanating from the darkness, it asks for your name... ')
print(f"Hello {name}, you are trapped in a maze, but it isn't an ordinary maze as you can see. It is a maze full of darkness, and what lurks within it.")
print(f'You see 3 doors, and as if on command the voice says,')
door = input(f'Pick a door: 1, 2, or 3')
correct_door = random.choice(["1", "2", "3"])
while door != correct_door:
  print('Door stuck, try again...')
  door = input('Pick again: 1, 2, 3 ')
  
print('The door swings open and you walk through.')

#Added guess limit for L9 + puzzle attempt limit to prevent retries (not_again)
def puzzle():
  password = random.choice(["Dark", "Maze", "Escape"])
  guess_count = 0
  while guess_count < 2:
    while not_again >= 1:
      print('Already attempted')
      break
    if not_again >= 1:
      break
    guess = input('Choose a phrase to solve the puzzle, you may gain something you want: Dark, Maze, Escape')
    if guess == password:
      print('Correct.')
      print('To regain your memories you must retrieve a key...')
      return True
    else:
      guess_count += 1
      print('The ground shakes beneath you...')
      print(f'Incorrect. {2 - guess_count} tries left.')
  if guess_count == 2:
    print('Failed, no tries left.')
    return False
  
def math_puzzle():
  int1 = random.choice(range(0, 16))
  int2 = random.choice(range(0,16))
  math_password = int1 * int2
  p_guess = int(input(f'What is the product of {int1} and {int2}? '))
  while p_guess != math_password:
    #p_guess = input(f'What is the product of {int1} and {int2}? ')
    #if p_guess == math_password:
      #print('Correct')
    if p_guess != math_password:
      print('Incorrect...')
      p_guess = int(input(f'What is the product of {int1} and {int2}? '))
  print('Correct')  
      
def announce_walls(current_row, current_col):
    # up  
    if room[current_row - 1][current_col] == "x":
        print("There is a wall above you.")
    # down
    if room[current_row + 1][current_col] == 'x':
        print('There is a wall below you.')
    # left
    if room[current_row][current_col - 1] == 'x':
        print('There is a wall to the left of you.')
    # right
    if room[current_row][current_col + 1] == 'x':
        print('There is a wall to the right of you.')

#x = 'wall'
#. = 'path'
#e = 'escape tile'
#add t for true exit that needs key (has_key = True)
room = [
  'xxxxxxxxxx',
  'x.......xx',
  'x.x.mx..tx',
  'x.x..x..xx',
  'xkp.x.p..x',
  'xx.em.x..x',
  'xxxxxxxxxx'
]
def check_tile(current_row, current_col):
  if current_row < 0 or current_row >= len(room):
    return False
  if current_col < 0 or current_col >= len(current_row):
    return False
  else:
    return room[current_row][current_col] != 'x'

def move(current_row, current_col, direction, room):
  if direction == 'up':
    if room[current_row - 1][current_col] == 'x':
      print('Ouch - a wall')
      return current_row, current_col
    else:
      return current_row - 1, current_col
    if check_tile(current_row - 1, current_col):
      return current_row - 1, current_col
    else:
      return current_row, current_col
  elif direction == 'down':
    if room[current_row + 1][current_col] == 'x':
      print('Ouch - a wall')
      return current_row, current_col
    else:
      return current_row + 1, current_col
    if check_tile(current_row + 1, current_col):
      return current_row + 1, current_col
    else:
      return current_row, current_col
  elif direction == 'left':
    if room[current_row][current_col - 1] == 'x':
      print('Ouch - a wall')
      return current_row, current_col
    else:
      return current_row, current_col - 1
    if check_tile(current_row, current_col - 1):
      return current_row, current_col - 1
    else:
      return current_row, current_col
  elif direction == 'right':
    if room[current_row][current_col + 1] == 'x':
      print('Ouch - a wall')
      return current_row, current_col
    else:
      return current_row, current_col + 1
    if check_tile(current_row, current_col + 1):
      return current_row, current_col + 1
    else:
      return current_row, current_col

# Added key feature for catch-up day and math puzzle
has_key = False
not_again = 0
player_row = 1
player_col = 1
while room[player_row][player_col] != 'e': 
  announce_walls(player_row, player_col)
  direction = input('Which way? (up/down/left/right): ')
  player_row, player_col = move(player_row, player_col, direction, room)
  print(f'You are at ({player_row}, {player_col})')
  if room[player_row][player_col] == 'p':
    puzzle()
    not_again += 1
  if room[player_row][player_col] == 'm':
    math_puzzle()
  if room[player_row][player_col] == 'k':
    print('You find a strange key...')
    has_key = True
  if room[player_row][player_col] == 't' and has_key == True:
    break
  elif room[player_row][player_col] == 't' and has_key == False:
    print('You find a strange locked door...')

if room[player_row][player_col] == 'e':
  print('You escaped, but you feel like you are missing something...')
elif room[player_row][player_col] == 't' and has_key == True:
  print('You escaped, with full recollection of who you are...')
