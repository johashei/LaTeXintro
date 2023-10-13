import numpy as np
import sys

def main():
    hjelp = "bruk: python terning.py <antall sider> <antall kast>"
    try:
        antall_sider = int(sys.argv[1])
        antall_kast = int(sys.argv[2])
        if (antall_sider < 1) or (antall_kast < 1):
            raise ValueError
    except IndexError:
        print(hjelp)
        sys.exit()
    except ValueError:
        print(hjelp)
        print("<antall sider> og <antall kast> må være positive heltall.")
        sys.exit()

    terning = Terning(antall_sider)
    resultat = terning.kast(antall_kast)
    print(f"Kastet {terning} {antall_kast} ganger:\n{resultat}")

class Terning:
    def __init__(self, antall_sider):
        self.rng = np.random.default_rng()
        self.antall_sider = antall_sider

    def __str__(self):
        return f"en {self.antall_sider}-sidet terning"

    def kast(self, antall_kast):
        return self.rng.integers(
            low=1,
            high=self.antall_sider,
            size=antall_kast,
            endpoint=True)

if __name__ == "__main__":
    main()
