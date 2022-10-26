class Html:
    def __init__(self, image, input, text, link):
        self.image = image
        self.input = input
        self.text = text
        self.link = link

    def __str__(self):
        return "<img {} > <input {} > <p>{}</p> <link {}>" \
            .format(self.image, self.input, self.text, self.link)


def tag(image, input, text, link):
    return Html(image, input, text, link)


def alt_tag(image, input, text, link):
    return Html(image, input, text, link)


if __name__ == "__main__":
    new_tag = tag("bmp", "456", "text", "http")
    one_more_tag = alt_tag("jpeg", "789", "text1", "https")
    print(new_tag, one_more_tag)
   