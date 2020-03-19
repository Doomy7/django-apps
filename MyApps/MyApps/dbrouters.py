class DBRouter(object):
    lite = {'toDoListItems', 'savedLocations'}
    my = {'cvModel'}

    def db_for_read(self, model, **hints):
        if model.__name__ in self.lite:
            return 'sqlite'
        elif model.__name__ in self.my:
            return 'mysql'
        return None

    def db_for_write(self, model, **hints):
        if model.__name__ in self.lite:
            return 'sqlite'
        elif model.__name__ in self.my:
            return 'mysql'
        return None
