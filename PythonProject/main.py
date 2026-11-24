from lib_requests import demo_requests
from lib_numpy import demo_numpy
from lib_pandas import demo_pandas
from lib_pillow import demo_pillow
from lib_colorama import demo_colorama
from lib_pyfiglet import demo_pyfiglet
from lib_qrcode import demo_qrcode
from lib_faker import demo_faker
from lib_tqdm import demo_tqdm
from lib_rich import demo_rich
from lib_os import demo_os
from lib_io import demo_io
from lib_time import demo_time
from lib_math import demo_math
from lib_random import demo_random

DEMOS = [
    ("requests", demo_requests),
    ("numpy", demo_numpy),
    ("pandas", demo_pandas),
    ("pillow", demo_pillow),
    ("colorama", demo_colorama),
    ("pyfiglet", demo_pyfiglet),
    ("qrcode", demo_qrcode),
    ("faker", demo_faker),
    ("tqdm", demo_tqdm),
    ("rich", demo_rich),
    ("os", demo_os),
    ("io", demo_io),
    ("time", demo_time),
    ("math", demo_math),
    ("random", demo_random),
]


def main():
    for name, func in DEMOS:
        print(f"\n===== {name} =====")
        try:
            func()
        except Exception as e:
            print(f"Збій у {name}: {e}")


if __name__:
    main()