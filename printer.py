class Printer:

    @staticmethod
    def print_to_terminal(text):
        f = open("output", "a")
        f.write(text+"\n")
        f.close()

    @staticmethod
    def clean_file():
        open("output", "w").close()