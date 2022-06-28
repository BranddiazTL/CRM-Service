class Choice:
    def __init__(self, name, value=None, help_text=""):
        self.name = name
        self.value = value if value is not None else name
        self.help_text = help_text


class Choices:
    def __init__(self, *args, **kwargs):

        choices = []

        for choice in args:

            if isinstance(choice, list):
                choice = Choice(*choice)

            elif not isinstance(choice, Choice):
                choice = Choice(choice)

            choices.append(choice)

        for name, value in sorted(kwargs.items(), key=lambda item: item[1]):
            choices.append(Choice(name=name, value=value))

        for choice in choices:
            setattr(self, choice.name, choice.value)

        self.choice_objects = choices
        self.choices = tuple([(choice.name, choice.value)
                              for choice in choices])
        self.keys = [choice.name for choice in choices]
        self.values = [choice.value for choice in choices]
        self.description = [[choice.value, choice.help_text]
                            for choice in choices]

    def next(self, value):

        try:
            return self.values[self.values.index(value) + 1]

        except IndexError:
            return value

    def previous(self, value):

        try:
            return self.values[self.values.index(value) - 1]

        except IndexError:
            return value
