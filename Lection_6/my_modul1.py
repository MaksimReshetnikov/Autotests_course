number = 1
string = 'Hello'


def global_changes():
    global number
    global string
    number = 5
    string = 'Hello, dear friend'
    print("2", number)
    print("2", string)

global_changes()
print("3", number)
print("3", string)
