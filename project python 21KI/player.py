"""Гравець."""
from config import (START_GOLD, POTION_SLOTS, POTION_STACK,
                    INGREDIENT_SLOTS, INGREDIENT_STACK)
from exceptions import InventoryFullError
from ingredients import random_ingredient
from inventory import Inventory


class Player:
    def __init__(self):
        self.gold = START_GOLD
        self.potions = Inventory(POTION_SLOTS, POTION_STACK, "Інвентар зіль")
        self.ingredients = Inventory(INGREDIENT_SLOTS, INGREDIENT_STACK,
                                     "Інвентар інгредієнтів")

    def receive_ingredients(self, amount):
        """Видає випадкові інгредієнти. Повертає (отримані, втрачені)."""
        got, lost = [], []
        for _ in range(amount):
            try:
                ing = random_ingredient()
                self.ingredients.add(ing.id)
                got.append(ing)
            except InventoryFullError:
                lost.append(ing)
        return got, lost