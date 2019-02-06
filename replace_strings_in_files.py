import argparse
import glob
import logging
import os

logging.basicConfig(format='[%(asctime)s] %(levelname)-8s | %(message)s',
                    datefmt='%d-%b-%Y %H:%M:%S', level=logging.INFO)
log = logging.getLogger()

args_parser = argparse.ArgumentParser(description='Converts strings in files.')
args_parser.add_argument('-p', dest='path', default='files',
                         help='The path to the directory that contains the files to scan (default is \'files\')')
args_parser.add_argument('-e', dest='file_extension', default='',
                         help='The extension of the files to scan for string replacement (scans everything by default')
args_parser.add_argument('-b', dest='string_list_before', default='before.txt',
                         help='The file that contains strings to convert (each string in its own line)')
args_parser.add_argument('-a', dest='string_list_after', default='after.txt',
                         help='The file that contains strings to convert to (each string in its corresponding line)')


class StringReplacer:
    """ Replaces strings in files.

    Expects 2 files with the same amount of lines. Each line from the first file will be replaced with the corresponding
    line from the second file.

    Args:
        path: The path to the directory that contains the files to scan.
        file_extension: The extension of the files to scan for string replacement
        string_list_before: The file that contains strings to convert (each string in its own line).
        string_list_after: The file that contains strings to convert to (each string in its corresponding line).

     """

    def __init__(self, path, file_extension, string_list_before, string_list_after):
        self.path = path
        self.file_extension = file_extension
        self.string_list_before = string_list_before
        self.string_list_after = string_list_after

    def replace(self):
        with open(self.string_list_before, 'r') as f:
            strings = f.readlines()
        strings_before = [s.strip() for s in strings]
        log.info('Strings to replace loaded from: {}'.format(self.string_list_before))

        with open(self.string_list_after, 'r') as f:
            strings = f.readlines()
        strings_after = [s.strip() for s in strings]
        log.info('Strings to replace to loaded from: {}'.format(self.string_list_after))

        # string_list_before and string_list_after must be have the same amount of strings:
        if len(strings_before) is not len(strings_after):
            log.fatal(
                '\'{}\' and \'{}\' files must have the same amount of lines. Exiting...'.format(self.string_list_before,
                                                                                                self.string_list_after))
            raise SystemExit(1)

        strings = dict(zip(strings_before, strings_after))

        # No need to keep these in RAM:
        del strings_before
        del strings_after

        if not self.file_extension:
            file_pattern = '*'
            log.info('All files in \'{}\' will be scanned.'.format(self.path))
        else:
            file_pattern = '*.{}'.format(self.file_extension)
            log.info('\'{}\' files in \'{}\' will be scanned.'.format(self.file_extension, self.path))

        for file in glob.glob(os.path.join(self.path, file_pattern)):
            log.info('Replacing strings in: {}'.format(file))
            name, extension = os.path.splitext(file)
            old_file = '{}.OLD.{}'.format(name, extension)
            os.rename(file, old_file)
            with open(old_file, 'r') as f:
                file_data = f.read()

            file_data = file_data
            for before, after in strings.items():
                file_data = file_data.replace(before, after)

            with open(file, 'w') as f:
                f.write(file_data)


if __name__ == '__main__':
    args = args_parser.parse_args()
    replacer = StringReplacer(args.path, args.file_extension, args.string_list_before, args.string_list_after)
    log.info('Starting string replacement...')
    replacer.replace()
    log.info('Done')
