"""
Fluent Python (Second Edition) by Luciano Ramalho
https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/

Original code: https://github.com/fluentpython/example-code-2e/
My playground: https://github.com/egalli64/pythonesque/ fluent folder

Initialization Variables That Are Not Fields: InitVar
"""
from dataclasses import dataclass, InitVar


class DatabaseType:
    """mock a database type"""

    def __init__(self, name: str):
        self.name = name
        self.value = len(name)

    def lookup(self, key: str) -> int:
        return self.value * len(key)


@dataclass
class C:
    i: int
    j: int | None = None
    # database is not a field, just an init-only variable
    database: InitVar[DatabaseType | None] = None

    def __post_init__(self, database: DatabaseType | None):
        if self.j and database:
            print(f"i is {self.i} j is {self.j}, database is {database}")

        if self.j is None and database is not None:
            self.j = database.lookup("j")


my_database = DatabaseType("a_database")

c = C(10, database=my_database)
print(c)
