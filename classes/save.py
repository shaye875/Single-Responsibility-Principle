from book import *

class File(Book):
    def __init__(self,title,author,content,name_file):
        super().__init__(title,author,content)
        self.file_name = name_file

    def save_to_file(self):
        with open(self.file_name,"w") as file:
            file.write(self.content)
