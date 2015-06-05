from HTMLParser import HTMLParser

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    props = {
        "h1": {
            "span": {
                "class" : {
                    "itemprop": "titre",
                    "title-extra": "titre original"
                }
            },
            "a": "date",
        },
        "div": {
            "time": {
                "itemprop": {
                    "duration": "duree"
                }
            }
        },
        "strong": {
            "span": {
                "itemprop": {
                    "ratingValue": "notation"
                }
            }
        }
    }
    container = ""
    label = ""
    data = {}
    tag = ""

    find = False

    def handle_starttag(self, tag, attrs):
        if tag in self.props.keys():
            self.container = tag

        if self.container != "":
            if tag in self.props[self.container]:
                if isinstance(self.props[self.container][tag], str):
                    self.find = True
                    self.label = self.props[self.container][tag]
                else:
                    for attr in attrs:
                        if attr[0] in self.props[self.container][tag].keys():
                            if attr[1] in self.props[self.container][tag][attr[0]].keys():
                                self.find = True
                                self.label = self.props[self.container][tag][attr[0]][attr[1]]
                                break
                            else:
                                self.find = False
                        else:
                            self.find = False
            else:
                self.find = False
        else:
            self.find = False


    def handle_endtag(self, tag):
        if tag == self.container:
            self.container = ""

    def handle_data(self, data):
        if self.label == "date":
            if self.label not in self.data.keys():
                self.data[self.label] = data.strip()
        else:
            if self.find and data.strip() != "":
                self.data[self.label] = data.strip()

