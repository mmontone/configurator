#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# CAVEAT UTILITOR
# This file was automatically generated by Grako.
#    https://bitbucket.org/apalala/grako/
# Any changes you make to it will be overwritten the
# next time the file is generated.
#

from __future__ import print_function, division, absolute_import, unicode_literals
from grako.parsing import * # @UnusedWildImport
from grako.exceptions import * # @UnusedWildImport

__version__ = '13.364.01.51.12'

class dependenciesParser(Parser):
    def __init__(self, whitespace='', nameguard=True, **kwargs):
        super(dependenciesParser, self).__init__(whitespace=whitespace,
            nameguard=nameguard, **kwargs)

    @rule_def
    def _number_(self):
        self._pattern(r'[0-9]+')

    @rule_def
    def _identifier_(self):
        self._ident_start_()
        def block0():
            self._ident_cont_()
        self._closure(block0)

    @rule_def
    def _ident_start_(self):
        self._pattern(r'[a-zA-Z_\ ]')

    @rule_def
    def _ident_cont_(self):
        with self._choice():
            with self._option():
                self._ident_start_()
            with self._option():
                self._pattern(r'[0-9]')
            self._error('expecting one of: [0-9]')

    @rule_def
    def _spacing_(self):
        def block0():
            self._space_()
        self._closure(block0)

    @rule_def
    def _space_(self):
        with self._choice():
            with self._option():
                self._token(' ')
            with self._option():
                self._token('\t')
            with self._option():
                self._check_eof()
            self._error('expecting one of: \t  ')

    @rule_def
    def _eol_(self):
        with self._choice():
            with self._option():
                self._token('\r\n')
            with self._option():
                self._token('\n')
            with self._option():
                self._token('\r')
            self._error('expecting one of: \r \r\n \n')

    @rule_def
    def _option_path_(self):
        with self._choice():
            with self._option():
                self._identifier_()
                self.ast['@'] = self.last_node
                self._token('.')
                self._option_path_()
                self.ast['@'] = self.last_node
            with self._option():
                self._identifier_()
            self._error('no available options')

    @rule_def
    def _boolexp_(self):
        with self._choice():
            with self._option():
                self._boolterm_()
                self.ast['@'] = self.last_node
                self._spacing_()
                self._boolean_connector_()
                self.ast['@'] = self.last_node
                self._spacing_()
                self._boolexp_()
                self.ast['@'] = self.last_node
            with self._option():
                self._boolterm_()
            self._error('no available options')

    @rule_def
    def _boolterm_(self):
        with self._choice():
            with self._option():
                self._bool_literal_()
            with self._option():
                self._option_path_()
                self.ast['@'] = self.last_node
                self._spacing_()
                self._operation_()
                self.ast['@'] = self.last_node
                self._spacing_()
                self._value_()
                self.ast['@'] = self.last_node
            with self._option():
                self._token('(')
                self._spacing_()
                self._boolexp_()
                self.ast['@'] = self.last_node
                self._spacing_()
                self._token(')')
            self._error('no available options')

    @rule_def
    def _bool_literal_(self):
        with self._choice():
            with self._option():
                self._token('True')
            with self._option():
                self._token('False')
            self._error('expecting one of: False True')

    @rule_def
    def _value_(self):
        with self._choice():
            with self._option():
                self._number_()
            with self._option():
                self._literal_string_()
            with self._option():
                self._bool_literal_()
            with self._option():
                self._option_path_()
                self.ast['path'] = self.last_node
            self._error('no available options')

    @rule_def
    def _operation_(self):
        with self._choice():
            with self._option():
                self._token('IS')
            with self._option():
                self._token('=')
            with self._option():
                self._token('<>')
            with self._option():
                self._token('>')
            with self._option():
                self._token('<')
            self._error('expecting one of: > IS < <> =')

    @rule_def
    def _literal_string_(self):
        self._token("'")
        def block1():
            self._pattern(r'[\w\ ]')
        self._closure(block1)
        self.ast['@'] = self.last_node
        self._token("'")

    @rule_def
    def _boolean_connector_(self):
        with self._choice():
            with self._option():
                self._token('AND')
            with self._option():
                self._token('OR')
            with self._option():
                self._token('XOR')
            self._error('expecting one of: OR AND XOR')



class dependenciesSemanticParser(CheckSemanticsMixin, dependenciesParser):
    pass


class dependenciesSemantics(object):
    def number(self, ast):
        return ast

    def identifier(self, ast):
        return ast

    def ident_start(self, ast):
        return ast

    def ident_cont(self, ast):
        return ast

    def spacing(self, ast):
        return ast

    def space(self, ast):
        return ast

    def eol(self, ast):
        return ast

    def option_path(self, ast):
        return ast

    def boolexp(self, ast):
        return ast

    def boolterm(self, ast):
        return ast

    def bool_literal(self, ast):
        return ast

    def value(self, ast):
        return ast

    def operation(self, ast):
        return ast

    def literal_string(self, ast):
        return ast

    def boolean_connector(self, ast):
        return ast

def main(filename, startrule, trace=False):
    import json
    with open(filename) as f:
        text = f.read()
    parser = dependenciesParser(parseinfo=False)
    ast = parser.parse(text, startrule, filename=filename, trace=trace)
    print('AST:')
    print(ast)
    print()
    print('JSON:')
    print(json.dumps(ast, indent=2))
    print()

if __name__ == '__main__':
    import argparse
    import sys
    class ListRules(argparse.Action):
        def __call__(self, parser, namespace, values, option_string):
            print('Rules:')
            for r in dependenciesParser.rule_list():
                print(r)
            print()
            sys.exit(0)
    parser = argparse.ArgumentParser(description="Simple parser for dependencies.")
    parser.add_argument('-l', '--list', action=ListRules, nargs=0,
                        help="list all rules and exit")
    parser.add_argument('-t', '--trace', action='store_true',
                        help="output trace information")
    parser.add_argument('file', metavar="FILE", help="the input file to parse")
    parser.add_argument('startrule', metavar="STARTRULE",
                        help="the start rule for parsing")
    args = parser.parse_args()

    main(args.file, args.startrule, trace=args.trace)
