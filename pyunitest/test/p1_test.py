import unittest
from pyunitest.p1 import Person as PersonClass
class POneTest(unittest.TestCase):
    person = PersonClass()
    user_id = []
    user_name = []
    def test_set_name(self):
        for i in range(4):
            name = 'name' + str(i)
            self.user_name.append(name)
            user_id = self.person.set_name(name)
            self.assertIsNotNone(user_id) # empty user id first
            self.user_id.append(user_id)
        print("finish test case")

    def test_get_name(self):
        length = len(self.user_id)
        for i in range(6):
            if i < length:
                self.assertEqual(self.user_name[i],
                                 self.person.get_name(self.user_id[i]))
            else:
                self.assertEqual('There is no such user', self.person.get_name(i))

if __name__ == "__main__":
    unittest.main()
