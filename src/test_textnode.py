import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    def test_not_eq(self):
        node = TextNode("Image of a dog",TextType.IMAGE,"http://www.cutedog.com")
        node2 = TextNode("Image of a dog",TextType.LINK,"http://www.cutedog.com")
        self.assertNotEqual(node,node2)
    def test_eq2(self):
        node = TextNode("Green Apples", TextType.ITALIC)
        node2 = TextNode("Green Apples", TextType.ITALIC)
        self.assertEqual(node, node2)
    def test_not_eq2(self):
        node = TextNode("Image of a dog",TextType.IMAGE,"http://www.cutecat.com")
        node2 = TextNode("Image of a dog",TextType.IMAGE,"http://www.cutedog.com")
        self.assertNotEqual(node,node2)
    def test_not_eq3(self):
        node = TextNode("Image of a dog",TextType.LINK,"http://www.cutecat.com")
        node2 = TextNode("Image of a dog",TextType.LINK,)
        self.assertNotEqual(node,node2)
    def test_not_eq4(self):
        node = TextNode("Image of a dog",TextType.CODE)
        node2 = TextNode("Image of a cat",TextType.CODE)
        self.assertNotEqual(node,node2)
    def test_raise_error(self):
        
        with self.assertRaises(AttributeError):
            node = TextNode("Image of a dog",TextType.DOG)

if __name__ == "__main__":
    unittest.main()