import argparse
class Employee:
    def __init__(self, no_of_employee):
        self.no_of_employee = no_of_employee
        print("no of Employee", self.no_of_employee)
    def add(self, a, b):
        print(a+b)
    def mul(self, p, q):
        print(p*q)

if __name__ =='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('no_of_employee',
                        help="employee", type=int)
    parser.add_argument('a',
                        help="employee", type=int)
    parser.add_argument('b',
                        help="employee", type=int)
    parser.add_argument('p',
                        help="employee", type=int)
    parser.add_argument('q',
                        help="employee", type=int)
    args = parser.parse_args()
    g = Employee(args.no_of_employee)
    g.add(args.a, args.b)
    g.mul(args.p, args.q)