#!/usr/bin/python3

class BaseModel:
    def __init__(self, id):
        self.id = id
    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
if __name__ == "__main__":
    my_obj = BaseModel(19)
    print(my_obj)
