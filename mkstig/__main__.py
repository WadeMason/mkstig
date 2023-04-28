#!/usr/bin/env python

import os

import click

from __init__ import __version__

@click.group()
@click.version_option(
    __version__,
    message=f"MkSTIG %(version)s", 
)
def cli():
    pass

@cli.command()
@click.option('-d', '--output-dir', type=click.Path())
def build(**kwargs):
    output_dir = kwargs.get('output_dir') or os.environ.get('MKSTIG_OUTPUT_PATH') or 'public'

    from commands import build
    build.build(output_dir)

if __name__ == "__main__":
    cli()