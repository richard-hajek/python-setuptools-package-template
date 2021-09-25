import project_name
from project_name import a
from project_name.submodule import b

def main():
    a.echo(b.add(1, 3))
    print("Module version: " + project_name.VERSION)


if __name__ == "__main__":
    main()
