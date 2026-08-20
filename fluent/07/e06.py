"""
Fluent Python (Second Edition) by Luciano Ramalho
https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/

Original code: https://github.com/fluentpython/example-code-2e/
My playground: https://github.com/egalli64/pythonesque/ fluent folder

A function with * and ** arguments
"""


def tag(name, *content, class_=None, **attrs):
    """
    Generate one or more HTML tags

    :param name: the name of the tag
    :param content: a list of strings
    :param class_: the class of the tag
    :param attrs: the attributes of the tag

    :return: the HTML tag
    """
    if class_ is not None:
        # by default, no class attribute
        attrs["class"] = class_

    attr_pairs = (f" {attr}='{value}'" for attr, value in sorted(attrs.items()))
    attr_str = "".join(attr_pairs)
    if content:
        elements = (f"<{name}{attr_str}>{c}</{name}>" for c in content)
        return "\n".join(elements)
    else:
        # XML-style for empty tag
        return f"<{name}{attr_str} />"


print("an empty tag:", tag("br"))
print("a plain p tag:", tag("p", "hello"))
print("when more content values are passed, more tags are created:")
print(tag("p", "hello", "world"))
print("extra kwargs are captured by **attrs", tag("p", "hello", id=33))
print("passing _class sidebar as explicit kwarg:")
print(tag("p", "hello", "world", class_="sidebar"))
print("possibly using kwarg is more clear:", tag(name="img", content="testing"))
my_tag = {"name": "img", "title": "Sunset Boulevard", "src": "sunset.jpg", "class": "framed"}
print("maybe you prefer passing just a dict", tag(**my_tag))
