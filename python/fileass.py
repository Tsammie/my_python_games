# Create a Package and Module:
# Create a package named data_processing.
# Inside data_processing, create two modules:
# file_reader.py for reading and processing data from a file.
# web_fetcher.py for fetching additional information from a web API.

# File Handling
# Create a text file named data.txt with the following content:
# Alice,30
# Fiona,28
# Jasmine,31
# George,33
# Bob,25
# Ella,22
# Hannah,27
# Daniel,40
# Isaac,29
# Charlie,35


# with open('data.txt','r') as files:
    # sam = files.read()
    # print(sam)

# with open('data.txt','w') as files:
#     sam = files.write("I love you")
#     print(sam)

# Custom Module (do this in file_reader.py):
# Implement a function read_data(file_path) that reads the content from data.txt, parses it, and returns a list of tuples containing names and ages. e..g [("Alice", 30), ("Fiona", 28), ...]

newlist=[]
def read_data(file_path): 
    with open(file_path,'r') as files:
        sam = files.readlines()
        for i in sam:
            you = i.repa
        # for x in you:
            newlist.append((i))
            print(newlist)

read_data(r"C:\Users\user\Documents\Sqi-lecture\python\data.txt")


