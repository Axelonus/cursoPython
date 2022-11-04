from __future__ import division


def make_division_by(n):
    def divide(x):
        print(x/n)
    return divide

def run():
    division_by_3 = make_division_by(3)
    division_by_3(18)
    division_by_5 = make_division_by(5)
    division_by_5(100)


if __name__ == '__main__':
    run()