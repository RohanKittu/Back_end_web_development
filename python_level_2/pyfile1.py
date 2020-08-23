def hello():
    print("\n entered into hello function in file one")
print("outside the function block")
if __name__ == "main":
    print("run file one main")
    hello()
else:
    print("file one got imported")
    