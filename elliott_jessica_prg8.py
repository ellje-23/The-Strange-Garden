'''
Programmer: Jess Elliott

Description: This program modifies image files.    

Input: User inputs include the name of an input PPM image and what modifications
       the user would like to make to the file. 

Output: The program outputs a PPM file with the modifications made to the input
        PPM file.
'''

# This function reads in the first 3 lines of the infile and writes those 3 lines
# out to the outfile
# Parameters: infile, fileObject that you're reading from
#             outfile, fileObject that you're writing to
# Returns: None
def process_header(infile, outfile):
    # Writing line 1 to the outfile 
    line1 = infile.readline()
    outfile.write(line1)
    
    # Writing line 2 to the outfile
    line2 = infile.readline()
    outfile.write(line2)

    # Writing line 3 to the outfile
    line3 = infile.readline()
    outfile.write(line3)

# This function reads in the body of a PPM file, one line at a time
# Parameters: infile, fileObject that you're reading from
#             outfile, fileObject that you're writing to
#             modification, a string explaining which modifications the user wants
# Returns: None
def process_body(infile, outfile, modification):
    # Loop over the infile object 1 line at a time
    for line in infile:
        line = line.rstrip()
        # Splitting the line into a list of strings
        vals = line.split(' ')
        # Looping over the list of strings and adding them to the appropriate list
        red = []
        green = []
        blue = []
        for v in range(0, len(vals), 3):
            v = vals[v]
            red.append(v)
        for v in range(1, len(vals), 3):
            v = vals[v]
            green.append(v)
        for v in range(2, len(vals), 3):
            v = vals[v]
            blue.append(v)                   
        # Calling the appropriate modification functions
        mod = int(modification)
        if mod == 1:
            red = negate(red)   
        elif mod == 2:
            blue = negate(blue)
        elif mod == 3:
            green = negate(green)          
        elif mod == 4:
            red = negate(red)
            blue = negate(blue)
            green = negate(green)
        elif mod == 5:
            red = flatten(red)
        elif mod == 6:
            blue = flatten(blue)   
        elif mod == 7:
            green = flatten(green)  
        elif mod == 8:
            red = flip_horizontal(red)
            green = flip_horizontal(green)
            blue = flip_horizontal(blue)   
        else: 
            red, green, blue = grey_scale(red, green, blue)
        # Putting together the red, green, and blue values into a new string
        newS = '' 
        for i in range(len(red)): 
            newS += str(red[i]) + ' ' + str(green[i]) + ' ' + str(blue[i])
            newS += '\n'

    # Writing the new string to the output file
        outfile.write(newS)

# This function takes in a list and negates each value in the list
# Parameters: lst, a 1-D list of integers
# Returns: negLst, a list with the modified values (negatives of the original values)
def negate(lst):
    # Creating a list to add the modified values to 
    negLst = []
    # Running through the values in lst and negating them 
    for val in lst:
        negVal = int(val) - 255
        if negVal < 0:
            negVal *= -1
        negLst.append(negVal)

    return negLst

# This function takes in a list and flattens each value in the list
# Parameters: lst, a 1-D list of integers
# Returns: flattenLst, a list of the same length as (lst) with all zeros
def flatten(lst):
    # Creating a list to add the modified values to 
    flattenLst = []
    # Running through the values in lst and flattening them
    for val in lst:
        val = 0
        flattenLst.append(val)
        
    return flattenLst

# This function takes in three 1-D lists, and returns 3 lists that contain the average 
# of the original values at each index
# Parameters: red; green; and blue, 3 1-D lists with the same number of elements in them
# Returns: red; green; and blue, as updated lists
def grey_scale(red, green, blue):    
    # Running through the number of elements
    # (since they have the same number, I used just used the length of red)   
    for n in range(len(red)):
        # Calculating the average of the elements 
        average = (int(red[n]) + int(green[n]) + int(blue[n])) // 3
        red[n] = average
        green[n] = average
        blue[n] = average 
        
    return red, green, blue

# This function takes in a list and reverses the order of the list
# Parameters: lst, a 1-D list of integers
# Returns: revLst, the original list in reverse order
def flip_horizontal(lst):
    #Creating a copy of the original list
    revLst = lst[:]
    #Reversing the list 
    revLst.reverse()

    return revLst

# This function takes in a filename and modification and outputs the correct
# output file name with my last and first name
# Parameters: filename, a string that includes a 3 character extension
#             mod, a string referencing the selected menu option
# Returns: outputFileName, a string with the correct output filename
def makeOutputFileName(filename, mod):
    outputFileName = ''
    # Getting and adding the original filename without '.ppm'
    originalFileName = filename.split('.ppm')
    outputFileName += originalFileName[0]
    # Adding my last and first name
    programmerName = '_elliott_jess_'
    outputFileName += programmerName
    # Adding the modification to the image
    mod = int(mod)
    if mod == 1:
        outputFileName += 'negate_red'
    elif mod == 2:
        outputFileName += 'negate_blue'
    elif mod == 3:
        outputFileName += 'negate_green'
    elif mod == 4:
        outputFileName += 'negate_all'
    elif mod == 5:
        outputFileName += 'remove_red'
    elif mod == 6:
        outputFileName += 'remove_blue'
    elif mod == 7:
        outputFileName += 'remove_green'
    elif mod == 8:
        outputFileName += 'flip_horizontally'
    else: 
        outputFileName += 'grey_scale'
    # Adding the PPM format 
    outputFileName += '.ppm'
    
    return outputFileName
    
def main():

    # Getting input from the user
    inputFileName = input("What file would you like to modify? ")
    print("Here are the options for modifications: \n\
          (1) Negate red \n\
          (2) Negate blue\n\
          (3) Negate green\n\
          (4) Negate all\n\
          (5) Remove red\n\
          (6) Remove blue\n\
          (7) Remove green\n\
          (8) Flip horizontally\n\
          (9) Grey scale\n")

    mod = int(input("What modification would you like to do? "))
    #Validating user input)
    while mod < 1 or mod > 9:
        print("Error: Please enter a valid option")
        mod = int(input("What modification would you like to do? "))
            
    # Opening the file 
    infile = open(inputFileName, 'r')

    # Getting the correct output file name, and opening the file in write mode
    outputFileName = makeOutputFileName(inputFileName, mod)
    outfile = open(outputFileName, 'w')

    # Processing the entire file
    process_header(infile, outfile)
    process_body(infile, outfile, mod)

    # Closing both files, and lets user know what the updated file is called
    infile.close()
    outfile.close()
    print("Your modified file has been created. It is called", outputFileName)

main()
