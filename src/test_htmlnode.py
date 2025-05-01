import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("a tag","a value","a child",{"href": "https://www.google.com"})
        node2 = HTMLNode("a tag","a value","a child",{"href": "https://www.google.com"})
        self.assertEqual(node, node2)
    def test_eq2(self):
        node = HTMLNode("a tag","a value",None,{"href": "https://www.google.com"})
        node2 = HTMLNode("a tag","a value",None,{"href": "https://www.google.com"})
        self.assertEqual(node, node2)
    def test_not_eq2(self):
        node = HTMLNode("a tag","a value","a child",{"href": "https://www.google.com"})
        node2 = HTMLNode("a tag","a value","a parent",{"href": "https://www.google.com"})
        self.assertNotEqual(node, node2)
    def test_not_eq3(self):
        node = HTMLNode("a tag","a value","a child",{"href": "https://www.google.com"})
        node2 = HTMLNode("a tag","a value","a child",)
        self.assertNotEqual(node, node2)
    def test_eq3(self):
        node = HTMLNode("a tag","a value","a child",{"href": "https://www.google.com","target": "_blank",})
        self.assertEqual(node.props_to_html(),' href="https://www.google.com" target="_blank"')

if __name__ == "__main__":
    unittest.main()