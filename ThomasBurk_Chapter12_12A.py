# Chapter 12 Assignment A
# 11/24/2024
# Thomas Burk

# CSV Analysis using Numpy: utilize numpy to analyze student grades stored
#   in a CSV file. You will perform various statistical calculations and
#   operations to gain insights into the dataset.

import csv
import numpy as np

def main():
    # Open npgrades.csv into numpy array, set data type to floating point
    with open('npgrades.csv', 'r') as f:
        g = list(csv.reader(f, delimiter=','))
    g = np.array(g[1:], dtype=float) 

    print (g[:3])
    
    exam1(g)
    exam2(g)
    exam3(g)
    all_exams(g)
    ex_pass(g)

def exam1(g):
    # Mean, median, standard deviation, minimum, and maximum for first column
    ex1_mean = np.mean(g[:,0])
    print ("The average (mean) score for Exam 1 is",ex1_mean)

    ex1_med = np.median(g[:,0])
    print ("The median score for Exam 1 is",ex1_med)

    ex1_std = np.std(g[:,0])
    print ("The standard deviation for Exam 1 is",ex1_std)

    ex1_min = np.min(g[:,0])
    print ("The minimum score for Exam 1 is",ex1_min)

    ex1_max = np.max(g[:,0])
    print ("The maximum score for Exam 1 is",ex1_max,"\n")

def exam2(g):
    # Mean, median, standard deviation, minimum, and maximum for second column
    ex2_mean = np.mean(g[:,1])
    print ("The average (mean) score for Exam 2 is",ex2_mean)

    ex2_med = np.median(g[:,1])
    print ("The median score for Exam 2 is",ex2_med)

    ex2_std = np.std(g[:,1])
    print ("The standard deviation for Exam 2 is",ex2_std)

    ex2_min = np.min(g[:,1])
    print ("The minimum score for Exam 2 is",ex2_min)

    ex2_max = np.max(g[:,1])
    print ("The maximum score for Exam 2 is",ex2_max,"\n")

def exam3(g):
    # Mean, median, standard deviation, minimum, and maximum for third column
    ex3_mean = np.mean(g[:,2])
    print ("The average (mean) score for Exam 3 is",ex3_mean)

    ex3_med = np.median(g[:,2])
    print ("The median score for Exam 3 is",ex3_med)

    ex3_std = np.std(g[:,2])
    print ("The standard deviation for Exam 3 is",ex3_std)

    ex3_min = np.min(g[:,2])
    print ("The minimum score for Exam 3 is",ex3_min)

    ex3_max = np.max(g[:,2])
    print ("The maximum score for Exam 3 is",ex3_max,"\n")

def all_exams(g):
    # Mean, median, standard deviation, minimum, and maximum for entire array
    all_mean = np.mean(g)
    print ("The average (mean) score for all exams is",all_mean)

    all_med = np.median(g)
    print ("The median score for all exams is",all_med)

    all_std = np.std(g)
    print ("The standard deviation for all exams is",all_std)

    all_min = np.min(g)
    print ("The minimum score for all exams is",all_min)

    all_max = np.max(g)
    print ("The maximum score for all exams is",all_max,"\n")

def ex_pass(g):
    # Add number of each element that has a value greater or equal to 60 for
    #   each column
    ex1_pass = np.array(g[:,0] >= 60, dtype=int)
    ex1_pass_sum = np.sum(ex1_pass)
    print ("Number of students who passed Exam 1:",ex1_pass_sum)

    ex2_pass = np.array(g[:,1] >= 60, dtype=int)
    ex2_pass_sum = np.sum(ex2_pass)
    print ("Number of students who passed Exam 2:",ex2_pass_sum)

    ex3_pass = np.array(g[:,2] >= 60, dtype=int)
    ex3_pass_sum = np.sum(ex3_pass)
    print ("Number of students who passed Exam 3:",ex3_pass_sum)

    # Add number of each element that has a value greater or equal to 60 for
    #   entire array. Divide by 30 to get pass percentage for all exams together
    all_pass = np.array(g >= 60, dtype=int)
    all_pass_sum = np.sum(all_pass)
    print ("The pass percentage for all exams is",((all_pass_sum/30)*100),"percent.")

main()
