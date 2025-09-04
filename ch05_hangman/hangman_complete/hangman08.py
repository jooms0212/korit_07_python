def play_hangman():
    import random
    from hangman_arts import logo, stages
    from hangman_word_list import word_list

    print(logo)
    chosen_word = random.choice(word_list)

    lives = 6
    display = []
    for _ in range(len(chosen_word)):
        display.append('_')
    print(display)

    end_of_game = False
    while not end_of_game:
        guess = input('알파벳을 입력하시오 >>>').lower()
        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                display[i] = guess

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

        print(' '.join(display))

play_hangman()