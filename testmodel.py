#!/usr/bin/python3
if __name__ == '__main__':
    from models.base_model import BaseModel

    instance = BaseModel()
    print(instance)

    print(instance.__init__(name="Californai"))
