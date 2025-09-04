import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
'''
이상의 코드라인을 확인하면 내부의 element가 복수의 라인으로 이루어진 str인 list라고 할 수 있습니다.
'''

#todo - 1 : 남은 기회 숫자를 추적하기 위한 lives 변수를 선언하고 6으로 초기화하세요.
lives = 6

#todo - 2 : hangman03을 참조하여 while 반복문 바깥은 완성하시오.
word_list = ['apple', 'banana', 'camel']
chosen_word = random.choice(word_list)
print(chosen_word)
display = []
for _ in range(len(chosen_word)):
    display.append('_')
print(display)
#todo - 3 : while문의 조건을 수정하여 6 번의 기회가 소진되면 반복문이 종료될 수 있도록 작성하시오.
end_of_game = False
while not end_of_game:
    guess = input('알파벳을 입력하시오 >>>').lower()
    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = guess
        # else:
        #     lives -= 1
        #     print(stages[lives])
        #     if lives == 0:
        #         end_of_game = True
        #         print('game over')
        # 라고 작성하시면 안됩니다. 반복문 내부에서 guess가 일치하는지 여부를 따지는 중입니다. 예를 들어 chosen_word가 apple이고, guess가 a라고 가정했을 때, 첫 번째 반복에서는 display의 0번지가 a로 바뀝니다. 그렇다면 내부에 위치해 있기 때문에 1, 2, 3, 4번지에 대해서도 a가 display의 인덱스와 인치하는 element인지를 확인하게 됩니다. 그 결과 p p l e가 a와 다르기 때문에 lives -= 1 이 4번 적용되어서 맞는 답을 입력했음에도 불구하고 행맨이 완성되는 것을 확인할 수 있게 됩니다.

    # 우리는 이상을 이유로 for 반복문의 바깥에서 guess가 chosen_word에 속하지 않는지를 확인하는 조건문을 '별개로' 작성해야만 합니다.
    # 틀렸을 때 lives를 1씩 감하고 0이 되었을 때 game over 시키는 부분
    if guess not in chosen_word:
        lives -= 1
        print(f'당신의 기회는 {lives} 번 남았습니다.')
        print(stages[lives])
    if lives == 0:
        end_of_game = True
        print('game over')
        print(f'정답은 {chosen_word} 입니다.')
    if '_' not in display:
        end_of_game = True
        print('정답입니다!💕')
        print(f'정답은 {chosen_word} 입니다.')

    # 현재 상황이 콘솔창에 출력돼서 user에게 안내가 가면 좋겠네요
    print(' '.join(display))

#todo - 4 : lives의 변수와 stages 리스트의 관계를 파악하여 guess를 입력할 때 마다 올바른 stages의 element가 출력될 수 있도록 작성하시오.

# 현재 기준에서 아까 완성판과 차이점 : logo 유무 / word_list가 부족함 / 혹시나 리팩토링 가능한지 여부
# hangman05 파일 생성 -> 필요한 부분들 다 복사 하고 주석들 정리
# logo를 text to ascii arts를 검색해서 하나 받아와서 맨 처음에 로고를 출력할 수 있도록 코드를 완성하겠습니다.




