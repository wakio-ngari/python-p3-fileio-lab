import os
def write_file(file_name, file_content):
    with open(f"{file_name}.txt", "w") as file:#writes content to txt,
        #if it already exists its overwritten
        file.write(file_content)
    
#adds content to a txt file if it doesn't exist
def append_file(file_name, append_content):
    with open(f"{file_name}.txt", "a") as file:
        file.write(append_content)

def read_file(file_name):
    if not os.path.exists(f"{file_name}.txt"):
        return "File not found."
    
    with open(f"{file_name}.txt", "r") as file:
        return file.read()

  
