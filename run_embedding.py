from python.embeddings import exercise_3

if __name__ == '__main__':
    exercise = input('Into the exercise: ')
    eval(f'exercise_{exercise}').executor()