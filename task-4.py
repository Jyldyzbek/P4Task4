class List():
    def __init__(self, names_):
        self.all_contacts = names_

    def search_by_name(self, names):
        self.names = names
        z = [a for a in self.names if a in self.all_contacts]
        return z

class ContactList(List):
    pass

list_ = ['JZ', 'BGZ', 'ISI', 'AZA']
my_list = ['JZ', 'ISI', 'FARY']

ss = ContactList(my_list)
dd = List(my_list)
print(ss.search_by_name(list_))
    
