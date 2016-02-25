# -*- encoding utf-8 -*-
"""
HOMEWORK PRECHECKER

* last update 2016-02-17-1450: typo's
* update 2016-02-17-0846: cleaned up comments and code
                               added usage message
                               
The prechecker exists to check that we can successfully read and process 
a file to be subnitted for your homework.

The prechecker can be run either:
(A) From within python.
        -1) make sure the directory (folder) holding this file is on the 
            python path:
                import sys # to import the sys module
                sys.path   # is the list of directories search for imports
                # if the directory containing precheck.py is not listed:
                sys.path.append('<full path of directory to search>')
         0) from precheck import precheck  # loads the precheck function to python
         
         Finally you can simply run the command
                    precheck('your homework filename.py')

 or
 (B) From the command line:  
         python </path/to/precheck/precheck.py> 'your homework filename.py'
  
precheck prints messages to the standard output.

In detail, it:

(1) attempts to open and read the file
(2) prints the modification date of the file
(3) 'Parses' the file -- trying to interpret it as a python program
(4) checks the toplevel statements in the program and removes things
    like print statements, input statements, and expressions that are not
    saved in a variable.  Note that this does not remove print or input 
    statements that are inside function definitions
(5) 'Compiles' the edited version of the program to produce a corresponding 'code'
     object.  This can fail if there are syntax or other errors in the program.
(6) Executes the code in a local namespace (a dictionary object).  This can also
    cause errors.
(7) After execution, precheck prints out the local dictionary containing all of
    the new names of objects created by exec'ing the code.  These include the
    student information your provided (check it) and also all of the functions
    that you defined.  This list of objects should make sense to you!


When you run precheck from within a python environment, the return value is the
local dictionary.  You can use this to access the compiled version of your
functions.  The homework grader does this.

"""


#%%  Imports 

import os
import sys
import copy
import ast
import time
        
#%% The code below checks a program represented as an 
#   'Abstract Syntax Tree' (AST) to identify nodes at the top (module) level 
#    that the prechecker needs to remove before it can be executed by the 
#    autograder.  Typically these involve calls to input or print that 
#    would be executed during the loading process.
        
def check_eval_node(node):
    """This function checks an AST node that might be evaluated from top level.
    Returns bool true or false indicating whether not it is good as is.
    Second return value is a 'reason' string.
    Checks: no toplevel EXPR's allowed
          : no toplevel calls to input or print
          : no toplevel assignments that involve input"""
    result=True; # default is that the node is OK
    reason=""  ; # default reason is empty string
    # start by checking common node types that lead to evaluation during loading
    if isinstance(node,ast.Expr):  # no exprs (free standing procedure calls)
        result=False
        reason="(line {:d}: Toplevel Expr)".format(node.lineno) # includes line number
    elif isinstance(node,ast.Call):  # examine toplevel calls
        if isinstance(node.func,ast.Name):
            if node.func.id in ("input","print"): # is the function input or print?
                result=False
                reason="(line {:d}: call to {} detected)".format(node.lineno, node.func.id)
        for a in node.args:  
            # also check the arguments
            argresult, argreason = check_eval_node(a) # recursive call on each function argument
            result = result and argresult    # result is false if *any* argument is bad
            if not argresult:
                reason = reason + argreason  # if the current argument was bad, append its 'reason'
    elif isinstance(node,ast.Assign):  # for assignment node, check value
        result,reason=check_eval_node(node.value)
    return result,reason
        
        
#%% This function does direct surgery on an AST to check for and remove
#   problematic top level statements

def fixup_ast(module):
    """remove toplevel statements that do not pass the check.
    returns: (new AST, list of strings with lineno/reason for removal)"""
    if isinstance(module,ast.Module): # verify that the node is a module (ie top level)
        result=copy.deepcopy(module)  # make a full copy of the node
        new_body=[]                   # a possible replacement for the module body (list of top nodes)
        removed=[]                    # list of top level nodes removed
        for item in module.body:      # loop over all the top level nodes in body
            check,reason=check_eval_node(item)  # check the current node and get its the reason string
            if check:
                new_body.append(item) # if the item is ok, add to the new version of the list
            else:
                removed.append(reason)# else add to the removed list
        result.body=new_body          # replace the node body
        ast.fix_missing_locations(result)  # tool to 'fix' the line numbers for all the nodes
        return result,removed         # return the new AST and also the list of removed nodes
    else:
        raise Exception('fixup_ast called with non-module',module) # only if node was not a module!
    

#%% main action for precheck
def precheck(filename):
    """attempts to load, parse, compile, and execute filename
    prints progress messages and issues along the way.
    Returns a local dictionary created by executing the program.
    
    Note: The keywords in the local dictionary are the names of objects defined in the file
    such as the student information variables and the functions defined there.
    The values associated for each keyword is the actual value (or code for functions)
    of the corresponding object.  So after successfully running precheck and saving the return value
    you have access to the program elements!
    """
    
    print("Reading",filename, end='...')
    with open(filename) as f:  # read the text from the file
        text=f.read()
    print("success")
    mtime=time.localtime(os.path.getmtime(filename))  # read the modification timestamp of the file
    print('     Modified {:d}-{:02d}-{:02d}-{:02d}:{:02d}:{:02d}'.format(mtime.tm_year,mtime.tm_mon,
         mtime.tm_mday,mtime.tm_hour,mtime.tm_min,mtime.tm_sec))
    print("Parsing", end='...')
    f_ast=ast.parse(text,filename,'exec')  # parse the file to an AST
    print("success")
    print("Checking top level expressions",end='...')  # try to fixuo the AST 
    fixed_ast,reasons=fixup_ast(f_ast)
    if reasons:
        print('some changes made:')  # printout reasons for if there were changes
        for item in reasons:
            print("==>",item)
    else:
        print('no changes needed')
    print("Compiling code",end='...')
    code=compile(fixed_ast,'ast-'+filename,'exec') # compile the AST to a code object
    print("Success")
    print('executing code',end='...')   
    g=dict()   # a new dictionary to hold the global namespace for loading the code
    l=dict()   # a new dictionary as the local namespace for the loaded code
    exec(code,g,l)    # actually execute the code object
    print("Success")
    print("Objects defined in the source code:")
    for k,v in l.items(): 
        print('{:>20s}= {}'.format(k,v))  # list the contents of the local namespace
    return l   # return the contents of the local namespace


#%% Make runnable from python

if __name__=='__main__':
    if len(sys.argv)>1:
        precheck(sys.argv[1])
    else:
        print("Usage: python precheck.py <filename.py>)")
        

    

