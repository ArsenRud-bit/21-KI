"""Власні винятки гри."""


class GameError(Exception):
    """Базовий виняток гри."""


class InventoryFullError(GameError):
    """В інвентарі немає місця."""


class NotEnoughItemsError(GameError):
    """Недостатньо предметів."""


class ItemNotFoundError(GameError):
    """Предмет не знайдено в пулі."""


class QuitGame(Exception):
    """Гравець вирішив вийти з гри."""