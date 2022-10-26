from enum import Enum


class TagType(Enum):
    Op1 = 0,
    Op2 = 1


class Tag:
    def __init__(self, image, inp, text, link):
        self.image = image
        self.inp = inp
        self.text = text
        self.link = link

    def get_tag(self):
        return self.image, self.inp, self.text, self.link


class Op1(Tag):
    def __init__(self, image, inp, text, link):
        super().__init__(image, inp, text, link)


class Op2(Tag):
    def __init__(self, image, inp, text, link):
        super().__init__(image, inp, text, link)


def create_tag(tag: TagType) -> Tag:
    factory_dict = {
        TagType.Op1: Op1,
        TagType.Op2: Op2
    }
    return factory_dict[tag]("<int {} >", "<input {} >", "<p>{}</p>", "<link {}>")


if __name__ == "__main__":
    for t in TagType:
        new_tag = create_tag(t)
        print(f"tag: {t}", f"one: {new_tag.get_tag()}")
