#docstring

'''Part 2:
The exercsie of writing these functions in part two is helpful
practice in learning how to generate random values.
The data structure of having tuples inside of a list
is one that we will see multiple times throughout unit 3.
It is helpful to get familiar with it and to also be able to simulate
our own versions of lists of tuples with fake data inside them.'''


import pandas as pd
import numpy as np
import random


# part 2 functions ===================================


adjectives = ['blue','large','grainy',
'substantial','potent','thermonuclear']
nouns = ['food','house','tree','bicycle',
'toupee','phone']

list1 = [1,2,3]
list2 = [4,5,6]

def random_phrase(list1, list2):
    '''Randomly select an adjective from a list of adjectives
    a noun from a list of nouns and then concatenate them together
    returning them as a single string.'''
    item1 = random.choice(list1)
    item2 = np.random.choice(list2)
    #cast item1 and item2 so they are returned as stings
    #and can actually be added together and not cause error from
    #adding str and int which can not happen
    #makes code more generic = better
    return str(item1) + ' ' + str(item2)

print(random_phrase(adjectives, nouns))

def random_float(min_val,max_val):
    '''Returns a random float uniformly distributed
    between some in and max values'''
    return random.uniform(min_val,max_val)

# print(random_float(2,4))
# print(random_float(3,7))

def random_bowling_score():
    '''returns a random integer uniformly distibuted
    between 0 and 300'''
    return random.randint(0,300)

# print(random_bowling_score())

def silly_tuple():
    '''returns a tuple that contains 3 items:
    - a random adjective-noun string, the second should be
    - a float representing a star-rating between 1 and 5 (rounded to 1 decimal place)
    - a  bowling score between 0 and 300.'''
    return (random_phrase(), round(random_float(1,5), 1), random_bowling_score())

# print(silly_tuple())
# print(silly_tuple())
# print(silly_tuple())

def silly_tuple_list(num_tuples):
    '''a function that returns alist filled with a 
    designated number of tuples'''
    tuple_list = []
    for item in range(num_tuples):
        tuple_list.append(silly_tuple())
    return tuple_list

# print(silly_tuple_list(5))


# part 3 functions ===================================

'''Part 3:
Part 3 is practice in writing functions that might be truely useful 
within a punlished python package. We are writing functions that we
could theoretically import into other projects to help us do our work.

Remember that it's only required for you to implement one of the 
functions from part 3'''

test_df = pd.DataFrame(np.array([[1,2,3],[4,5,6],[7,8,9]]))
null_df = pd.DataFrame(np.array([[1,np.nan,3],[np.nan,5,6],[7,8,np.nan]]))


def null_count(df):
    '''check a dataframe for nulls and return the number of missing values'''
    return df.isnull().sum().sum()

# print(null_count(test_df))
# print(null_count(null_df))

def train_test_split(df, frac=0.8):
    '''create a train/test split function for a dataframe and return
    both the training and test sets'''
    train = df.sample(frac=frac)
    test = df.drop(train.index).sample(frac=1.0)
    return train, test

# print(train_test_split(test_df))



def randomize(df, seed):
    '''develop a randomization function that randomizes all of a dataframe and then 
    returns that randomized dataframe.
    '''
    return df.sample(frac=1.0, random_state=seed)

# print(randomize(test_df, 9))

address_df = pd.DataFrame({'address': ['890 Jennifer Brooks\nNorth Janet, WY 24785',
                                        '8394 Kim Meadow\nDarrenVille, AK 27389', 
                                        '379 cain Plaza\nJosephsberg, WY 06332', 
                                        '5803 Tina Hill\nAudreychester, VA 97036']})


def addy_split(addy_series):
    '''
    Split addresses into three columns (df['city], df['state'], df['zip']).
    you can use regexes to detect the format and pull out the important pieces.'''

    df = pd.DataFrame()
    
    city_list = []
    state_list = []
    zip_list = []

    for addy in addy_series:
        second_half = addy.split('\n')[1]
        city = second_half.split(',')[0]
        state = second_half.split()[-2]
        zip = second_half.split()[-1]

        city_list.append(city)
        state_list.append(state)
        zip_list.append(zip)

    df['city'] = city_list
    df['state'] = state_list
    df['zip'] = zip_list

    return df


# print(addy_split(address_df['address']))


