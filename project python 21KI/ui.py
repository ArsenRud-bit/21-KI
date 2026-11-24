"""Виведення інформації в консоль."""
from config import ELEMENTS, WIN_GOLD, MAX_DAYS
from ingredients import get_ingredient
from potions import get_potion, find_potion
from market import potion_price


def show_status(game):
    p = game.player
    print("\n" + "=" * 60)
    print(f" День {game.day}/{MAX_DAYS} | Золото: {p.gold} / {WIN_GOLD}")
    print("=" * 60)


def show_ingredients(player):
    inv = player.ingredients
    print(f"\n--- Інгредієнти (слотів {len(inv.slots)}/{inv.max_slots}) ---")
    if not inv.slots:
        print("  (порожньо)")
    for n, (item_id, cnt) in enumerate(inv.slots, 1):
        try:
            print(f"  [{n:>2}] {get_ingredient(item_id).name} x{cnt}")
        except Exception as e:
            print(f"  [{n:>2}] ??? ({e})")


def show_potions(player, multipliers=None):
    inv = player.potions
    print(f"\n--- Зілля (слотів {len(inv.slots)}/{inv.max_slots}) ---")
    if not inv.slots:
        print("  (порожньо)")
    for n, (item_id, cnt) in enumerate(inv.slots, 1):
        try:
            potion = get_potion(item_id)
            price = ""
            if multipliers:
                price = f" | ціна: {potion_price(potion, multipliers)}"
            print(f"  [{n:>2}] {potion.name} x{cnt}{price}")
        except Exception as e:
            print(f"  [{n:>2}] ??? ({e})")


def show_recipe_book():
    print("\n--- Книга рецептів ---")
    for name, _, _ in ELEMENTS:
        print(f"\n[{name}]")
        for grade in range(1, 6):
            try:
                pt = find_potion(name, grade)
                print(f"  {pt.name}: {pt.recipe_text} (база {pt.base_price})")
            except Exception as e:
                print(f"  ! {e}")


def show_distinct_ingredients(player):
    ids = player.ingredients.item_ids()
    for n, item_id in enumerate(ids, 1):
        print(f"  {n}. {get_ingredient(item_id).name} "
              f"[{get_ingredient(item_id).element}] x{player.ingredients.count(item_id)}")
    return ids