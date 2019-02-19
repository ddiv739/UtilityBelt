import os
import argparse



#Recursively iterates folders until it reaches children (leaves) and 
#returns the name/ filepath of each child
def recurseFolder(inputDir):
    for obj in os.listdir(inputDir):
        #If folder recurse, if not - termination condition and return
        if(os.path.isdir(inputDir + '/' + obj)):
            recurseFolder(inputDir + '/' + obj)
        
        print(obj)

if __name__ == "__main__":
    recurseFolder(os.getcwd())