class DBRouter(object):
    # we list model names
    lite = {'toDoListItems', 'savedLocations'}
    my = {'cvModel'}

    # for reading operations we check model name and redirect it to its database
    def db_for_read(self, model, **hints):
        if model.__name__ in self.lite:
            return 'sqlite'
        elif model.__name__ in self.my:
            return 'mysql'
        return None

    # the same is done for writing operations
    def db_for_write(self, model, **hints):
        if model.__name__ in self.lite:
            return 'sqlite'
        elif model.__name__ in self.my:
            return 'mysql'
        return None
