def add(a,b):
    return a + b

# if __name__ == "__main__" function

# can not import runs only when the main function calls
# use for testing purpose 
# if imported to some files functions under this functions does not run
if __name__ == "__main__":
    print("Testing addition module")
    print(add(2,3))

    def hi():
        print("ds")