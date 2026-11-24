"""Пул інгредієнтів (200 унікальних)."""
import random
from dataclasses import dataclass

from config import ELEMENTS
from exceptions import ItemNotFoundError

NOUNS = {
    "Вогонь": ["Вогнецвіт", "Жарокорінь", "Лава-камінь", "Жаринка", "Попіл фенікса"],
    "Вода": ["Морська перлина", "Водорість", "Лотос", "Росяна крапля", "Корал"],
    "Земля": ["Глиногриб", "Кремінь", "Кореневище", "Мох", "Самородок"],
    "Повітря": ["Пір'їна грифона", "Хмарник", "Вітрогон", "Пухнатка", "Бурепил"],
    "Світло": ["Сонячник", "Зоряний пил", "Місячний камінь", "Світлогриб", "Промінець"],
    "Тінь": ["Тіньовець", "Воронове перо", "Нічна фіалка", "Темнокорінь", "Сутінкова ягода"],
    "Життя": ["Живокіст", "Меліса", "Цвіт папороті", "Золотий корінь", "Квітка життя"],
    "Смерть": ["Беладона", "Могильна кістка", "Блідий гриб", "Вовче лико", "Трупниця"],
    "Дух": ["Привидниця", "Ехо-кришталь", "Духолист", "Душевик", "Ефірна квітка"],
    "Хаос": ["Хаосцвіт", "Безоднець", "Кристал розладу", "Мінлива слиз", "Дикий корінь"],
}

PLACES = ["з Туманних боліт", "з Сірих гір", "з Тихої долини", "з Забутих руїн"]


@dataclass(frozen=True)
class Ingredient:
    id: int
    name: str
    element: str


def _build_pool():
    pool = {}
    next_id = 0
    for element, _, _ in ELEMENTS:
        for noun in NOUNS[element]:
            for place in PLACES:
                pool[next_id] = Ingredient(next_id, f"{noun} {place}", element)
                next_id += 1
    return pool


INGREDIENT_POOL = _build_pool()


def get_ingredient(ingredient_id):
    try:
        return INGREDIENT_POOL[ingredient_id]
    except KeyError:
        raise ItemNotFoundError(f"Інгредієнта з id={ingredient_id} не існує")


def random_ingredient():
    try:
        return random.choice(list(INGREDIENT_POOL.values()))
    except IndexError:
        raise ItemNotFoundError("Пул інгредієнтів порожній")