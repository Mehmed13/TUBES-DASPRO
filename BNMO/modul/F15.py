import argparse, os

def load():
    parser = argparse.ArgumentParser()
    parser.add_argument("foldername",type=str)
    try:
        args = parser.parse_args()
    except:
        print("Tidak ada nama folder yang diberikan!")
    
    if checkFolder(args.foldername):
        return args.foldername
    else:
        return ""

def checkFolder(folderName): # membuat function check folder
    for root in os.walk(folderName): # mengecek list folder yang ada di dalam "folderName"
        if (root[0] == folderName): # Jika root index 0 (nama folder) sama dengan "folderName"
    	    return True
    return False

