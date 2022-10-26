class HTml:
    def release(self):
        pass


class Image(HTml):
    def __init__(self):
        print("<img>")


class Input(HTml):
    def __init__(self):
        print("<input type=" ">")


class Text(HTml):
    def __init__(self):
        print("<p> </p>")


class Link(HTml):
    def __init__(self):
        print("<a> </a>")


class Create:
    def create(self) -> HTml:
        pass


class CrImage(Create):
    def create(self):
        return Image()


class CrInput(Create):
    def create(self):
        return Input()


class CrText(Create):
    def create(self):
        return Text()


class CrLink(Create):
    def create(self):
        return Link()


if __name__ == "__main__":
    creator = CrImage()
    img = creator.create()

    creator = CrInput()
    inp = creator.create()

    creator = CrText()
    text = creator.create()

    creator = CrLink()
    link = creator.create()

    img.release()
    inp.release()
    text.release()
    link.release()
