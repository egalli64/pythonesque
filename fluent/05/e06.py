"""
Fluent Python (Second Edition) by Luciano Ramalho
https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/

Original code: https://github.com/fluentpython/example-code-2e/
My playground: https://github.com/egalli64/pythonesque/ fluent folder

@dataclass __post_init__: useful for validation and computing field values based on other fields
"""
from dataclasses import dataclass
from e05 import ClubMember


@dataclass
class HackerClubMember(ClubMember):
    all_handles = set()  # class attribute
    handle: str = ""

    def __post_init__(self):
        # assign a value to handle
        if self.handle == "":
            self.handle = self.name.split()[0]

        # handle validation
        cls = self.__class__

        if self.handle in cls.all_handles:
            msg = f"handle {self.handle!r} already exists."
            raise ValueError(msg)

        cls.all_handles.add(self.handle)


tom = HackerClubMember("Tom")
print(tom)

bob = HackerClubMember("Bob")
print(bob)

try:
    tom_bob = HackerClubMember("Tom Bob")
    print(tom_bob)
except ValueError as e:
    print(f"{e!r}")
