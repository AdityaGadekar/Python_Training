from jinja2 import Template
name = input("Enter name  ")
tm = Template("Hello {{ name }}")
msg = tm.render(name=name)
print(msg)

name ="Jogy"
age = 25
tm = Template("My name is {{name}} and I am {{age}}")
msg = tm.render(name=name, age=age)
print(msg)