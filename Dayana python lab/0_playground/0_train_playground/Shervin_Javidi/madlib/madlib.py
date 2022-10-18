from madlib_templates import t_1, t_2, t_3, t_4
import random as rnd

# enter a list of words to generate a story
if __name__ == "__main__":
    mt = rnd.choice([t_1, t_2, t_3, t_4])
    mt.madlib()
    