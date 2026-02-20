# Custom Module (do this in file_reader.py):
# Implement a function read_data(file_path) that reads the content from data.txt, parses it, and returns a list of tuples containing names and ages. e..g [("Alice", 30), ("Fiona", 28), ...]

def read_data(file_path):
    with open(file_path,"r") as file:
        lines = file.readlines()
        print(lines)



read_data("PYTHON/data.txt")