class Image():
    def __init__(self, img):
        self.img = img

    def get(self):
        return "<int {} >".format(self.img)


class Input():
    def __init__(self, inp):
        self.inp = inp

    def get(self):
        return "<input {} >".format(self.inp)


class Text():
    def __init__(self, text):
        self.text = text

    def get(self):
        return "<p>{}</p>".format(self.text)


class Link():
    def __init__(self, link):
        self.link = link

    def get(self):
        return "<link {}>".format(self.link)


img1 = Image("src=img_girl.jpg")
inp1 = Input("type=text")
text1 = Text("This is some text in a paragraph.")
lint1 = Link("rel=stylesheet")

tag = [img1, inp1, text1, lint1]
for t in tag:
    print(t.get())
   