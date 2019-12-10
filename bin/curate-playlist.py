#!/usr/bin/env python

import os
import json
import click
import logging

@click.group()
def cli():
    pass

@click.command('generate', short_help='Generate data.')
@click.option('--directory', default="var/build", help='Write to directory.')
@click.option('--config', default='etc/example-config.json', help='Configuration filename.')
def generate(directory, config):
    try:
        with open(config, 'r') as f:
            cfg = json.load(f)
    except FileNotFoundError:
        print("Error: config {} not found".format(config))
        return(-1)
    except json.decoder.JSONDecodeError as e:
        print("Error: cannot parse {}".format(config))
        print(e)
        return(-1)

    print(cfg)

cli.add_command(generate)

if __name__ == '__main__':
    if not os.path.isdir('var'):
        os.mkdir('var')

    logging.basicConfig(
        filename='var/curate.log',
        level=logging.INFO
    )

    print("curate 0.1")
    cli()
