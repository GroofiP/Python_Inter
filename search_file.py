import os


def find(name):
    for root, dirs, files in os.walk("/home"):
        if name in files:
            return f"{root}/{name}"


if __name__ == "__main__":
    pass
