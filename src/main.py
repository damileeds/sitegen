from textnode import TextNode, TextType
from htmlnode import HTMLNode
def main():
    testing = TextNode("Hi World",TextType.NORMAL)
    print(testing)

    testing2 = HTMLNode("a tag","a value","a child",{"href": "https://www.google.com"})
    print(testing2)

main()


