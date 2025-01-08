# Grade-Processing-with-Python

In this project, I use Python to process CSV files containing multiple grades and generate corresponding letter grades.

The first two cells are the last name and the first name of the student. The rest of the data is as follows:
- 8 Preparations scores, with a maximum grade of 10
- 8 Labs scores, with a max grade of 30
- 2 Project scores with a max grade of 100
- 4 Exam scores with a max grade of 160

Additional Info: 
- The two lowest lab scores are dropped before averaging. 
- The lowest exam score is also dropped.

Each function validates that the input scores are numeric and within the allowed ranges, raising errors if these conditions are unmet.
The scores are then averaged and rounded to the nearest tenth. The `check_numeric` helper function ensures scores are numeric.

