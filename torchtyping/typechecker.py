import typeguard


_typechecked = typeguard.typechecked


def typechecked(*args, **kwargs):
    pass


global patched_typeguard = False


def patch_typeguard():
    if not patched_typeguard:
        global patched_typeguard = True
        typeguard.typechecked = typechecked