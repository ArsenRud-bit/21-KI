"""Інвентар зі слотами та стаками."""
import copy

from exceptions import InventoryFullError, NotEnoughItemsError


class Inventory:
    def __init__(self, max_slots, stack_size, title="Інвентар"):
        self.max_slots = max_slots
        self.stack_size = stack_size
        self.title = title
        self.slots = []  # список [item_id, count]

    def count(self, item_id):
        return sum(c for i, c in self.slots if i == item_id)

    def item_ids(self):
        ids = []
        for i, _ in self.slots:
            if i not in ids:
                ids.append(i)
        return ids

    def total_items(self):
        return sum(c for _, c in self.slots)

    def free_capacity(self, item_id):
        in_stacks = sum(self.stack_size - c for i, c in self.slots if i == item_id)
        free_slots = self.max_slots - len(self.slots)
        return in_stacks + free_slots * self.stack_size

    def can_add(self, item_id, amount=1):
        return self.free_capacity(item_id) >= amount

    def add(self, item_id, amount=1):
        if amount <= 0:
            raise ValueError("Кількість має бути додатною")
        if not self.can_add(item_id, amount):
            raise InventoryFullError(f"{self.title}: недостатньо місця")
        for slot in self.slots:
            if amount == 0:
                break
            if slot[0] == item_id and slot[1] < self.stack_size:
                put = min(self.stack_size - slot[1], amount)
                slot[1] += put
                amount -= put
        while amount > 0:
            put = min(self.stack_size, amount)
            self.slots.append([item_id, put])
            amount -= put

    def remove(self, item_id, amount=1):
        if amount <= 0:
            raise ValueError("Кількість має бути додатною")
        if self.count(item_id) < amount:
            raise NotEnoughItemsError(f"{self.title}: недостатньо предметів")
        for slot in reversed(self.slots):
            if amount == 0:
                break
            if slot[0] == item_id:
                take = min(slot[1], amount)
                slot[1] -= take
                amount -= take
        self.slots = [s for s in self.slots if s[1] > 0]

    def copy(self):
        return copy.deepcopy(self)