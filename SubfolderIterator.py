import os
import argparse


# construct the argument parse and parse the arguments. nargs means 0 or 1 with ?. const is fallback in case of 0 i.e no arg entered
ap = argparse.ArgumentParser()
ap.add_argument("-g", "--git", required=False, nargs="?", const=False,
	help="ignore git folders. True by default")
#Make an accumulator if you only want certain file types!
args = vars(ap.parse_args())


#Recursively iterates folders until it reaches children (leaves) and 
#returns the name/ filepath of each child
def recurseFolder(inputDir):
    for obj in os.listdir(inputDir):
        #If folder recurse, if not - termination condition and return
        objlocation = inputDir + "\\" + obj
        if(os.path.isdir(objlocation)):
            if(obj == ".git"):
                continue
            recurseFolder(objlocation)
        else :
            #Return the object location
            print(objlocation)
            pass

if __name__ == "__main__":
    recurseFolder(os.getcwd())