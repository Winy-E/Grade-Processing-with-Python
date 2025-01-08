# Winy

import os 

def check_numeric(s, message, student_name):
    """Check whether or not all the characters in a string are numeric values and
       print an error message if the string contains non-numeric values except if
       the first character is a (-) sign. s is the name of the string. message is the
       error message that will appear"""
    if s=="-" or s=="":
        raise ValueError(f"{student_name}: {message}")
    if "\n" in s:
        s= s[:s.index("\n")]
    if s[0] == '-':
        s = s[1:]
    for c in s:
        if c not in "0123456789":        					  # if c is not a numeric value...
            raise ValueError(f"{student_name}: {message}")    # raise value error

def get_prep_scores(scores, student_name):
    """Compute the average percentage of the preparations scores. The percentage is
       rounded to the nearest tenth. Raise error if a preparation score is negatif,
       is not numeric or is higher than 10"""
    total = 0
    for score in scores:
        check_numeric(score, "The preparation scores must be integers", student_name)
        score = float(score)
        if score < 0:
            raise ValueError(f"{student_name}: The preparation scores cannot be smaller than 0")
        elif score > 10:
            raise ValueError(f"{student_name}: The preparation scores cannot be higher than 10")
        total += score
    total = total / len(scores) * 100 / 10
    return round(total, 1)        # return the average percentage rounded to the nearest tenth

def get_lab_average(scores, student_name):
    """Drop the two lowest lab scores and calculate the average percentage
       of the lab scores.The percentage is rounded to the nearest tenth. Raise
       error if a lab score is negative, is not numeric, or is higher than 30"""
        
    total = 0
    newlist = []
    for score in scores:
        check_numeric(score, "The lab scores must be integers", student_name)
        score = float(score)
        if score < 0:
            raise ValueError(f"{student_name}: The lab scores cannot be negative numbers")
        elif score > 30:
            raise ValueError(f"{student_name}: The lab scores cannot be higher than 30")
        newlist.append(score)
    newlist.remove(min(newlist))
    newlist.remove(min(newlist))
    for score in newlist:
        total += score
    lab_average = (total / len(newlist)) / 30 * 100
    return round(lab_average, 1)   # return the average percentage rounded to the nearest tenth

def get_project_average(scores, student_name):
    """Compute the average percentage of the projects scores. The percentage is rounded
       to the nearest tenth. Raise error if a project score is negatif,
       is not numeric or is higher than 100"""
    total = 0
    for score in scores:
        check_numeric(score, "The project scores must be integers", student_name)
        score = float(score)
        if score < 0:
            raise ValueError(f"{student_name}: The project scores cannot be smaller than 0")
        elif score > 100:
            raise ValueError(f"{student_name}: The project scores cannot be higher than 100")
        total += score
    project_average = total / len(scores)
    return round(project_average, 1)
    
def get_exam_average(scores, student_name):
    """Drop the lowest lab score and calculate the average percentage of the exam scores.
   The percentage is rounded to the nearest tenth. Raise error if an exam score is negatif,
    is not numeric or is higher than 160"""
    
    total = 0
    min_score = 161
    
    for score in scores:
        check_numeric(score, "The exam scores must be integers", student_name)
        score = float(score)
        if score < 0:
            raise ValueError(f"{student_name}: The exam scores cannot be negative numbers")
        elif score > 160:
            raise ValueError(f"{student_name}: The exam scores cannot be higher than 160")
        total += score
        if score < min_score:
            min_score = score
            
    total = (total - min_score) / (len(scores) - 1)
    exam_average = total * 100 / 160
    return round(exam_average, 1)           # return the average percentage rounded to the nearest tenth
        
def get_grade(score):
    """determine the letter grade. 90 and higher is A. 80 to 89 is B.
       70 to 79 is C. 60 to 69 is D. Below 60 is F"""
    if score >= 90:
        grade="A"
    elif score >= 80:
        grade="B"
    elif score>=70:
        grade="C"
    elif score>=60:
        grade="D"
    else:
        grade="F"
    return grade


def main():
    """this functions reads grade data from a CSV file called grades.csv . 
       It computes the average percentage rounded to the nearest tenth of each type
       of assignment. Then, it compute the weighted average grade, and the letter
       grade in the class. Lastly, it writes the results to a csv file called final_grades.csv"""
    
    lines = []    #list that will contain the data that will be written in the output file 
    
    try:
        fin = open("grades.csv")
         
        for line in fin:
            #read the values
            tokens = line.split(",")
            lname = tokens[0]   # read the last name
            fname = tokens [1] # read the first name
            student_name = fname+ " "+ lname
            
            if type(lname)!= str or type(fname) != str:
                raise ValueError(f"{student_name}: The first two values must be names")
            
            prep_scores= tokens[2:10]    # read the preparations scores
            lab_scores=tokens[10:18]     # read the labs scores
            project_scores=tokens[18:20] # read the projects scores
            exam_scores=tokens[20:24]    # read the exams scores
            
            # Compute the average of each type of assignment in percentage
            preparations = get_prep_scores(prep_scores, student_name)     # calculate the preparations average
            labs = get_lab_average(lab_scores, student_name)              # calculate the labs averages
            projects = get_project_average(project_scores, student_name)  # calculate the projects average
            exams = get_exam_average(exam_scores, student_name)           # calculate the exams average
            
            weighted_average = (preparations*.08 + labs*.24 + projects*.20 +exams*.48)
            weighted_average = round(weighted_average,1)
            grade = get_grade(weighted_average)
            
            # append the names, average percentages, weighted averages and grades in a list 
            line = [lname+ ","+fname+","+ str(preparations)+ ","+str(labs)+","+ str(projects)+","+\
                    str(exams)+","+ str(weighted_average)+"," + str(grade) + "\n"]
            lines.append(line)

        try:
            if os.path.exists("final_grades.csv"):                                        # if the ouput file already exists on the disk...
                raise NameError("The file 'final_grades.csv' already exists on your disk")# display error message
            else:                                                             
                fout = open("final_grades.csv", 'a')
        
                # write data on the output file
                for line in lines:
                    for word in line:
                        fout.write(str(word))
                    
        except IOError:                                                    # if the outpout file cannot be created...        
            print("Error, the file 'final_grades.csv' cannot be created")  # display error message
                
        fout.close()
        fin.close()

        
    except FileNotFoundError:                        # if the input file does not exist...
        print("The file 'grades.csv' does not exist") # display error message
    
    except Exception as e:      
        print(e)

            
    
if __name__ == '__main__':
    main()
