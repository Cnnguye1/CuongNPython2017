import random
import math
def Score_and_Graces(numb):
    """random_num = math.floor(random.random()*(100 -60) + 60)
    print random_num"""
    for count in range(numb):
        random_num = random.randint(60,100)
        if random_num >=90:
            print "Score:", str(random_num) + "; Your grade is A"
        elif random_num >=80:
            print "Score:", str(random_num) + "; Your grade is B"
        elif random_num >=70:
            print "Score:", str(random_num) + "; Your grade is C"
        else:
            print "Score:", str(random_num) + "; Your grade is D"
    print "End of the program. Bye!!"
    return

x = Score_and_Graces(10)