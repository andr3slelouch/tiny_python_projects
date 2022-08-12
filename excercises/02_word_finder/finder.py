#!/usr/bin/env python3
"""
Author : Me <me@foo.com>
Date   : today
Purpose: Rock the Casbah
"""

import argparse

# --------------------------------------------------
import sys


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        nargs='*',
                        default=[sys.stdin],
                        type=argparse.FileType('rt'),
                        help='Input file(s)')

    parser.add_argument('-w',
                        '--word',
                        help='Palabra a ser encontrada',
                        metavar='str',
                        type=str,
                        default='')

    parser.add_argument('-r',
                        '--replace',
                        help='Palabra para reemplazar la o las palabras buscadas',
                        metavar='str',
                        type=str,
                        default=None)

    parser.add_argument('-s',
                        '--substring',
                        help='Habilita la búsqueda de las palabras como parte de otras',
                        action='store_true')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        nargs='*',
                        metavar='str',
                        type=str,
                        default=[])

    return parser.parse_args()


def count_words_in_string(searched_word, string, substring_flag=False) -> int:
    counter = 0
    words = string.split()
    for word in words:
        if word == searched_word or (substring_flag and searched_word in word):
            counter += 1
    return counter


def replace_word(searched_word, replacing_word, string):
    words = string.split()
    for i, word in enumerate(words):
        if word == searched_word:
            words[i] = replacing_word
    return " ".join(words)


def write_files(out_files_list, files_dicts):
    keys_list = files_dicts.keys()
    for file_name, key in zip(out_files_list, keys_list):
        with open(file_name, "wt") as replaced_file:
            replaced_file.writelines(files_dicts[key]["contents"])


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    searched_word = args.word
    replaced_word = args.replace
    substring_flag = args.substring
    files_dicts = {}
    total_found_words = 0
    for file_handler in args.file:
        file_name = file_handler.name
        current_dict = {}
        num_searched_word = 0
        file_contents = []
        for line in file_handler:
            num_searched_word += count_words_in_string(searched_word, line, substring_flag)
            if replaced_word is not None:
                if substring_flag:
                    file_contents.append(line.replace(searched_word, replaced_word))
                else:
                    file_contents.append(replace_word(searched_word, replaced_word, line) + "\n")
        current_dict["contents"] = file_contents
        files_dicts[file_name] = current_dict
        total_found_words += num_searched_word
        print(f'{searched_word:5} {num_searched_word:5} {file_handler.name}')

    if len(args.file) > 1:
        print(f'{searched_word:5} {total_found_words:5} total')

    if replaced_word is not None:
        if len(args.file) == len(args.outfile):
            write_files(args.outfile, files_dicts)
        elif len(args.file) > len(args.outfile):
            out_files_list = args.outfile
            for num in range(len(args.outfile), len(args.file)):
                out_files_list.append(args.file[num].name)
            write_files(out_files_list, files_dicts)
        else:
            out_files_list = args.outfile[:len(args.file)]
            write_files(out_files_list, files_dicts)


# --------------------------------------------------
if __name__ == '__main__':
    main()
