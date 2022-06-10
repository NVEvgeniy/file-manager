

from creating_folder import creating

def test_creating_folder():
    assert creating(question) == os.mkdir(folder)


# def creating(question):
#     folder = input(question)
#     os.mkdir(folder)
#
#
# creating('Введите название папки: ')