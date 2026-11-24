import io


def demo_io():
    try:
        buffer = io.StringIO()
        buffer.write("Привіт з пам'яті!")
        print("Вміст буфера:", buffer.getvalue())
        buffer.close()
    except Exception as e:
        print("Помилка io:", e)