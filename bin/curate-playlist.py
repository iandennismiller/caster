#!/usr/bin/env python

import os
import re
import glob
import json
import click

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

    base_cwd = os.getcwd()

    for name, pattern in cfg['patterns'].items():
        if type(pattern) is dict:
            pattern_include = pattern["include"]
            pattern_exclude = pattern["exclude"]
        else:
            pattern_include = pattern
            pattern_exclude = None

        buf = ""
        for search_path in cfg['subdirs']:
            search_glob = "{}/{}/**".format(cfg["path"], search_path)
            for filename in glob.iglob(search_glob, recursive=True):
                was_found = False
                if pattern_exclude:
                    if re.search(pattern_include, filename, re.IGNORECASE) and not re.search(pattern_exclude, filename, re.IGNORECASE):
                        was_found = True
                else:
                    if re.search(pattern_include, filename, re.IGNORECASE):
                        was_found = True
                if was_found:
                    found = os.path.join(base_cwd, filename)
                    buf += "{}\n".format(found)
        if buf != "":
            filename = "{}/{}.m3u".format(cfg["path"], name)
            print("write {}".format(filename))
            with open(filename, "w") as f:
                f.write("#EXTM3U\n")
                f.write(buf)


cli.add_command(generate)

if __name__ == '__main__':
    print("curate 0.1")
    cli()
