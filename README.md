# Grade-Processing-with-Python

# Score Calculation Module

In this project, I use Python to process CSV files containing multiple grades and generate corresponding letter grades.

Some limitations: 
-The `get_prep_scores` function handles preparation scores, which must not exceed 10. 
-The `get_lab_average` function processes lab scores, with each score capped at 30, and drops the two lowest scores before averaging. 
-The `get_project_average` function calculates the average for project scores, each of which can be up to 100. 
-The `get_exam_average` function averages exam scores, dropping the lowest, with each score having a maximum score of 160.

Each function validates that the input scores are numeric and within the allowed ranges, raising errors if these conditions are unmet.
The scores are then averaged and rounded to the nearest tenth. The `check_numeric` helper function ensures scores are numeric.
