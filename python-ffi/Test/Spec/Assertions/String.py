def _startsWith(subs):
    def _startsWith1(s):
        return s.startswith(subs)

    return _startsWith1


def _endsWith(subs):
    def _endsWith1(s):
        return s.endswith(subs)

    return _endsWith1

