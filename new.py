import os
 
# Function to Get the current
# working directory
def current_path():
    print("Current working directory before")
    print(os.getcwd())
    print()
 
 
# Driver's code
# Printing CWD before
current_path()
 
# Changing the CWD
os.chdir(r'c:\Users\BANERJEES\Desktop\[CN] Machine Learning\movie-recommender-system-tmdb-dataset-main\movie-recommender-system-tmdb-dataset-main')
 
# Printing CWD after
current_path()