import typer


def cli(name: str):
    print('Hello', name)


if __name__ == "__main__":
    typer.run(cli)
