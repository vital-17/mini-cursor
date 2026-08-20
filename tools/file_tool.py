import os


WORKSPACE = "workspace"


def create_file(filename, content):

    if not os.path.exists(WORKSPACE):
        os.makedirs(WORKSPACE)


    filepath = os.path.join(
        WORKSPACE,
        filename
    )


    with open(
        filepath,
        "w",
        encoding="utf-8"
    ) as f:

        f.write(content)


    return filepath



def read_file(filename):

    filepath = os.path.join(
        WORKSPACE,
        filename
    )


    with open(
        filepath,
        "r",
        encoding="utf-8"
    ) as f:

        return f.read()