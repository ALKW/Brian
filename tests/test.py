# Test script that executes every test file in the directory and prints if all tests pass and if tests fail
#! /usr/bin/env python
import os.path
from subprocess import call
import sys
sys.path.insert(0, os.getcwd() + "/..")
import brain.settings as bs

# Ensure no printing is done by the system and only the print statements in the test script are executed
bs.PRINT = False

def parse_and_build_exp(filename):
    global exp_filename

    in_file = open(filename, "r+")
    next_line_is_exp = False
    
    # Go line by line in the test file looking for comments with the special symbol
    with open(exp_filename, "w+") as fout:
        for line in in_file.readlines():
            # If we are currently parsing expected output 
            # and reach the end of the comment we are done
            if next_line_is_exp and "'''" in line:
                next_line_is_exp = False
            # Otherwise add the line to the expected result file
            elif next_line_is_exp:
                fout.write(line)
            # Indicates the start of expected response lines
            elif "''':-" in line:
                next_line_is_exp = True

    in_file.close()

def execute_tests():
    global failed_tests
    global failed
    global exp_filename 
    global res_filename 

    # Cycle through each .py file in the directory
    for filename in os.listdir(os.getcwd()):
        # If the file is not a python file, it is not a test file
        if ".py" not in filename or "test.py" == filename:
            continue
        else:
            # Parse the file and build an expected outputs file
            parse_and_build_exp(filename)
            
            # Execute the program and pipe the output to a test file
            result = call(["python",filename], stdout=open(res_filename, "w+"))

            # If the result is non-zero then the program failed
            if result != 0:
                print("Error was recieved in trying to execute test program:", filename)

            # Compare the expected result with the actual result
            if not same_contents(exp_filename, res_filename):
                failed = True
                failed_tests.append(filename)
    
    #remove the two temporary files
    os.remove(os.path.join(os.getcwd(), res_filename))
    os.remove(os.path.join(os.getcwd(), exp_filename))

# Compare files, ignoring newlines
def same_contents(exp_filename, res_filename):
    f1 = open(exp_filename, "r+")
    f2 = open(res_filename, "r+")

    # Read in the lines from each file and build it into one long string
    # stripped of trailing/leading whitespace on each line
    f1_lines = f1.readlines()
    f2_lines = f2.readlines()

    # Close the files as they are no longer needed
    f1.close()
    f2.close()

    # Convert to one long string
    f1_data = ""
    for line in f1_lines:
        f1_data += line.strip()

    # Convert to one long string
    f2_data = ""
    for line in f2_lines:
        # Ignore lines with special starting as they are not to be compared
        if ":-" in line:
            continue
        else:
            f2_data += line.strip()

    if f1_data != f2_data:
        return False
    return True


if __name__ == '__main__':
    exp_filename = "temp_exp_result.txt"
    res_filename = "temp_test_result.txt"
    failed = False
    failed_tests = []

    execute_tests()

    if failed:
        print("####### FAILED #######\n")
        print("Failed Tests:")
        for failed_test in failed_tests:
            print(failed_test)
    else:
        print("####### PASSED #######")


