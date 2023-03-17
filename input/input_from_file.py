## using a built-in fucntion "open()" as below:
## open(filename, 'r') as variable_name:
    # <Do sth with the variable here>
 
####
def open_input(file):
    with open(file, 'r') as f:
        text = f.read()
        print(text)

def open_input(write_file):
    with open(write_file, 'w') as f:
        text = f.write("Append additional characters in this file from open() built-in fuction")
        print(text)

def main():
    open_input("file.txt")
    open_input("write_file.txt")

if __name__ == "__main__":
    main()