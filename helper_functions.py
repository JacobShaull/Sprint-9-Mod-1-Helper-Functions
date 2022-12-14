import pandas as pd
import numpy as np
import random


# Part 2 Functions =============================

adjectives = ['blue', 'large', 'grainy',
            'substantial', 'soft', 'thermonuclear']

nouns = ['food', 'house', 'tree', 'bicycle', 'toupee', 'phone']

def random_phrase():
    adj = random.choice(adjectives)
    #noun = np.random.choice(nouns)
    #random_index = random.randint(0,len(nouns)-1)
    #noun = nouns[random_index]
    noun = random.sample(nouns, 1)[0]

    return adj + ' ' + noun

#print(random_phrase())
#print(random_phrase())
#print(random_phrase())

def random_float(min_val,max_val):
    return random.uniform(min_val, max_val)

#print(random_float(2,4))
#print(random_float(2,4))
#print(random_float(2,4))


def random_bowling_score():
    return random.randint(0,300)

#print(random_bowling_score())
#print(random_bowling_score())
#print(random_bowling_score())


def silly_tuple():
    return(random_phrase(), round(random_float(1,5),1),  random_bowling_score())

#print(silly_tuple())
#print(silly_tuple())
#print(silly_tuple())


def silly_tuple_list(num_tuples):
    tuple_list = []
    for item in range(num_tuples):
        tuple_list.append(silly_tuple())

    return tuple_list

#print(silly_tuple_list(5))


#Part 3 Functions ======================================================

test_df = pd.DataFrame(np.array([[1,2,3],[4,5,6],[7,8,9]]))
null_df = pd.DataFrame(np.array([[1,np.nan,3],[4,5,np.nan],[np.nan,8,np.nan]]))

def null_count(df):
    return df.isnull().sum().sum()

print(null_count(test_df))
print(null_count(null_df))

# Time 33:25 for the rest of the functions
#Link: https://bloomtech.instructure.com/courses/2363/pages/module-1-project-solution-video?module_item_id=661781
