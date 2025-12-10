#Reading metrics from CSV

import numpy as np
#create a csv file with data 45,55,78,88,92,73,81,65
with open("file1.csv","w") as f:
    f.write("45,55,78,88,92,73,81,65")

cpu_metrics=np.loadtxt("file1.csv",delimiter=",") #np.loadtxt reads numeric data from a CSV file.
#delimiter="," tells NumPy that values in the file are separated by commas.
print(np.mean(cpu_metrics),np.max(cpu_metrics))
