#!/usr/bin/python

import os
import sys
import argparse

# Jam Master W. Because it's a Wrapper.

build_methods = []
run_methods = []

def add_build_method(method):
    build_methods.append(method)

def add_run_method(method):
    run_methods.append(method)

def main():
    parser = argparse.ArgumentParser(description="do some stuff")
    parser.add_argument('--build', action='store_true')
    parser.add_argument('command', help='command to wrap', nargs="*")
    args = parser.parse_args()

    if args.build:
        for m in build_methods:
            m()
    else:
        for m in run_methods:
            m()
        os.execvp(args.command[0], args.command)
