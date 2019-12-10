#!/usr/bin/env python

import os
import re
import glob
import json
import click
import logging

@click.group()
def cli():
    pass

@click.command('generate', short_help='Generate data.')
@click.option('--config', default='etc/example-config.json', help='Configuration filename.')
def generate(config):
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

    if not os.path.isdir(cfg["output"]):
        os.mkdir(cfg["output"])

    for name, pattern in cfg['patterns'].items():
        buf = ""
        for search_path in cfg['search']:
            for filename in glob.iglob('{}/**'.format(search_path), recursive=True):
                if re.search(pattern, filename):
                    buf += "{}\n".format(filename)
        if buf != "":
            with open("{}/{}.m3u".format(cfg["output"], name), "w") as f:
                f.write("#EXTM3U\n")
                f.write(buf)


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
