# TESTING DIRECTORY #
Tests parts of the system to make sure they are in working order

## Usage ##
Run the test script to run all tests
```
python test.py
```

## Writing Tests ##
Make tests with `*.py` files  
Tests are evaluated with print statements - Simple diff matching of program and expected output  
Newlines are ignored
Add expected outputs right after the corresponding print statements with special indicators:   
```
''':-   
output  
'''  
```

If printing needs to be done and that is not meant to be compared to output, add `:-` at the beginning of the line
