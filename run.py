from python.homework import (exercise_1, exercise_2, exercise_3, exercise_4, exercise_5)

if __name__ == '__main__':
    exercise = input('Into the exercise: ')
    eval(f'exercise_{exercise}').executor()