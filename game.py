"""Ігровий цикл."""
from config import (DAILY_INGREDIENTS, START_INGREDIENTS, DAILY_COST,
                    WIN_GOLD, MAX_DAYS, ELEMENTS)
from alchemy import brew, count_element
from exceptions import GameError
from input_utils import read_int
from market import generate_prices, sell, sell_all
from player import Player
from potions import find_potion
import ui


class Game:
    def __init__(self):
        self.player = Player()
        self.day = 1
        self.won = False

    # ---------- основний цикл ----------
    def run(self):
        self._intro()
        self._give_ingredients(START_INGREDIENTS, "Стартовий набір")
        while True:
            self._start_day()
            self._day_actions()
            if self._end_day():
                break
            self.day += 1
        self._ending()

    def _intro(self):
        print("=" * 60)
        print(" АЛХІМІК: гра-RPG")
        print(f" Мета: назбирати {WIN_GOLD} золотих за {MAX_DAYS} днів.")
        print(f" Щодня потрібно платити {DAILY_COST} золотих за життя.")
        print("=" * 60)

    def _give_ingredients(self, amount, label):
        try:
            got, lost = self.player.receive_ingredients(amount)
            print(f"\n{label}:")
            for ing in got:
                print(f"  + {ing.name} [{ing.element}]")
            for ing in lost:
                print(f"  ! Немає місця, пропало: {ing.name}")
        except GameError as e:
            print(f"Помилка видачі інгредієнтів: {e}")

    def _start_day(self):
        self.prices = generate_prices()
        self._give_ingredients(DAILY_INGREDIENTS, f"Ранок дня {self.day}")

    # ---------- дії протягом дня ----------
    def _day_actions(self):
        while True:
            ui.show_status(self)
            print("1. Інгредієнти  2. Зілля  3. Зварити зілля")
            print("4. Книга рецептів  5. Викинути інгредієнти  6. Завершити день")
            choice = read_int("Ваш вибір: ", 1, 6)
            try:
                if choice == 1:
                    ui.show_ingredients(self.player)
                elif choice == 2:
                    ui.show_potions(self.player, self.prices)
                elif choice == 3:
                    self._brew_menu()
                elif choice == 4:
                    ui.show_recipe_book()
                elif choice == 5:
                    self._discard_menu()
                else:
                    return
            except GameError as e:
                print(f"  ! {e}")
            except Exception as e:
                print(f"  ! Неочікувана помилка: {e}")

    def _brew_menu(self):
        if not self.player.ingredients.slots:
            print("  У вас немає інгредієнтів.")
            return
        print("\nОберіть стихію (0 — назад):")
        for n, (name, _, _) in enumerate(ELEMENTS, 1):
            have = count_element(self.player.ingredients, name)
            print(f"  {n}. {name} (є інгредієнтів: {have})")
        e_choice = read_int("Стихія: ", 0, len(ELEMENTS))
        if e_choice == 0:
            return
        element = ELEMENTS[e_choice - 1][0]

        g_choice = read_int("Ступінь зілля (1-5, 0 — назад): ", 0, 5)
        if g_choice == 0:
            return
        potion = find_potion(element, g_choice)
        print(f"\n{potion.name}: {potion.recipe_text}")

        print("Оберіть каталізатор (0 — назад):")
        ids = ui.show_distinct_ingredients(self.player)
        c_choice = read_int("Каталізатор: ", 0, len(ids))
        if c_choice == 0:
            return
        brew(self.player, potion, ids[c_choice - 1])
        print(f"  ✔ Зварено: {potion.name}")

    def _discard_menu(self):
        ids = self.player.ingredients.item_ids()
        if not ids:
            print("  Нічого викидати.")
            return
        print("Що викинути (0 — назад):")
        ids = ui.show_distinct_ingredients(self.player)
        choice = read_int("Номер: ", 0, len(ids))
        if choice == 0:
            return
        item_id = ids[choice - 1]
        amount = read_int("Скільки: ", 1, self.player.ingredients.count(item_id))
        self.player.ingredients.remove(item_id, amount)
        print("  Викинуто.")

    # ---------- кінець дня ----------
    def _end_day(self):
        """Повертає True, якщо гра закінчилась."""
        self._sell_menu()
        p = self.player
        if p.gold < DAILY_COST:
            print(f"\nНе вистачає {DAILY_COST} золотих на життя!")
            self.won = False
            return True
        p.gold -= DAILY_COST
        print(f"\nВи заплатили {DAILY_COST} за життя. Золото: {p.gold}")

        if p.gold >= WIN_GOLD:
            self.won = True
            return True
        if self.day >= MAX_DAYS:
            self.won = False
            return True
        return False

    def _sell_menu(self):
        while self.player.potions.slots:
            print("\n=== Вечірній ринок ===")
            ui.show_potions(self.player, self.prices)
            print("1. Продати все  2. Продати конкретне  3. Не продавати")
            choice = read_int("Вибір: ", 1, 3)
            try:
                if choice == 1:
                    income = sell_all(self.player, self.prices)
                    print(f"  Виручка: {income}")
                elif choice == 2:
                    ids = self.player.potions.item_ids()
                    n = read_int("Номер виду зілля (за порядком у списку): ", 1, len(ids))
                    item_id = ids[n - 1]
                    amount = read_int("Скільки: ", 1, self.player.potions.count(item_id))
                    income = sell(self.player, item_id, amount, self.prices)
                    print(f"  Виручка: {income}")
                else:
                    return
            except GameError as e:
                print(f"  ! {e}")
        print("\nЗілля для продажу більше немає.")

    def _ending(self):
        print("\n" + "=" * 60)
        if self.won:
            print(" ПЕРЕМОГА! Ваші еліксири прославились на все королівство.")
            print(" Король призначає вас Головним Алхіміком двору!")
        else:
            print(" ПОРАЗКА. Лабораторію забрали за борги,")
            print(" а ваші колби розбили кредитори...")
        print(f" Днів прожито: {self.day}, золота: {self.player.gold}")
        print("=" * 60)