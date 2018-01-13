# =======================  INITIALIZATION PARAMETERS  =========================

# Name of text file to extract grades from.
file = open('grades.txt', 'r')

# List of assignments.
A1 = 0
A2 = 1
A3 = 2
A4 = 3
A5 = 4

# Enter A1, A2, A3, A4 or A5 to see it graphed.
assignment_to_graph = A1

# ======================  /INITIALIZATION PARAMETERS  =========================



# =============================  INFORMATION  =================================
#
# Assignment 3: Histogram for Grade Distribution
# Class: CPSC 235
# By: R. Apperley
# Date: October 25th, 2016
# Scope: Program that extracts data from a text file and prints a histogram for
#        a given assignment's grade distribution.
#        As a bonus, an additional function has been created that calculates and
#        displays statistics for a given assignment.
#
# ============================  /INFORMATION  =================================



# ==============================  FUNCTIONS  ==================================

def create_grades_list(file):
    '''Function that extracts data from a text file by transforming it into a
       series of temporary strings where characters '\n', and ' ' are removed.
       The strings are then transformed into a temporary list by splitting on ',' 
       and then consolidated into a master list called grades_list. 
       Grade values are then transformed from string type to float type.'''
    grades_list = []
    for line in file:
        temp_string_1 = line
        # Removing '\n' and ' ' from each string.
        temp_string_2 = temp_string_1.replace('\n', '')
        temp_string_3 = temp_string_2.replace(' ', '')
        # Splitting string into list using ','.
        temp_list = temp_string_3.split(',')
        grades_list.append(temp_list)
    # Double nested for loop to convert string grades into float.
    for i in range(1, len(grades_list) - 1):
        for j in range(5, 10):
            grades_list[i][j] = float(grades_list[i][j])          
    return(grades_list)
        

def create_bins_list(grades_list):
    '''Function that reads through the grades_list and counts the number of
       grades that fall into each bin for each assignment. The quantity in 
       each bin is then recorded in a temporary list. The lists are then 
       consolidated into a master list called bin_list.'''
    assignment_list = ['A1', 'A2', 'A3', 'A4', 'A5']
    bin_list = []
    # Loop to iterate through each set of assignment grades.    
    for assignment in assignment_list:
        temp_list = []
        # Loop to iterate through each bin of grades.
        for i in range(11):  
            counter = 0
            # Loop to iterate through each student.
            for j in range(1, len(grades_list) - 1):             
                if (grades_list[j][assignment_list.index(assignment) + 5] >= i and (grades_list[j][assignment_list.index(assignment) + 5] < (i + 1))):
                    counter = counter + 1          
            temp_list.append(counter)
        bin_list.append(temp_list)
    return(bin_list)

    
def draw_graph(bin_list, assignment_number):
    '''Function that prints the histogram of a given assignment in Quickdraw.'''
    # Setting background color.
    print('color', 255, 255, 255)
    print('clear')
    
    # Setting line color.
    print('color', 0, 0, 0)
    
    # Drawing title.
    print('text', '"', 'HISTOGRAM FOR ASSIGNMENT', assignment_number + 1, 'GRADE DISTRIBUTION', '"', 225, 50)
    
    # Drawing x-axis and label.
    print('line', 130, 470, 625, 470)
    print('text', '"', 'GRADES', '"', 350, 550)
    
    # Simultaneous double loop to draw x-axis tick marks and scale labels.
    for i, j in zip(range(130, 626, 45), range(12)):
        print('line', i, 470, i, 490)
        if j <= 10:
            print('text', '"', j, '"', (i + 12), 510)
    
    # Drawing y-axis and label.
    print('line', 130, 130, 130, 470)  
    y_axis_text = 'FREQUENCY'
    for character, i in zip(y_axis_text, range(250, 360, 12)):
        print('text', '"', character, '"', 40, i)    
    
    # Calculating the maximum value for the y-axis.
    if max(bin_list[assignment_number]) // 10 >= 10:
        y_max = ((max(bin_list[assignment_number]) // 10) + 2) * 10
    elif max(bin_list[assignment_number]) // 10 < 10:
        y_max = ((max(bin_list[assignment_number]) // 10) + 1) * 10
    elif max(bin_list[assignment_number]) // 10 < 1:
        y_max = 10
    
    # Drawing y-axis tick marks and dynamic scale labels.
    y_tick_frequency = int(y_max / 10)
    for k, l in zip(range(470, 129, -34), range(0, y_max + 1, y_tick_frequency)):    
        print('line', 110, k, 130, k)
        print('text', '"', l, '"', 80, (k + 4))

    # Drawing bin bars.
    for bins, m in zip(bin_list[assignment_number], range(130, 626, 45)):
        print('color', 255, 0, 255, int(255*(bins / max(bin_list[assignment_number]))))
        print('fillrect', m, 470 - ((bins / y_max) * 340 ), 45, (bins / y_max) * 340)


def statistics(grades_list, assignment_number):
    '''Function that calculates statistics for a given assignment by extracting
       data from a previously created grades_list and prints the statistics
       in Quickdraw.'''
    # Creating the assignment_grades list.
    assignment_grades = []
    for i in range(1, len(grades_list)-1):
        assignment_grades.append(grades_list[i][assignment_number + 5])
    
    # Finding the max and min.
    max_grade = max(assignment_grades)
    min_grade = min(assignment_grades)

    # Calculating the average.
    average = sum(assignment_grades)/(len(assignment_grades))

    # Calculating the median.
    assignment_grades.sort()
    if len(grades_list) % 2 == 0:
        median = (assignment_grades[len(assignment_grades)//2] + assignment_grades[len(assignment_grades)//2 +1]) / 2
    else:
        median = assignment_grades[(len(assignment_grades)//2) +1]

    # Calculating the standard deviation.
    standard_deviation_list = []
    for j in range(len(assignment_grades)):
        standard_deviation_list.append((assignment_grades[j] - average)**2)
    standard_deviation = ((sum(standard_deviation_list))/len(standard_deviation_list))**(1/2)

    # Printing the statistics.
    print('color', 0, 0 ,0)
    print('text', '"', 'STATISTICS:', '"', 660, 80)
    print('text', '"', 'Max:', "%.1f" %max_grade, '"', 660, 100)
    print('text', '"', 'Min:', "%.1f" %min_grade, '"', 660, 118)
    print('text', '"', 'Avg:', "%.2f" %average, '"', 660, 136)
    print('text', '"', 'Med:', "%.2f" %median, '"', 660, 154)
    print('text', '"', 'Standard','"', 660, 172)
    print('text', '"', 'Deviation:', "%.2f" %standard_deviation, '"', 660, 184)
        

def main():
    grades_list = create_grades_list(file)
    draw_graph(create_bins_list(grades_list), assignment_to_graph)
    statistics(grades_list, assignment_to_graph)

# =============================  /FUNCTIONS  ==================================


    
# ===============================  PROGRAM  ===================================

main()

# ==============================  /PROGRAM  ===================================
