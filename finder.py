#!/usr/local/bin/python3

import argparse
import re
from termcolor import colored

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file', help='file name. multiple files allowed')
parser.add_argument('-r', '--regex', help='a pattern to search for')
parser.add_argument('-c', '--color', action='store_true', help='color output')
parser.add_argument('-u', '--underscore', action='store_true',
                    help='puts a "^" sign under the match')
parser.add_argument('-m', '--machine', action='store_true',
                    help='generate machine-readable format')
args = parser.parse_args()
# iterate over optional flags and set boolean accordingly
for arg in ('color', 'underscore', 'machine'):
    arg = (getattr(args, arg))
# set mandatory args and ask for input if their were not set
if not args.regex:
    regex = input("--No regex given--\nPlease feed me with desired pattern:")
else:
    regex = args.regex
if not args.file:
    file = input("--No file specified--\nPlease feed me with text to parse:")
    temp_file = open("stdin", 'w')
    for line in file:
        temp_file.write(line)
    temp_file.close()
    file = "stdin"
else:
    file = args.file


class match_finder:
    def parse_file(file, regex):
        regex = re.compile(regex)  # change regex type
        with open(file, 'r') as current_file:
            for line_i, line in enumerate(current_file, 1):
                if regex.search(line):
                    for match in re.finditer(regex, line):
                        group = match.group()
                        start_position = match.start()
                        end_position = match.end()
                        line_no = ("%d" % line_i)
                        finding = ('"{}"'.format(group))
                        in_string = colored(match.string)
                        generate_output.out(file, line_no, finding, in_string,
                                            start_position, end_position)


class generate_output:
    def out(file, line_no, finding, in_string, start_position, end_position):
        if args.color:
            in_string = str(in_string[0:start_position] +
                            colored(in_string[start_position:end_position],
                                    'green') + in_string[end_position:])
            finding = (colored(finding, 'green'))
            file = (colored(file, 'blue'))
            line_no = (colored(line_no, 'red'))
        if args.machine:
            print(file + ":" + line_no + ":" + str(start_position) +
                  ":" + finding)
        else:
            print(in_string + "file: " + file + " " + "line: " + line_no)
            if args.underscore:
                print(' ' * int(start_position) +
                      '^' * (end_position - start_position))

for each in file.split():
    match_finder.parse_file(file, regex)
