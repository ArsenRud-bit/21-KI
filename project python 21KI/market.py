"""Ринок: щоденні ціни та продаж."""
import random

from config import ELEMENTS
from exceptions import NotEnoughItemsError
from potions import get_potion


def generate_prices():
    """Множник ціни для кожної стихії на день."""
    return {name: round(random.uniform(0.8, 1.3), 2) for name, _, _ in ELEMENTS}


def potion_price(potion, multipliers):
    try:
        return round(potion.base_price * multipliers[potion.element])
    except KeyError:
        return round(potion.base_price)


def sell(player, potion_id, amount, multipliers):
    """Продає amount зіль. Повертає виручку."""
    potion = get_potion(potion_id)
    if player.potions.count(potion_id) < amount:
        raise NotEnoughItemsError("Немає стільки зіль")
    player.potions.remove(potion_id, amount)
    income = potion_price(potion, multipliers) * amount
    player.gold += income
    return income


def sell_all(player, multipliers):
    total = 0
    for potion_id in player.potions.item_ids():
        total += sell(player, potion_id, player.potions.count(potion_id), multipliers)
    return total