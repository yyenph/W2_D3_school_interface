class Person:
    def __init__(self,**kwargs):
        self.name=kwargs.get('name')
        self.age=kwargs.get('age')
        self.role=kwargs.get('role')
        self.id=kwargs.get('id')
        self.password=kwargs.get('password')




