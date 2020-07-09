import sys


def write(s):
    def _write1():
        try:
            sys.stdout.write(s)
        except Exception as e:
            pass

    return _write1

