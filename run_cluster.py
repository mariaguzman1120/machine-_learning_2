from python.clustering import (exercise_3, exercise_4, exercise_5, exercise_6)

if __name__ == '__main__':
    exercise = input('Into the exercise: ')
    eval(f'exercise_{exercise}').executor()