class Person:

    name = []

    def set_name(self, user_name):
        self.name.append(user_name)
        return len(self.name) - 1
    def get_name(self, user_id):
        if user_id >= len(self.name):
            return 'There is no such user'
        else:
            return self.name[user_id]
if __name__ == "__main__":
    person = Person()
    print("User andre is been added with id", person.set_name('andre'))
    print("User is associated with id 0 is", person.get_name(0))
