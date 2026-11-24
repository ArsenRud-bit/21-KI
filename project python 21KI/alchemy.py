"""Варіння зіль."""
from exceptions import InventoryFullError, NotEnoughItemsError
from ingredients import get_ingredient


def count_element(inventory, element):
    total = 0
    for item_id in inventory.item_ids():
        try:
            if get_ingredient(item_id).element == element:
                total += inventory.count(item_id)
        except Exception:
            continue
    return total


def brew(player, potion, catalyst_id):
    """Варить 1 зілля. Атомарно: або все вдалось, або нічого не змінюється."""
    if not player.potions.can_add(potion.id, 1):
        raise InventoryFullError("В інвентарі зіль немає місця для нового зілля")

    if count_element(player.ingredients, potion.element) < potion.grade:
        raise NotEnoughItemsError(
            f"Потрібно {potion.grade} інгр. стихії «{potion.element}»")

    work = player.ingredients.copy()
    remaining = potion.grade
    for item_id in work.item_ids():
        if remaining == 0:
            break
        if get_ingredient(item_id).element == potion.element:
            take = min(work.count(item_id), remaining)
            work.remove(item_id, take)
            remaining -= take

    # може кинути NotEnoughItemsError, якщо каталізатор вже витрачено
    work.remove(catalyst_id, 1)

    player.ingredients = work
    player.potions.add(potion.id, 1)