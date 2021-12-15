# 구현 가능한 OOP 만들기 - 노트북
# - Note를 정리하는 프로그램
# - 사용자는 Note에 뭔가를 적을 수 있다.
# - Note에는 Content가 있고, 내용을 제거할 수 있다.
# - 두개의노트북을합쳐하나로만들수있다.
# - Note는 Notebook에 삽입된다.
# - Notebook은 Note가 삽일 될 때 페이지를 생성하며, 최고 300페이지까지 저장 가능하다
# - 300 페이지가 넘으면 더 이상 노트를 삽입하지 못한다.

# class Notebook
# method add_note remove_note get_number_of_pages
# variable title page_number notes

# class Note
# method write_content remove_all
# variable content


class Note(object):
    def __init__(self, content = None):
        self.content = content
    
    def write_content(self, content : str):
        self.content = content

    def remove_all(self):
        self.content = ''

    def __add__(self, other):
        return self.content + other.content

    def __str__(self):
        # return "content : {0}".format(self.content)
        return self.content

class Notebook(object):
    def __init__(self, title):
        self.title = title
        self.page_number = 1
        self.notes = {}

    def add_note(self, note, page = -1):
        if self.page_number < 301:
            if page == -1:
                self.notes[self.page_number] = note
                self.page_number += 1
            else:
                self.notes[page] = note
        else:
            print("페이지가 모두 채워졌습니다.")
    
    def remove_note(self, page_number):
        if page_number in self.notes.keys():
            return self.notes.pop()
        else:
            print("해당 페이지는 존재하지 않습니다.")

    def get_number_of_page(self):
        return len(self.notes.keys())

    

my_notebook = Notebook("This is Notebook")
note1 = Note("note 1")
note2 = Note("note 2")
note3 = Note("note 3")
my_notebook.add_note(note1)
my_notebook.add_note(note2)
my_notebook.add_note(note3, 100)
my_notebook.notes[4] = "hello"
# print(my_notebook.notes[4])
# print(my_notebook.notes[100])
for i in my_notebook.notes:
    print(i, my_notebook.notes[i])
