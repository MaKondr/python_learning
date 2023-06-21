class Animal:

    def __init__(self, environment=None):
        self._environment = environment

    def info_animal(self):
        return self._environment


class Dog(Animal):

    def __init__(self,*, say=None, color=None, names=None):
        super().__init__()
        self._say = say
        self._color = color
        self._name = names

    def do_say(self):
        print(self._say)

    def get_name(self):
        return self._name

    def info_animal(self):
        return {'name': self._name,
                'how_say': self._say,
                'color': self._color}


if '__main__' == __name__:
    print('Ты чего наделал?!')
