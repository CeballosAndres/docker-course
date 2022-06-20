"""Script para docker"""

import os

if __name__ == "__main__":
    print("Hola desde docker!!")

    for env, value in os.environ.items():
        print(f"{env} ==> {value}")
