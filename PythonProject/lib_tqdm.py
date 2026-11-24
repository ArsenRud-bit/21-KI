import time
from tqdm import tqdm


def demo_tqdm():
    try:
        for _ in tqdm(range(20), desc="Завантаження"):
            time.sleep(0.05)
    except Exception as e:
        print("Помилка tqdm:", e)