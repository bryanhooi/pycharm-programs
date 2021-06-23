# NAME          : BRYAN HOOI YU ERN
# EMAIL         : hooibryan@gmail.com
# DATE EDITED   : 23/06/2021

"""
Run using `python -m unittest local_test_suite`.
"""

from typing import Any, List
import unittest
from dataclasses import dataclass

from qualifier import make_table


@dataclass
class TableParams:
    rows: List[List[Any]]
    labels: List[Any] = None
    centered: bool = False

    def __repr__(self):
        """Used for putting in a dict."""
        return f"{self.rows=}{self.labels=}{self.centered=}"


class MakeTableTests(unittest.TestCase):
    baked_solutions = {
        "self.rows=[['Apple', 5]]self.labels=Noneself.centered=False":
            '┌───────┬───┐\n'
            '│ Apple │ 5 │\n'
            '└───────┴───┘',
        "self.rows=[['Apple', 5], ['Banana', 3], ['Cherry', 7]]self.labels=Noneself.centered=False":
            '┌────────┬───┐\n'
            '│ Apple  │ 5 │\n'
            '│ Banana │ 3 │\n'
            '│ Cherry │ 7 │\n'
            '└────────┴───┘',
        "self.rows=[['Apple', 5], ['Banana', 3], ['Cherry', 7], ['Kiwi', 4], ['Strawberry', 6]]self.labels=Noneself.centered=False":
            '┌────────────┬───┐\n'
            '│ Apple      │ 5 │\n'
            '│ Banana     │ 3 │\n'
            '│ Cherry     │ 7 │\n'
            '│ Kiwi       │ 4 │\n'
            '│ Strawberry │ 6 │\n'
            '└────────────┴───┘',
        "self.rows=[['Apple', 5, 70]]self.labels=Noneself.centered=False":
            '┌───────┬───┬────┐\n'
            '│ Apple │ 5 │ 70 │\n'
            '└───────┴───┴────┘',
        "self.rows=[['Apple', 5, 70, 'Red'], ['Banana', 3, 5, 'Yellow'], ['Cherry', 7, 31, 'Red']]self.labels=Noneself.centered=False":
            '┌────────┬───┬────┬────────┐\n'
            '│ Apple  │ 5 │ 70 │ Red    │\n'
            '│ Banana │ 3 │ 5  │ Yellow │\n'
            '│ Cherry │ 7 │ 31 │ Red    │\n'
            '└────────┴───┴────┴────────┘',
        "self.rows=[['Apple', 5, 70, 'Red', 76], ['Banana', 3, 5, 'Yellow', 8], ['Cherry', 7, 31, 'Red', 92], ['Kiwi', 4, 102, 'Green', 1], ['Strawberry', 6, 134, 'Red', 28]]self.labels=Noneself.centered=False":
            '┌────────────┬───┬─────┬────────┬────┐\n'
            '│ Apple      │ 5 │ 70  │ Red    │ 76 │\n'
            '│ Banana     │ 3 │ 5   │ Yellow │ 8  │\n'
            '│ Cherry     │ 7 │ 31  │ Red    │ 92 │\n'
            '│ Kiwi       │ 4 │ 102 │ Green  │ 1  │\n'
            '│ Strawberry │ 6 │ 134 │ Red    │ 28 │\n'
            '└────────────┴───┴─────┴────────┴────┘',
        "self.rows=[['Apple', 5, 70]]self.labels=['Fruit', 'Tastiness', 'Sweetness']self.centered=False":
            '┌───────┬───────────┬───────────┐\n'
            '│ Fruit │ Tastiness │ Sweetness │\n'
            '├───────┼───────────┼───────────┤\n'
            '│ Apple │ 5         │ 70        │\n'
            '└───────┴───────────┴───────────┘',
        "self.rows=[['Apple', 5, 70, 'Red'], ['Banana', 3, 5, 'Yellow'], ['Cherry', 7, 31, 'Red']]self.labels=['Fruit', 'Tastiness', 'Sweetness', 'Colour']self.centered=False":
            '┌────────┬───────────┬───────────┬────────┐\n'
            '│ Fruit  │ Tastiness │ Sweetness │ Colour │\n'
            '├────────┼───────────┼───────────┼────────┤\n'
            '│ Apple  │ 5         │ 70        │ Red    │\n'
            '│ Banana │ 3         │ 5         │ Yellow │\n'
            '│ Cherry │ 7         │ 31        │ Red    │\n'
            '└────────┴───────────┴───────────┴────────┘',
        "self.rows=[['Apple', 5, 70, 'Red', 76], ['Banana', 3, 5, 'Yellow', 8], ['Cherry', 7, 31, 'Red', 92], ['Kiwi', 4, 102, 'Green', 1], ['Strawberry', 6, 134, 'Red', 28]]self.labels=['Fruit', 'Tastiness', 'Sweetness', 'Colour', 'Smell']self.centered=False":
            '┌────────────┬───────────┬───────────┬────────┬───────┐\n'
            '│ Fruit      │ Tastiness │ Sweetness │ Colour │ Smell │\n'
            '├────────────┼───────────┼───────────┼────────┼───────┤\n'
            '│ Apple      │ 5         │ 70        │ Red    │ 76    │\n'
            '│ Banana     │ 3         │ 5         │ Yellow │ 8     │\n'
            '│ Cherry     │ 7         │ 31        │ Red    │ 92    │\n'
            '│ Kiwi       │ 4         │ 102       │ Green  │ 1     │\n'
            '│ Strawberry │ 6         │ 134       │ Red    │ 28    │\n'
            '└────────────┴───────────┴───────────┴────────┴───────┘',
        "self.rows=[['Apple', 5, 70]]self.labels=['Fruit', 'Tastiness', 'Sweetness']self.centered=True":(
            '┌───────┬───────────┬───────────┐\n'
            '│ Fruit │ Tastiness │ Sweetness │\n'
            '├───────┼───────────┼───────────┤\n'
            '│ Apple │     5     │    70     │\n'
            '└───────┴───────────┴───────────┘',
            '┌───────┬───────────┬───────────┐\n'
            '│ Fruit │ Tastiness │ Sweetness │\n'
            '├───────┼───────────┼───────────┤\n'
            '│ Apple │     5     │     70    │\n'
            '└───────┴───────────┴───────────┘',
        ),
        "self.rows=[['Apple', 5, 70, 'Red'], ['Banana', 3, 5, 'Yellow'], ['Cherry', 7, 31, 'Red']]self.labels=['Fruit', 'Tastiness', 'Sweetness', 'Colour']self.centered=True": (
            '┌────────┬───────────┬───────────┬────────┐\n'
            '│ Fruit  │ Tastiness │ Sweetness │ Colour │\n'
            '├────────┼───────────┼───────────┼────────┤\n'
            '│ Apple  │     5     │    70     │  Red   │\n'
            '│ Banana │     3     │     5     │ Yellow │\n'
            '│ Cherry │     7     │    31     │  Red   │\n'
            '└────────┴───────────┴───────────┴────────┘',
            '┌────────┬───────────┬───────────┬────────┐\n'
            '│ Fruit  │ Tastiness │ Sweetness │ Colour │\n'
            '├────────┼───────────┼───────────┼────────┤\n'
            '│ Apple  │     5     │     70    │  Red   │\n'
            '│ Banana │     3     │     5     │ Yellow │\n'
            '│ Cherry │     7     │     31    │  Red   │\n'
            '└────────┴───────────┴───────────┴────────┘'

        ),
        "self.rows=[['Apple', 5, 70, 'Red', 76], ['Banana', 3, 5, 'Yellow', 8], ['Cherry', 7, 31, 'Red', 92], ['Kiwi', 4, 102, 'Green', 1], ['Strawberry', 6, 134, 'Red', 28]]self.labels=['Fruit', 'Tastiness', 'Sweetness', 'Colour', 'Smell']self.centered=True": (
            '┌────────────┬───────────┬───────────┬────────┬───────┐\n'
            '│   Fruit    │ Tastiness │ Sweetness │ Colour │ Smell │\n'
            '├────────────┼───────────┼───────────┼────────┼───────┤\n'
            '│   Apple    │     5     │    70     │  Red   │  76   │\n'
            '│   Banana   │     3     │     5     │ Yellow │   8   │\n'
            '│   Cherry   │     7     │    31     │  Red   │  92   │\n'
            '│    Kiwi    │     4     │    102    │ Green  │   1   │\n'
            '│ Strawberry │     6     │    134    │  Red   │  28   │\n'
            '└────────────┴───────────┴───────────┴────────┴───────┘',
            '┌────────────┬───────────┬───────────┬────────┬───────┐\n'
            '│   Fruit    │ Tastiness │ Sweetness │ Colour │ Smell │\n'
            '├────────────┼───────────┼───────────┼────────┼───────┤\n'
            '│   Apple    │     5     │     70    │  Red   │   76  │\n'
            '│   Banana   │     3     │     5     │ Yellow │   8   │\n'
            '│   Cherry   │     7     │     31    │  Red   │   92  │\n'
            '│    Kiwi    │     4     │    102    │ Green  │   1   │\n'
            '│ Strawberry │     6     │    134    │  Red   │   28  │\n'
            '└────────────┴───────────┴───────────┴────────┴───────┘'

        ),
        "self.rows=[['Pneumonoultramicroscopicsilicovolcanoconiosis'], ['Hippopotomonstrosesquippedaliophobia'], ['Supercalifragilisticexpialidocious'], ['Pseudopseudohypoparathyroidism'], ['Floccinaucinihilipilification'], ['Antidisestablishmentarianism'], ['.']]self.labels=['My Favourite Long Words']self.centered=True": (
            '┌───────────────────────────────────────────────┐\n'
            '│            My Favourite Long Words            │\n'
            '├───────────────────────────────────────────────┤\n'
            '│ Pneumonoultramicroscopicsilicovolcanoconiosis │\n'
            '│     Hippopotomonstrosesquippedaliophobia      │\n'
            '│      Supercalifragilisticexpialidocious       │\n'
            '│        Pseudopseudohypoparathyroidism         │\n'
            '│         Floccinaucinihilipilification         │\n'
            '│         Antidisestablishmentarianism          │\n'
            '│                       .                       │\n'
            '└───────────────────────────────────────────────┘',
            '┌───────────────────────────────────────────────┐\n'
            '│            My Favourite Long Words            │\n'
            '├───────────────────────────────────────────────┤\n'
            '│ Pneumonoultramicroscopicsilicovolcanoconiosis │\n'
            '│      Hippopotomonstrosesquippedaliophobia     │\n'
            '│       Supercalifragilisticexpialidocious      │\n'
            '│         Pseudopseudohypoparathyroidism        │\n'
            '│         Floccinaucinihilipilification         │\n'
            '│          Antidisestablishmentarianism         │\n'
            '│                       .                       │\n'
            '└───────────────────────────────────────────────┘'
        ),

        "self.rows=[['Pneumonoultramicroscopicsilicovolcanoconiosis'], ['Hippopotomonstrosesquippedaliophobia'], ['Supercalifragilisticexpialidocious'], ['Pseudopseudohypoparathyroidism'], ['Floccinaucinihilipilification'], ['Antidisestablishmentarianism'], ['.']]self.labels=['My Favourite Long Words']self.centered=False":
            '┌───────────────────────────────────────────────┐\n'
            '│ My Favourite Long Words                       │\n'
            '├───────────────────────────────────────────────┤\n'
            '│ Pneumonoultramicroscopicsilicovolcanoconiosis │\n'
            '│ Hippopotomonstrosesquippedaliophobia          │\n'
            '│ Supercalifragilisticexpialidocious            │\n'
            '│ Pseudopseudohypoparathyroidism                │\n'
            '│ Floccinaucinihilipilification                 │\n'
            '│ Antidisestablishmentarianism                  │\n'
            '│ .                                             │\n'
            '└───────────────────────────────────────────────┘',
        "self.rows=[['A'], ['B'], ['C'], ['D'], ['E'], ['F'], ['Pneumonoultramicroscopicsilicovolcanoconiosis']]self.labels=['Alphabet']self.centered=True":(
            '┌───────────────────────────────────────────────┐\n'
            '│                   Alphabet                    │\n'
            '├───────────────────────────────────────────────┤\n'
            '│                       A                       │\n'
            '│                       B                       │\n'
            '│                       C                       │\n'
            '│                       D                       │\n'
            '│                       E                       │\n'
            '│                       F                       │\n'
            '│ Pneumonoultramicroscopicsilicovolcanoconiosis │\n'
            '└───────────────────────────────────────────────┘',
            '┌───────────────────────────────────────────────┐\n'
            '│                    Alphabet                   │\n'
            '├───────────────────────────────────────────────┤\n'
            '│                       A                       │\n'
            '│                       B                       │\n'
            '│                       C                       │\n'
            '│                       D                       │\n'
            '│                       E                       │\n'
            '│                       F                       │\n'
            '│ Pneumonoultramicroscopicsilicovolcanoconiosis │\n'
            '└───────────────────────────────────────────────┘'
        ),
        "self.rows=[['A'], ['B'], ['C'], ['D'], ['E'], ['F'], ['Pneumonoultramicroscopicsilicovolcanoconiosis']]self.labels=['Alphabet']self.centered=False":
            '┌───────────────────────────────────────────────┐\n'
            '│ Alphabet                                      │\n'
            '├───────────────────────────────────────────────┤\n'
            '│ A                                             │\n'
            '│ B                                             │\n'
            '│ C                                             │\n'
            '│ D                                             │\n'
            '│ E                                             │\n'
            '│ F                                             │\n'
            '│ Pneumonoultramicroscopicsilicovolcanoconiosis │\n'
            '└───────────────────────────────────────────────┘',
        "self.rows=[[None, 1, 2.5, None, 32j, '123']]self.labels=[3, None, 12, 'A', 12.6, 12j]self.centered=True": (
            '┌──────┬──────┬─────┬──────┬──────┬─────┐\n'
            '│  3   │ None │ 12  │  A   │ 12.6 │ 12j │\n'
            '├──────┼──────┼─────┼──────┼──────┼─────┤\n'
            '│ None │  1   │ 2.5 │ None │ 32j  │ 123 │\n'
            '└──────┴──────┴─────┴──────┴──────┴─────┘',
            '┌──────┬──────┬─────┬──────┬──────┬─────┐\n'
            '│  3   │ None │  12 │  A   │ 12.6 │ 12j │\n'
            '├──────┼──────┼─────┼──────┼──────┼─────┤\n'
            '│ None │  1   │ 2.5 │ None │ 32j  │ 123 │\n'
            '└──────┴──────┴─────┴──────┴──────┴─────┘'
        ),
        "self.rows=[[<Fruit Apple>, 5, 70]]self.labels=['Fruit', 'Tastiness', 'Sweetness']self.centered=True": (
            '┌───────┬───────────┬───────────┐\n'
            '│ Fruit │ Tastiness │ Sweetness │\n'
            '├───────┼───────────┼───────────┤\n'
            '│ Apple │     5     │    70     │\n'
            '└───────┴───────────┴───────────┘',
            '┌───────┬───────────┬───────────┐\n'
            '│ Fruit │ Tastiness │ Sweetness │\n'
            '├───────┼───────────┼───────────┤\n'
            '│ Apple │     5     │     70    │\n'
            '└───────┴───────────┴───────────┘'
        ),
        "self.rows=[[<Fruit Apple>, 5, 70, 'Red'], [<Fruit Banana>, 3, 5, 'Yellow'], [<Fruit Cherry>, 7, 31, 'Red']]self.labels=['Fruit', 'Tastiness', 'Sweetness', 'Colour']self.centered=True": (
            '┌────────┬───────────┬───────────┬────────┐\n'
            '│ Fruit  │ Tastiness │ Sweetness │ Colour │\n'
            '├────────┼───────────┼───────────┼────────┤\n'
            '│ Apple  │     5     │    70     │  Red   │\n'
            '│ Banana │     3     │     5     │ Yellow │\n'
            '│ Cherry │     7     │    31     │  Red   │\n'
            '└────────┴───────────┴───────────┴────────┘',
            '┌────────┬───────────┬───────────┬────────┐\n'
            '│ Fruit  │ Tastiness │ Sweetness │ Colour │\n'
            '├────────┼───────────┼───────────┼────────┤\n'
            '│ Apple  │     5     │     70    │  Red   │\n'
            '│ Banana │     3     │     5     │ Yellow │\n'
            '│ Cherry │     7     │     31    │  Red   │\n'
            '└────────┴───────────┴───────────┴────────┘'
        ),
        "self.rows=[[<Fruit Apple>, 5, 70, 'Red', 76], [<Fruit Banana>, 3, 5, 'Yellow', 8], [<Fruit Cherry>, 7, 31, 'Red', 92], [<Fruit Kiwi>, 4, 102, 'Green', 1], [<Fruit Strawberry>, 6, 134, 'Red', 28]]self.labels=['Fruit', 'Tastiness', 'Sweetness', 'Colour', 'Smell']self.centered=True":(
            '┌────────────┬───────────┬───────────┬────────┬───────┐\n'
            '│   Fruit    │ Tastiness │ Sweetness │ Colour │ Smell │\n'
            '├────────────┼───────────┼───────────┼────────┼───────┤\n'
            '│   Apple    │     5     │    70     │  Red   │  76   │\n'
            '│   Banana   │     3     │     5     │ Yellow │   8   │\n'
            '│   Cherry   │     7     │    31     │  Red   │  92   │\n'
            '│    Kiwi    │     4     │    102    │ Green  │   1   │\n'
            '│ Strawberry │     6     │    134    │  Red   │  28   │\n'
            '└────────────┴───────────┴───────────┴────────┴───────┘',
            '┌────────────┬───────────┬───────────┬────────┬───────┐\n'
            '│   Fruit    │ Tastiness │ Sweetness │ Colour │ Smell │\n'
            '├────────────┼───────────┼───────────┼────────┼───────┤\n'
            '│   Apple    │     5     │     70    │  Red   │   76  │\n'
            '│   Banana   │     3     │     5     │ Yellow │   8   │\n'
            '│   Cherry   │     7     │     31    │  Red   │   92  │\n'
            '│    Kiwi    │     4     │    102    │ Green  │   1   │\n'
            '│ Strawberry │     6     │    134    │  Red   │   28  │\n'
            '└────────────┴───────────┴───────────┴────────┴───────┘'
        ),
        "self.rows=[['Just', 'Another', 'Row'], ['Just', 'Another', 'Row'], ['Just', 'Another', 'Row'], ['Just', 'Another', 'Row'], ['Just', 'Another', 'Row'], ['Just', 'Another', 'Row'], ['Just', 'Another', 'Row'], ['Just', 'Another', 'Row'], ['Just', 'Another', 'Row'], ['Just', 'Another', 'Row'], ['Just', 'Another', 'Row'], ['Just', 'Another', 'Row'], ['Just', 'Another', 'Row'], ['Just', 'Another', 'Row'], ['Just', 'Another', 'Row'], ['Just', 'Another', 'Row'], ['Just', 'Another', 'Row'], ['Just', 'Another', 'Row'], ['Just', 'Another', 'Row'], ['Just', 'Another', 'Row'], ['Just', 'Another', 'Row'], ['Just', 'Another', 'Row'], ['Just', 'Another', 'Row'], ['Just', 'Another', 'Row'], ['Just', 'Another', 'Row']]self.labels=Noneself.centered=False":
            '┌──────┬─────────┬─────┐\n'
            '│ Just │ Another │ Row │\n'
            '│ Just │ Another │ Row │\n'
            '│ Just │ Another │ Row │\n'
            '│ Just │ Another │ Row │\n'
            '│ Just │ Another │ Row │\n'
            '│ Just │ Another │ Row │\n'
            '│ Just │ Another │ Row │\n'
            '│ Just │ Another │ Row │\n'
            '│ Just │ Another │ Row │\n'
            '│ Just │ Another │ Row │\n'
            '│ Just │ Another │ Row │\n'
            '│ Just │ Another │ Row │\n'
            '│ Just │ Another │ Row │\n'
            '│ Just │ Another │ Row │\n'
            '│ Just │ Another │ Row │\n'
            '│ Just │ Another │ Row │\n'
            '│ Just │ Another │ Row │\n'
            '│ Just │ Another │ Row │\n'
            '│ Just │ Another │ Row │\n'
            '│ Just │ Another │ Row │\n'
            '│ Just │ Another │ Row │\n'
            '│ Just │ Another │ Row │\n'
            '│ Just │ Another │ Row │\n'
            '│ Just │ Another │ Row │\n'
            '│ Just │ Another │ Row │\n'
            '└──────┴─────────┴─────┘',
        "self.rows=[['Just', 'Another', 'Row'], ['Just', 'Another', 'Row'], ['Just', 'Another', 'Row'], ['Just', 'Another', 'Row'], ['Just', 'Another', 'Row'], ['Just', 'Another', 'Row'], ['Just', 'Another', 'Row'], ['Just', 'Another', 'Row'], ['Just', 'Another', 'Row'], ['Just', 'Another', 'Row'], ['Just', 'Another', 'Row'], ['Just', 'Another', 'Row'], ['Just', 'Another', 'Row'], ['Just', 'Another', 'Row'], ['Just', 'Another', 'Row'], ['Just', 'Another', 'Row'], ['Just', 'Another', 'Row'], ['Just', 'Another', 'Row'], ['Just', 'Another', 'Row'], ['Just', 'Another', 'Row'], ['Just', 'Another', 'Row'], ['Just', 'Another', 'Row'], ['Just', 'Another', 'Row'], ['Just', 'Another', 'Row'], ['Just', 'Another', 'Row']]self.labels=Noneself.centered=True": (
            '┌──────┬─────────┬─────┐\n'
            '│ Just │ Another │ Row │\n'
            '│ Just │ Another │ Row │\n'
            '│ Just │ Another │ Row │\n'
            '│ Just │ Another │ Row │\n'
            '│ Just │ Another │ Row │\n'
            '│ Just │ Another │ Row │\n'
            '│ Just │ Another │ Row │\n'
            '│ Just │ Another │ Row │\n'
            '│ Just │ Another │ Row │\n'
            '│ Just │ Another │ Row │\n'
            '│ Just │ Another │ Row │\n'
            '│ Just │ Another │ Row │\n'
            '│ Just │ Another │ Row │\n'
            '│ Just │ Another │ Row │\n'
            '│ Just │ Another │ Row │\n'
            '│ Just │ Another │ Row │\n'
            '│ Just │ Another │ Row │\n'
            '│ Just │ Another │ Row │\n'
            '│ Just │ Another │ Row │\n'
            '│ Just │ Another │ Row │\n'
            '│ Just │ Another │ Row │\n'
            '│ Just │ Another │ Row │\n'
            '│ Just │ Another │ Row │\n'
            '│ Just │ Another │ Row │\n'
            '│ Just │ Another │ Row │\n'
            '└──────┴─────────┴─────┘',
            '┌──────┬─────────┬─────┐\n'
            '│ Just │ Another │ Row │\n'
            '│ Just │ Another │ Row │\n'
            '│ Just │ Another │ Row │\n'
            '│ Just │ Another │ Row │\n'
            '│ Just │ Another │ Row │\n'
            '│ Just │ Another │ Row │\n'
            '│ Just │ Another │ Row │\n'
            '│ Just │ Another │ Row │\n'
            '│ Just │ Another │ Row │\n'
            '│ Just │ Another │ Row │\n'
            '│ Just │ Another │ Row │\n'
            '│ Just │ Another │ Row │\n'
            '│ Just │ Another │ Row │\n'
            '│ Just │ Another │ Row │\n'
            '│ Just │ Another │ Row │\n'
            '│ Just │ Another │ Row │\n'
            '│ Just │ Another │ Row │\n'
            '│ Just │ Another │ Row │\n'
            '│ Just │ Another │ Row │\n'
            '│ Just │ Another │ Row │\n'
            '│ Just │ Another │ Row │\n'
            '│ Just │ Another │ Row │\n'
            '│ Just │ Another │ Row │\n'
            '│ Just │ Another │ Row │\n'
            '│ Just │ Another │ Row │\n'
            '└──────┴─────────┴─────┘',
        ),
        "self.rows=[['Just', 'Another', 'Column', 'Just', 'Another', 'Column', 'Just', 'Another', 'Column', 'Just', 'Another', 'Column'], ['Just', 'Another', 'Column', 'Just', 'Another', 'Column', 'Just', 'Another', 'Column', 'Just', 'Another', 'Column'], ['Just', 'Another', 'Column', 'Just', 'Another', 'Column', 'Just', 'Another', 'Column', 'Just', 'Another', 'Column'], ['Just', 'Another', 'Column', 'Just', 'Another', 'Column', 'Just', 'Another', 'Column', 'Just', 'Another', 'Column'], ['Just', 'Another', 'Column', 'Just', 'Another', 'Column', 'Just', 'Another', 'Column', 'Just', 'Another', 'Column'], ['Just', 'Another', 'Column', 'Just', 'Another', 'Column', 'Just', 'Another', 'Column', 'Just', 'Another', 'Column'], ['Just', 'Another', 'Column', 'Just', 'Another', 'Column', 'Just', 'Another', 'Column', 'Just', 'Another', 'Column'], ['Just', 'Another', 'Column', 'Just', 'Another', 'Column', 'Just', 'Another', 'Column', 'Just', 'Another', 'Column'], ['Just', 'Another', 'Column', 'Just', 'Another', 'Column', 'Just', 'Another', 'Column', 'Just', 'Another', 'Column'], ['Just', 'Another', 'Column', 'Just', 'Another', 'Column', 'Just', 'Another', 'Column', 'Just', 'Another', 'Column'], ['Just', 'Another', 'Column', 'Just', 'Another', 'Column', 'Just', 'Another', 'Column', 'Just', 'Another', 'Column'], ['Just', 'Another', 'Column', 'Just', 'Another', 'Column', 'Just', 'Another', 'Column', 'Just', 'Another', 'Column'], ['Just', 'Another', 'Column', 'Just', 'Another', 'Column', 'Just', 'Another', 'Column', 'Just', 'Another', 'Column'], ['Just', 'Another', 'Column', 'Just', 'Another', 'Column', 'Just', 'Another', 'Column', 'Just', 'Another', 'Column'], ['Just', 'Another', 'Column', 'Just', 'Another', 'Column', 'Just', 'Another', 'Column', 'Just', 'Another', 'Column'], ['Just', 'Another', 'Column', 'Just', 'Another', 'Column', 'Just', 'Another', 'Column', 'Just', 'Another', 'Column'], ['Just', 'Another', 'Column', 'Just', 'Another', 'Column', 'Just', 'Another', 'Column', 'Just', 'Another', 'Column'], ['Just', 'Another', 'Column', 'Just', 'Another', 'Column', 'Just', 'Another', 'Column', 'Just', 'Another', 'Column'], ['Just', 'Another', 'Column', 'Just', 'Another', 'Column', 'Just', 'Another', 'Column', 'Just', 'Another', 'Column'], ['Just', 'Another', 'Column', 'Just', 'Another', 'Column', 'Just', 'Another', 'Column', 'Just', 'Another', 'Column'], ['Just', 'Another', 'Column', 'Just', 'Another', 'Column', 'Just', 'Another', 'Column', 'Just', 'Another', 'Column'], ['Just', 'Another', 'Column', 'Just', 'Another', 'Column', 'Just', 'Another', 'Column', 'Just', 'Another', 'Column'], ['Just', 'Another', 'Column', 'Just', 'Another', 'Column', 'Just', 'Another', 'Column', 'Just', 'Another', 'Column'], ['Just', 'Another', 'Column', 'Just', 'Another', 'Column', 'Just', 'Another', 'Column', 'Just', 'Another', 'Column'], ['Just', 'Another', 'Column', 'Just', 'Another', 'Column', 'Just', 'Another', 'Column', 'Just', 'Another', 'Column']]self.labels=Noneself.centered=False":
            '┌──────┬─────────┬────────┬──────┬─────────┬────────┬──────┬─────────┬────────┬──────┬─────────┬────────┐\n'
            '│ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │\n'
            '│ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │\n'
            '│ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │\n'
            '│ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │\n'
            '│ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │\n'
            '│ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │\n'
            '│ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │\n'
            '│ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │\n'
            '│ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │\n'
            '│ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │\n'
            '│ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │\n'
            '│ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │\n'
            '│ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │\n'
            '│ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │\n'
            '│ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │\n'
            '│ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │\n'
            '│ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │\n'
            '│ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │\n'
            '│ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │\n'
            '│ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │\n'
            '│ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │\n'
            '│ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │\n'
            '│ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │\n'
            '│ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │\n'
            '│ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │\n'
            '└──────┴─────────┴────────┴──────┴─────────┴────────┴──────┴─────────┴────────┴──────┴─────────┴────────┘',
        "self.rows=[['Just', 'Another', 'Column', 'Just', 'Another', 'Column', 'Just', 'Another', 'Column', 'Just', 'Another', 'Column'], ['Just', 'Another', 'Column', 'Just', 'Another', 'Column', 'Just', 'Another', 'Column', 'Just', 'Another', 'Column'], ['Just', 'Another', 'Column', 'Just', 'Another', 'Column', 'Just', 'Another', 'Column', 'Just', 'Another', 'Column'], ['Just', 'Another', 'Column', 'Just', 'Another', 'Column', 'Just', 'Another', 'Column', 'Just', 'Another', 'Column'], ['Just', 'Another', 'Column', 'Just', 'Another', 'Column', 'Just', 'Another', 'Column', 'Just', 'Another', 'Column'], ['Just', 'Another', 'Column', 'Just', 'Another', 'Column', 'Just', 'Another', 'Column', 'Just', 'Another', 'Column'], ['Just', 'Another', 'Column', 'Just', 'Another', 'Column', 'Just', 'Another', 'Column', 'Just', 'Another', 'Column'], ['Just', 'Another', 'Column', 'Just', 'Another', 'Column', 'Just', 'Another', 'Column', 'Just', 'Another', 'Column'], ['Just', 'Another', 'Column', 'Just', 'Another', 'Column', 'Just', 'Another', 'Column', 'Just', 'Another', 'Column'], ['Just', 'Another', 'Column', 'Just', 'Another', 'Column', 'Just', 'Another', 'Column', 'Just', 'Another', 'Column'], ['Just', 'Another', 'Column', 'Just', 'Another', 'Column', 'Just', 'Another', 'Column', 'Just', 'Another', 'Column'], ['Just', 'Another', 'Column', 'Just', 'Another', 'Column', 'Just', 'Another', 'Column', 'Just', 'Another', 'Column'], ['Just', 'Another', 'Column', 'Just', 'Another', 'Column', 'Just', 'Another', 'Column', 'Just', 'Another', 'Column'], ['Just', 'Another', 'Column', 'Just', 'Another', 'Column', 'Just', 'Another', 'Column', 'Just', 'Another', 'Column'], ['Just', 'Another', 'Column', 'Just', 'Another', 'Column', 'Just', 'Another', 'Column', 'Just', 'Another', 'Column'], ['Just', 'Another', 'Column', 'Just', 'Another', 'Column', 'Just', 'Another', 'Column', 'Just', 'Another', 'Column'], ['Just', 'Another', 'Column', 'Just', 'Another', 'Column', 'Just', 'Another', 'Column', 'Just', 'Another', 'Column'], ['Just', 'Another', 'Column', 'Just', 'Another', 'Column', 'Just', 'Another', 'Column', 'Just', 'Another', 'Column'], ['Just', 'Another', 'Column', 'Just', 'Another', 'Column', 'Just', 'Another', 'Column', 'Just', 'Another', 'Column'], ['Just', 'Another', 'Column', 'Just', 'Another', 'Column', 'Just', 'Another', 'Column', 'Just', 'Another', 'Column'], ['Just', 'Another', 'Column', 'Just', 'Another', 'Column', 'Just', 'Another', 'Column', 'Just', 'Another', 'Column'], ['Just', 'Another', 'Column', 'Just', 'Another', 'Column', 'Just', 'Another', 'Column', 'Just', 'Another', 'Column'], ['Just', 'Another', 'Column', 'Just', 'Another', 'Column', 'Just', 'Another', 'Column', 'Just', 'Another', 'Column'], ['Just', 'Another', 'Column', 'Just', 'Another', 'Column', 'Just', 'Another', 'Column', 'Just', 'Another', 'Column'], ['Just', 'Another', 'Column', 'Just', 'Another', 'Column', 'Just', 'Another', 'Column', 'Just', 'Another', 'Column']]self.labels=Noneself.centered=True": (
            '┌──────┬─────────┬────────┬──────┬─────────┬────────┬──────┬─────────┬────────┬──────┬─────────┬────────┐\n'
            '│ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │\n'
            '│ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │\n'
            '│ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │\n'
            '│ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │\n'
            '│ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │\n'
            '│ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │\n'
            '│ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │\n'
            '│ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │\n'
            '│ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │\n'
            '│ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │\n'
            '│ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │\n'
            '│ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │\n'
            '│ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │\n'
            '│ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │\n'
            '│ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │\n'
            '│ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │\n'
            '│ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │\n'
            '│ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │\n'
            '│ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │\n'
            '│ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │\n'
            '│ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │\n'
            '│ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │\n'
            '│ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │\n'
            '│ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │\n'
            '│ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │\n'
            '└──────┴─────────┴────────┴──────┴─────────┴────────┴──────┴─────────┴────────┴──────┴─────────┴────────┘',
            '┌──────┬─────────┬────────┬──────┬─────────┬────────┬──────┬─────────┬────────┬──────┬─────────┬────────┐\n'
            '│ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │\n'
            '│ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │\n'
            '│ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │\n'
            '│ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │\n'
            '│ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │\n'
            '│ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │\n'
            '│ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │\n'
            '│ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │\n'
            '│ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │\n'
            '│ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │\n'
            '│ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │\n'
            '│ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │\n'
            '│ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │\n'
            '│ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │\n'
            '│ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │\n'
            '│ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │\n'
            '│ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │\n'
            '│ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │\n'
            '│ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │\n'
            '│ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │\n'
            '│ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │\n'
            '│ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │\n'
            '│ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │\n'
            '│ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │\n'
            '│ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │ Just │ Another │ Column │\n'
            '└──────┴─────────┴────────┴──────┴─────────┴────────┴──────┴─────────┴────────┴──────┴─────────┴────────┘',
        )
    }
    last_char = None  # Done as class Var to ensure consistent across all test. (Unittest object recreates for each test)
    centering_strategy = None

    def run_against_solution(self, params: TableParams, fail_msg: str) -> None:
        """Run the user's result against the solution."""
        expected = MakeTableTests.baked_solutions.get(repr(params))
        result = make_table(**vars(params))

        if expected is None:
            raise RuntimeError("Couldn't find the known good result for this test.")

        if params.centered:
            if MakeTableTests.centering_strategy is None:
                f_string, center = expected
                if f_string == result:
                    MakeTableTests.centering_strategy = 0
                elif center == result:
                    MakeTableTests.centering_strategy = 1
                else:
                    raise AssertionError("Table does not meet our centering requirements.")
            expected = expected[MakeTableTests.centering_strategy]

        if MakeTableTests.last_char is None:  # Allows for ending with newline return
            MakeTableTests.last_char = "\n" if result[-1] == "\n" else ""

        self.assertEqual(result, expected + MakeTableTests.last_char, msg=fail_msg)

    def test_001_parameters(self) -> None:
        make_table(
            rows=[
                ["Apple", 5],
                ["Banana", 3],
                ["Cherry", 7],
            ],
        ),
        make_table(
            rows=[
                ["Apple", 5],
                ["Banana", 3],
                ["Cherry", 7],
            ],
            labels=["Fruit", "Tastiness"],
        ),
        make_table(
            rows=[
                ["Apple", 5],
                ["Banana", 3],
                ["Cherry", 7],
            ],
            labels=["Fruit", "Tastiness"],
            centered=True
        )

    def test_002_return_type(self) -> None:
        table = make_table(
            rows=[
                ["Apple", 5],
                ["Banana", 3],
                ["Cherry", 7],
            ],
        )
        self.assertIsInstance(table, str, msg="The return type from your solution does not seem to be a string.")

    def test_003_creates_rows(self) -> None:
        cases = (
            TableParams(rows=[
                ["Apple", 5],
            ]),
            TableParams(rows=[
                ["Apple", 5],
                ["Banana", 3],
                ["Cherry", 7],
            ]),
            TableParams(rows=[
                ["Apple", 5],
                ["Banana", 3],
                ["Cherry", 7],
                ["Kiwi", 4],
                ["Strawberry", 6]
            ])
        )

        for case in cases:
            self.run_against_solution(case, fail_msg="Failed when creating multiple rows.")

    def test_004_creates_cols(self) -> None:
        cases = (
            TableParams(rows=[
                ["Apple", 5, 70],
            ]),
            TableParams(rows=[
                ["Apple", 5, 70, "Red"],
                ["Banana", 3, 5, "Yellow"],
                ["Cherry", 7, 31, "Red"],
            ]),
            TableParams(rows=[
                ["Apple", 5, 70, "Red", 76],
                ["Banana", 3, 5, "Yellow", 8],
                ["Cherry", 7, 31, "Red", 92],
                ["Kiwi", 4, 102, "Green", 1],
                ["Strawberry", 6, 134, "Red", 28]
            ])
        )

        for case in cases:
            self.run_against_solution(case, fail_msg="Failed when creating multiple columns.")

    def test_005_creates_label(self) -> None:
        cases = (
            TableParams(
                rows=[
                    ["Apple", 5, 70]
                ],
                labels=["Fruit", "Tastiness", "Sweetness"]
            ),
            TableParams(
                rows=[
                    ["Apple", 5, 70, "Red"],
                    ["Banana", 3, 5, "Yellow"],
                    ["Cherry", 7, 31, "Red"],
                ],
                labels=["Fruit", "Tastiness", "Sweetness", "Colour"]
            ),
            TableParams(
                rows=[
                    ["Apple", 5, 70, "Red", 76],
                    ["Banana", 3, 5, "Yellow", 8],
                    ["Cherry", 7, 31, "Red", 92],
                    ["Kiwi", 4, 102, "Green", 1],
                    ["Strawberry", 6, 134, "Red", 28]
                ],
                labels=["Fruit", "Tastiness", "Sweetness", "Colour", "Smell"]
            )
        )

        for case in cases:
            self.run_against_solution(case, fail_msg="Failed when creating labels.")

    def test_006_align_center(self) -> None:
        cases = (
            TableParams(
                rows=[
                    ["Apple", 5, 70]
                ],
                labels=["Fruit", "Tastiness", "Sweetness"],
                centered=True
            ),
            TableParams(
                rows=[
                    ["Apple", 5, 70, "Red"],
                    ["Banana", 3, 5, "Yellow"],
                    ["Cherry", 7, 31, "Red"],
                ],
                labels=["Fruit", "Tastiness", "Sweetness", "Colour"],
                centered=True
            ),
            TableParams(
                rows=[
                    ["Apple", 5, 70, "Red", 76],
                    ["Banana", 3, 5, "Yellow", 8],
                    ["Cherry", 7, 31, "Red", 92],
                    ["Kiwi", 4, 102, "Green", 1],
                    ["Strawberry", 6, 134, "Red", 28]
                ],
                labels=["Fruit", "Tastiness", "Sweetness", "Colour", "Smell"],
                centered=True
            )
        )

        for case in cases:
            self.run_against_solution(case, fail_msg="Failed when using align_center parameter.")

    def test_007_column_width_scaling(self) -> None:
        cases = (
            TableParams(
                rows=[
                    ["Pneumonoultramicroscopicsilicovolcanoconiosis"],
                    ["Hippopotomonstrosesquippedaliophobia"],
                    ["Supercalifragilisticexpialidocious"],
                    ["Pseudopseudohypoparathyroidism"],
                    ["Floccinaucinihilipilification"],
                    ["Antidisestablishmentarianism"],
                    ["."]
                ],
                labels=["My Favourite Long Words"],
                centered=True
            ),
            TableParams(
                rows=[
                    ["Pneumonoultramicroscopicsilicovolcanoconiosis"],
                    ["Hippopotomonstrosesquippedaliophobia"],
                    ["Supercalifragilisticexpialidocious"],
                    ["Pseudopseudohypoparathyroidism"],
                    ["Floccinaucinihilipilification"],
                    ["Antidisestablishmentarianism"],
                    ["."]
                ],
                labels=["My Favourite Long Words"],
                centered=False
            ),
            TableParams(
                rows=[
                    ["A"],
                    ["B"],
                    ["C"],
                    ["D"],
                    ["E"],
                    ["F"],
                    ["Pneumonoultramicroscopicsilicovolcanoconiosis"]
                ],
                labels=["Alphabet"],
                centered=True
            ),
            TableParams(
                rows=[
                    ["A"],
                    ["B"],
                    ["C"],
                    ["D"],
                    ["E"],
                    ["F"],
                    ["Pneumonoultramicroscopicsilicovolcanoconiosis"]
                ],
                labels=["Alphabet"],
                centered=False
            ),
        )

        for case in cases:
            self.run_against_solution(case, fail_msg="Columns did not seem to scale in size appropriately.")

    def test_008_other_item_types(self) -> None:
        cases = (
            TableParams(
                rows=[
                    [None, 1, 2.5, None, 32j, '123'],
                ],
                labels=[3, None, 12, "A", 12.6, 12j],
                centered=True
            ),
        )

        for case in cases:
            self.run_against_solution(
                case,
                fail_msg="Could not handle list of object that implement __str__() correctly."
            )

    def test_009_custom_objects(self) -> None:
        class Fruit:
            def __init__(self, fruit: str):
                self.fruit = fruit

            def __str__(self) -> str:
                return self.fruit

            def __repr__(self):
                return f"<Fruit {self.fruit}>"

        apple = Fruit("Apple")
        banana = Fruit("Banana")
        cherry = Fruit("Cherry")
        kiwi = Fruit("Kiwi")
        strawberry = Fruit("Strawberry")

        cases = (
            TableParams(
                rows=[
                    [apple, 5, 70]
                ],
                labels=["Fruit", "Tastiness", "Sweetness"],
                centered=True
            ),
            TableParams(
                rows=[
                    [apple, 5, 70, "Red"],
                    [banana, 3, 5, "Yellow"],
                    [cherry, 7, 31, "Red"],
                ],
                labels=["Fruit", "Tastiness", "Sweetness", "Colour"],
                centered=True
            ),
            TableParams(
                rows=[
                    [apple, 5, 70, "Red", 76],
                    [banana, 3, 5, "Yellow", 8],
                    [cherry, 7, 31, "Red", 92],
                    [kiwi, 4, 102, "Green", 1],
                    [strawberry, 6, 134, "Red", 28]
                ],
                labels=["Fruit", "Tastiness", "Sweetness", "Colour", "Smell"],
                centered=True
            )
        )

        for case in cases:
            self.run_against_solution(case, fail_msg="Couldn't handle a class with a __str__ implementation.")

    def test_010_lots_of_rows(self) -> None:
        rows = [["Just", "Another", "Row"] for _ in range(25)]

        cases = (
            TableParams(rows=rows),
            TableParams(rows=rows, centered=True)
        )

        for case in cases:
            self.run_against_solution(case, fail_msg="Couldn't handle lots of rows.")

    def test_011_lots_of_columns(self) -> None:
        rows = [["Just", "Another", "Column"] * 4 for _ in range(25)]
        cases = (
            TableParams(rows=rows),
            TableParams(rows=rows, centered=True)
        )

        for case in cases:
            self.run_against_solution(case, fail_msg="Couldn't handle lots of cols.")