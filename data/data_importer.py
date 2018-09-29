class Data_Importer:
    def __init__(self,name=None):
        self.name = name

    def set_name(self,name=None):
        self.name = name

    def search(self):
        pass

    def error(self):
        def no_name():
            print("No name given to search for")
        return {
            no_name
        }