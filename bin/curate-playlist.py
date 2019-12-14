#!/usr/bin/env python

import os
import re
import glob
import json
import click

def load_cfg(config):
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
    return(cfg)

@click.group()
def cli():
    pass

@click.command('analyze', short_help='Analyze path.')
@click.option('--config', default='etc/example-config.json', help='Configuration filename.')
def analyze(config):
    cfg = load_cfg(config)

    import nltk
    from nltk import ngrams, FreqDist
    from nltk.corpus import stopwords

    word_list = []
    for search_path in cfg['subdirs']:
        search_glob = "{}/{}/**".format(cfg["path"], search_path)
        for filename in glob.iglob(search_glob, recursive=True):
            word_list += re.split(r'\W', filename.lower())

    filtered_words = [word for word in word_list if word not in stopwords.words('english')]
    filtered_words = [word for word in filtered_words if word not in ['vids', '_db', 'mp4', '_', '1', '2']]

    raw = " ".join(filtered_words)
    bag = nltk.word_tokenize(raw)
    freqdist = FreqDist(bag)
    # words = [ x for (x, c) in freqdist.items() if c > 5 ]
    words_sorted = sorted(freqdist.items(), key = 
        lambda kv:(kv[1], kv[0]))
    top_words = words_sorted[-30:]
    top_words.reverse()
    for word in top_words:
        print("{1}: {0}".format(*word))

@click.command('generate', short_help='Generate data.')
@click.option('--config', default='etc/example-config.json', help='Configuration filename.')
def generate(config):
    cfg = load_cfg(config)
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
cli.add_command(analyze)

if __name__ == '__main__':
    print("curate 0.1")
    cli()
