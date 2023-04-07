# Context Managerii = sunt niste obiecte care ne ajuta sa controlam accesul la anumite resurse


# pentru a implementa un context manager, o clasa trebuie sa implementeze __enter__ si __exit__
class FileManager:
    def __init__(self, filename, access_mode):
        self.filename = filename
        self.access_mode = access_mode
        self.file = None

    def __enter__(self):
        # deschidem si accessam resursele
        self.file = open(self.filename, self.access_mode)
        return self.file

    def __exit__(self, type, value, traceback):
        # eliberarea resurselor
        self.file.close()


with FileManager("my_first_file.txt", "r") as f:
    print(f.read())

    from contextlib import contextmanager


    @contextmanager
    def file_manager(filename, mode):
        f = open(filename, mode)
        yield f
        f.close()


    with file_manager("my_first_file.txt", "r") as f:
        print(f.read())