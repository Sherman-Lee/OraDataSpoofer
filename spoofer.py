import numpy as np
import pandas as pd
import random
import string

def fake_floats(min, max, records):
    col1 = np.random.randint(min, high=max, size=records)
    col2 = np.random.random((records,))
    col = np.multiply(col1, col2)
    return col

def fake_ints(min, max, records):
    col = np.random.randint(min, high=max, size=records)
    return col

def fake_maps(min, max, records, dictionary):
    tmp = np.random.randint(min, high=max, size=records)
    col = [dictionary[x] for x in tmp]
    return col

def fake_dates(base_date, min, max, records):
    days = np.random.randint(min, high=max, size=records)
    col = np.add(np.datetime64(base_date), days)
    return col

def fake_emails(records,length):
    rstr = [''.join(random.choices(string.ascii_letters + string.digits, k=length)) for _ in range(records)]
    at = ['@ora.com' for _ in range(records)]
    col = np.core.defchararray.add(rstr, at)
    return col

def fake_zips(records):
    col1 = np.random.randint(00000, high=99999, size=records)
    col = [str(z).zfill(5) for z in col1]
    return col
    
def load_nouns():
    nouns = set()
    input_file = open('nounlist.txt','r')
    for line in input_file:
        line = line.replace("\n", "")
        nouns.add(line)
    return nouns

def gen(headers, records, items):
    output = pd.DataFrame([])
    emailLen = 15

    if (items == ""):
        items = dict(enumerate(load_nouns()))
    else:
        words = items.split("\n")
        items = dict(enumerate(words))

    for h in headers:
        min = h[1]
        max = h[2]
        if h[3] == 'Strings':
            col = fake_maps(min, max, records, items)
        elif h[3] == 'Floats':
            col = fake_floats(min, max, records)
        elif h[3] == 'Ints':
            col = fake_ints(min, max, records)
        elif h[3] == 'Dates':
            col = fake_dates('2010-01-01', min, max, records)
        elif h[3] == 'Emails':
            col = fake_emails(records, emailLen)
        elif h[3] == 'Zips':
            col = fake_zips(records)
        else:
            raise ValueError('Header \"' + h[0] + '\" is unqualified.') 

        df = pd.Series(col)

        output.insert(loc = len(output.columns), column=h[0], value=df)
    
    print(output)
    output.to_csv('output.csv', index=False)