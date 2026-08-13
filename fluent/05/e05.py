"""
Fluent Python (Second Edition) by Luciano Ramalho
https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/

Original code: https://github.com/fluentpython/example-code-2e/
My playground: https://github.com/egalli64/pythonesque/ fluent folder

@dataclass Field Options
"""
from dataclasses import dataclass, field

try:
    @dataclass
    class ClubMemberBug:
        name: str
        guests: list = []  # Mutable default [] is not allowed. Use default_factory
except ValueError as e:
    print(f"{e!r}")


@dataclass
class ClubMemberClassic:
    name: str
    guests: list = field(default_factory=list)


x = ClubMemberClassic("x")
print("a dataclass object w/ default list", x)
y = ClubMemberClassic("y")

print("different guests in the two objects:", x.guests is not y.guests)


@dataclass
class ClubMember:
    name: str
    # notice the Python 3.9 notation for parameterized generic type
    guests: list[str] = field(default_factory=list)
