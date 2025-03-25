#!/usr/bin/env python3

from pprint import pprint

from gendiff.cli import pars_args
from gendiff.generate_diff import generate_diff


def main():
    args = pars_args()
    diff = generate_diff(args.first_file, args.second_file)
    pprint(diff)


if __name__ == '__main__':
    main()