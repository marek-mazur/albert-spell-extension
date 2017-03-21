#!/usr/bin/env python
#coding: utf-8

import os
import sys
import json
import subprocess
import re

albert_op = os.environ.get("ALBERT_OP")

if albert_op == "METADATA":
    metadata="""{
      "iid":"org.albert.extension.external/v2.0",
      "name":"spell",
      "version":"1.0",
      "author":"Marek Mazur",
      "dependencies":[],
      "trigger":"spell"
    }"""
    print(metadata)
    sys.exit(0)

elif albert_op == "NAME":
    print('spell')
    sys.exit(0)

elif albert_op == "INITIALIZE":
    sys.exit(0)

elif albert_op == "FINALIZE":
    sys.exit(0)

elif albert_op == "SETUPSESSION":
    sys.exit(0)

elif albert_op == "SETUPSESSION":
    sys.exit(0)

elif albert_op == "TEARDOWNSESSION":
    sys.exit(0)

elif albert_op == "QUERY":

    albert_query = os.environ.get("ALBERT_QUERY")
    phrase = ''
    language = ''

    match = re.search('^spell (?P<language>[^ ]{2,}) (?P<phrase>.*)$', albert_query)
    if match:
        phrase = match.group('phrase')
        language = match.group('language')

    if not language or not phrase:
        print('{"items": [' + ", ".join([]) + "]}")
        sys.exit(0)

    class Object(object):
        pass

    items = []
    cmd = "grep '^{phrase}' -m 5 ~/.local/share/albert/external/spell/{language}.dict"

    results = ""
    try:
        results = subprocess.check_output(cmd.format(phrase=phrase, language=language), shell=True)
    except subprocess.CalledProcessError:
        pass
    results = results.splitlines()

    for result in results:
        value = result.split(' ')[0]

        item = Object()
        item.id = "spell-result"
        item.name = value
        item.description = result
        item.icon = ""
        item.actions = []

        action = Object()
        action.command = "sh"
        action.name = "Copy {} to clipboard".format(value)
        cmd = 'echo -n "{0}" | xclip -i; echo -n "{0}" | xclip -i -selection clipboard;'
        action.arguments = ['-c', cmd.format(value)]
        item.actions.append(action)

        items.append(item)

    if len(items) == 0:
        item = Object()
        item.id = "spell-result"
        item.name = "'{phrase}' not found".format(phrase=phrase)
        item.description = ''
        item.icon = ""
        item.actions = []
        items.append(item)

    results = []
    for item in items:
        results += [json.dumps(item, default=lambda o: o.__dict__)]

    print('{"items": [' + ", ".join(results) + "]}")
    sys.exit(0)
