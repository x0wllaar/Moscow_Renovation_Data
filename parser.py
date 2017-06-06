import pandas as pd
import numpy as np
import json
import sys

#From https://stackoverflow.com/a/19647596
def flatten_dict(dd, separator='_', prefix=''):
    return { prefix + separator + k if prefix else k : v
             for kk, vv in dd.items()
             for k, v in flatten_dict(vv, separator, kk).items()
             } if isinstance(dd, dict) else { prefix : dd }

if len(sys.argv) < 3:
    print('Usage: ' + sys.argv[0] + ' infile.json outfile.csv')
    exit(1)

infile = sys.argv[1]
outfile = sys.argv[2]

print('Parsing JSON from ' + infile)    
data = pd.read_json(infile)
print('Data for ' + str(len(data)) + ' buildings')

print('Parsing...')
new_df_dl = list()
for row in data['card_fields']:
    new_dict = flatten_dict(row)
    new_df_dl.append(new_dict)
new_df = pd.DataFrame(new_df_dl)

print('Saving to ' + outfile)
new_df.to_csv(path_or_buf=outfile)