import qrcode


def demo_qrcode():
    try:
        qr = qrcode.QRCode(border=1)
        qr.add_data("https://github.com")
        qr.make()
        qr.print_ascii(invert=True)
    except Exception as e:
        print("Помилка qrcode:", e)