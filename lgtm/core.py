import click


@click.command()
@click.option("--message", "-m", default="LGTM", show_default=True,
              help="Text to be put in the generated image")
@click.argument("keyword")
def cli(keyword: str, message: str) -> None:
    """A tool to generate LGTM images"""
    lgtm(keyword, message)
    click.echo("lgtm")  # for debugging


def lgtm(keyword: str, message: str) -> None:
    # [todo] Add some logic here
    pass
