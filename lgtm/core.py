import click

from lgtm.drawer import save_with_message
from lgtm.image_source import get_image


@click.command()
@click.option("--message", "-m", default="LGTM", show_default=True,
              help="Text to be put in the generated image")
@click.argument("keyword")
def cli(keyword: str, message: str) -> None:
    """A tool to generate LGTM images"""
    lgtm(keyword, message)
    click.echo("lgtm")  # for debugging


def lgtm(keyword: str, message: str) -> None:
    with get_image(keyword) as fp:
        save_with_message(fp, message)