def abbr_2_st(state_series, abbr_2_st=True):
    '''
    Returna new column with the full state name from a state abbreviation
    column.
    -> an input of FL would return Florida
    '''
    state_dict = {
            'AK': 'Alaska',
            'AL': 'Alabama',
            'AR': 'Arkansas',
            'AS': 'American Samoa',
            'AZ': 'Arizona',
            'CA': 'California',
            'CO': 'Colorado',
            'CT': 'Connecticut',
            'DC': 'District of Columbia',
            'DE': 'Delaware',
            'FL': 'Florida',
            'GA': 'Georgia',
            'GU': 'Guam',
            'HI': 'Hawaii',
            'IA': 'Iowa',
            'ID': 'Idaho',
            'IL': 'Illinois',
            'IN': 'Indiana',
            'KS': 'Kansas',
            'KY': 'Kentucky',
            'LA': 'Louisiana',
            'MA': 'Massachusetts',
            'MD': 'Maryland',
            'ME': 'Maine',
            'MI': 'Michigan',
            'MN': 'Minnesota',
            'MO': 'Missouri',
            'MP': 'Northern Mariana Islands',
            'MS': 'Mississippi',
            'MT': 'Montana',
            'NA': 'National',
            'NC': 'North Carolina',
            'ND': 'North Dakota',
            'NE': 'Nebraska',
            'NH': 'New Hampshire',
            'NJ': 'New Jersey',
            'NM': 'New Mexico',
            'NV': 'Nevada',
            'NY': 'New York',
            'OH': 'Ohio',
            'OK': 'Oklahoma',
            'OR': 'Oregon',
            'PA': 'Pennsylvania',
            'PR': 'Puerto Rico',
            'RI': 'Rhode Island',
            'SC': 'South Carolina',
            'SD': 'South Dakota',
            'TN': 'Tennessee',
            'TX': 'Texas',
            'UT': 'Utah',
            'VA': 'Virginia',
            'VI': 'Virgin Islands',
            'VT': 'Vermont',
            'WA': 'Washington',
            'WI': 'Wisconsin',
            'WV': 'West Virginia',
            'WY': 'Wyoming'
    }

    def abbrev_replace(abbrev):
        return state_dict[abbrev]

    def state_replace(state_name):
        reverse_state_dict = dict((v, k) for k, v in state_dict.items()) 
        return reverse_state_dict[state_name]

    if abbr_2_st:
        return state_series.apply(abbrev_replace)
    else:
        return state_series.apply(state_replace)
    

addy_states = addy_split(address_df['address'])['state']

full_state_names_col = abbr_2_st(addy_states)


# print(abbr_2_st(full_state_names_col, abbr_2_st=False))
# # print(abbr_2_st(addy_states))





def list_2_series(list_2_series, df):
    '''
    Single function to take a list and dataframe, tturn it into a series,
    and add it to a dataframe as a new column.
    '''
    new_column = pd.Series(list_2_series)
    return pd.concat([df, new_column], axis=1)

# print(list_2_series([10, 11, 12], test_df))


outlier_df = pd.DataFrame(
    {'a': [1, 2, 3, 4, 5, 6],
     'b': [4, 5, 6, 7, 8, 9],
     'c': [7, 1000, 9, 10, 11, 12]}
)

def rm_outlier(df):
    '''
    A 1.5*interquartile range outlier detection/removal function that
    gets rid of outlying rows and an outlier free/cleaned dataframe.
    '''
    

    cleaned_df = pd.DataFrame()

    for (columnName, columnData) in df.iteritems():
        Q1 = columnData.quantile(0.25)
        Q3 = columnData.quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - (1.5*IQR)
        upper_bound = Q3 + (1.5*IQR)
        # print(lower_bound, upper_bound)

        mask = columnData.between(lower_bound, upper_bound, inclusive='both')
        cleaned = columnData.loc[mask]
        
        cleaned_df[columnName] = cleaned

    return cleaned_df


# print(rm_outlier(outlier_df))


def split_dates(date_series):
    '''
    a function that takes in a date series and splits all dates inside
    by the month, day , and year. It then will append month day and year to 3 seperate
    lists and those lists are then used to form the columns of a new dataframe of the
    same dates and headers of each column of month, day, year.
    '''
    # mm/dd/yyyy
    df = pd.DataFrame()

    month_list = []
    day_list = []
    year_list = []
    
    for date in date_series:
        month_list.append(date.split('/')[0])
        day_list.append(date.split('/')[1])
        year_list.append(date.split('/')[2])

    df['month'] = month_list
    df['day'] = day_list
    df['year'] = year_list

    return df




# print(split_dates(pd.Series(['01/13/2016', '02/14/2017', '03/15/2018', '04/16/2019'])))