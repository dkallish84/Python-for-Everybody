# Exercise 7: Rewrite the grade program from the previous chapter using a function called computegrade that takes a score as its parameter and returns a grade as a string.

def get_grade(g):
    if g > 1.0 or g < 0.0:
        return 'Bad score'
    elif g >= 0.9:
        return 'A'
    elif g >= 0.8:
        return 'B'
    elif g >= 0.7:
        return 'C'
    elif g >= 0.6:
        return 'D'
    else:
        return 'F'

grade = input('Enter score: ')
try:
    grade = float(grade)
    print(get_grade(grade))
except:
    print('Bad score')
