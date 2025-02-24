FILE_PATH_ABS = r'F:\!PracaInf\Python\ToDoApp\todos.txt'
FILE_PATH_REL = 'todos.txt'


def list_elements(input_list):
    for i, item in enumerate(input_list):
        print(f'{i + 1}. {item.strip("\n")}.')


def read_file(filename=FILE_PATH_REL):
    """
    Reads the text file and returns the list of
    to-do items.
    :param filename: path to file to read from
    :return: list of to-do items
    """
    # context manager
    with open(filename, 'r') as file:
        todos_local = file.readlines()
    return todos_local
    # new_todos = [item.strip('\n') for item in todos]


def write_file(content, filename=FILE_PATH_REL):
    """Writes to-do item list in the text file"""
    with open(filename, 'w') as file:
        file.writelines(content)


if __name__ == "__main__":
    print("Hello from functions.py!")
