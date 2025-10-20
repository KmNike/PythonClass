"""
Group Members: []

Week_10_Exercise_II (10 Points)

Due Date: 
This assignment is due on Wednesday October 22th, 2025 @ 12:30pm (Along with last Wednesday's assigment!)

Directions: 
Please complete the below exercises. You must use, edit, and submit this python script directly for this assignment.

Collaboration: 
You must work in small groups (2-4 students) on this assignment!
Failure to do so will result in an automatic 15% penalty to your submission. 
Please indicate who worked on the assignment together at the top of this script and if you want any parts graded differently between group members in your submission, else all members will get the same grade.

Submission Details: 
Please submit 1 script per group. For members of the group who do not submit the script, there will be a text box available on the submission page. 
Please tell me who you worked with in the text box and I will assign the same grade to you and all other members of that group. 

Sources:
At the end of the script, in a comment block like this one, please include a list of any links to any webpages (stackoverflow, github, geeksforgeeks etc.) used for help completing the assignment.
"""
# The McGrath lab studies evolution of behavior using Lake Malawi cichlid fishes as our model system.
# Int the lake, some of these fish live over sand and perform complex courtship behaviors to attract mates
# Males will manipulate the sand on the lake bottoms (or in lab tank setups) to excavate large pits or build sand mounds called 'castles'.
# This behavior is called bower building. In the lab, we can quanify bower building by measuring changes in the sand surface using depth sensors.
# The provided daily_depth.npy file numpy file contains 7 depth readings, each representing a snapshot of the sand surface during bower building.
# In this exercise, you will use this array to practice basic numpy operations.

# Please install numpy and matplotlib with conda or pip if you don't already have these modules installed.
import numpy as np
import matplotlib.pyplot as plt
import pdb

def save_array_visualization(array, filename): # (0 points)
    # This function is provided to help you visualize any numpy arrays you create. 
    # Simply provide the array to visualize and the filename for the output visualization
    if not filename.endswith('.jpg'):
        filename = filename + '.jpg'
    plt.figure()
    plt.imshow(array, cmap='viridis', vmin=-5, vmax=5)
    plt.colorbar()
    plt.savefig(filename, format='jpg')
    plt.close()


# Q1: Loading arrays from the file (1 point)
# load the "daily_depth.npy" as an array
### Your Code Here ###
data = None #
# print(f"Q1: The first element in the loaded numpy array is:\n {data[0]}")
print("-"*50)


# Q2: What are some basic attributes of the array? (2 points)
# Print the following attributes for the array:
#   a) The shape
#   b) The size
#   c) The number of dimensions
#   d) The data type of the daily depth array. 
#   e) What do you think the three dimensions represent?
### Your Code Here ###
print(f"Q2: The shape of the numpy array is: \n {None}")
print(f"Q2: The size of the numpy array is: \n {None}")
print(f"Q2: The number of dimenstions in the numpy array is: \n {None}")
print(f"Q2: The type of data within the numpy array is: \n {None}")
print('Q2: The three dimensions represent: # Your answer here')
print("-"*50)


# Q3: Indexing Through the Array (1 point)
#     a) use array indexing to isolate the first depth frame and the last depth frame
#     b) subtract the first depth frame from the last depth frame element-wise to get the total depth change
#     c) use the save_array_visualization function to save the total depth change array as a jpg. Name the file "Q3.jpg"
#     d) Describe what the visualization shows you. What do the yellow and blue parts represent? What do the white parts represent?
# You will be graded here based on the accuracy of the Q3.jpg file generated for this question.
### Your Code Here ###
print("The various colors in the jpg image represent: # Your answer here")
print("-"*50)


# Q4: Aggregation Methods and NaN's (2 points)
#   a) What are the minimum and maximum values in the daily depth array
#   b) Now find the min and max values but excluding the nan in the np array
#   c) find the mean, median, standard deviation, and sum of the non-nan values in the array
#   d) find the depth change array from the previous section, determine the minimum and maximum depth changes
### Your Code Here ###
print(f"Q4: The minimin value from all the data in the np array is:\n {None}")
print(f"Q4: The maximum value from all the data in the np array is:\n {None}")
print(f"Q4: The minimin value without nans in the np array is:\n {None}")
print(f"Q4: The maximum value without nans in the np array is:\n {None}")
print(f"Q4: The mean value, excluding nans in the np array is:\n {None}")
print(f"Q4: The median value, excluding nans in the np array is:\n {None}")
print(f"Q4: The standard deviation of the non-nan data in the np array is:\n {None}")
print(f"Q4: The sum of the non-nan values in the np array is:\n {None}")
print(f"Q4: The minimum depth change from the change array is :\n {None}")
print(f"Q4: The minimum depth change from the change array is :\n {None}")
print("-"*50)


# Q5: Creating and Using Boolean Arrays (1 points)
### Your Code Here ###
#   a) Create a boolean mask the same size as the daily depth array that is True wherever the original array contains a nan value and False wherever it contains a non-nan value
#   b) Use this array to determine the total number of nan values
#   c) invert the boolean array so that it is True wherever the daily depth array is non-Nana and False wherever it is Nan
#   d) use the inverted mask and the original array to find the sum of non-nan values in the daily depth array without using the nansum built-in. Confirm it matches your previous result from Q4. If the values match, your answer is correct.
### Your Code Here ###
mask = None
inv_mask = None
print(f"Q5: Using the mask array, the number of nan values is:\n {None}")
print(f"Q5: Using the inverted mask and the original np array, the sum of non-nan values is:\n {None}")


# Q6 (challenge): (3 points)
# In as few lines of code as possible, find the depth change between each successive frame and save a visualization.
# You already did this between thr first and last day. 
# Now, repeat but find the depth change between the first and second day and save it to a file, find the depth change between the second and third day and save it to a file, etc. 
# Save each file as "ChangeX.jpg" e.g. Change1.jpg, Change2.jpg, ... etc.
### Your Code Here ###