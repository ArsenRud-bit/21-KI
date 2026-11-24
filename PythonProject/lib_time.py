import time


def demo_time():
    try:
        start = time.perf_counter()
        time.sleep(0.3)
        elapsed = time.perf_counter() - start
        print("Зараз:", time.strftime("%d.%m.%Y %H:%M:%S"))
        print(f"Пауза тривала {elapsed:.2f} с")
    except Exception as e:
        print("Помилка time:", e)