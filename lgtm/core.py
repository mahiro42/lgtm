import click


@click.command()
def cli():
    """A tool to generate LGTM images"""
    lgtm()
    click.echo("lgtm")  # for debugging


def lgtm():
    # [todo] Add some logic here
    pass
