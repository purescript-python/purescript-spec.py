import sys


def exit(code):
    def _exit1():
        try:
            sys.exit(code)
        except Exception as e:
            pass
    return _exit1

