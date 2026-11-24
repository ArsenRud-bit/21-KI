"""Пул зіль (50 унікальних) та рецепти."""
from dataclasses import dataclass

from config import ELEMENTS, GRADE_NAMES
from exceptions import ItemNotFoundError


@dataclass(frozen=True)
class Potion:
    id: int
    name: str
    element: str
    grade: int        # 1..5
    base_price: float

    @property
    def recipe_text(self):
        return f"{self.grade} × інгредієнт стихії «{self.element}» + 1 будь-який каталізатор"


def _build_pool():
    pool = {}
    for e_idx, (element, genitive, base) in enumerate(ELEMENTS):
        for grade in range(1, 6):
            pid = e_idx * 5 + (grade - 1)
            name = f"{GRADE_NAMES[grade - 1]} зілля {genitive}"
            price = base * (grade + 1) * (1 + 0.2 * (grade - 1))
            pool[pid] = Potion(pid, name, element, grade, round(price, 2))
    return pool


POTION_POOL = _build_pool()


def get_potion(potion_id):
    try:
        return POTION_POOL[potion_id]
    except KeyError:
        raise ItemNotFoundError(f"Зілля з id={potion_id} не існує")


def find_potion(element, grade):
    for potion in POTION_POOL.values():
        if potion.element == element and potion.grade == grade:
            return potion
    raise ItemNotFoundError(f"Зілля ({element}, ступінь {grade}) не знайдено")