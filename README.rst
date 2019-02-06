String Replacer
###############

| This script replaces strings in requested files.
| It expects 2 files with the same amount of lines to create the replacement "rules".
| Each line from the first file will be replaced with the corresponding line from the second file.

-----


.. contents::

.. section-numbering::

Usage
=====
This project requires:

* Python 3.6

Clone the source code
---------------------
In your working folder (your home folder, for example)

.. code-block:: bash

    git clone https://github.com/yevgenykuz/string_replacer.git

Configure and run
-----------------
- Create your replacement "rules" by editing the provided "before.txt" and "after.txt" files. You can point to your own files instead (*see arguments*)
- Put the files you want to scan in the provided "files" folder. You can point to your own folder instead (*see arguments*)

Run with:

.. code-block:: bash

    python replace_strings_in_files.py


Arguments
---------
.. code-block::

    usage: replace_strings_in_files.py [-h] [-p PATH] [-e FILE_EXTENSION]
                                       [-b STRING_LIST_BEFORE]
                                       [-a STRING_LIST_AFTER]

    optional arguments:
      -h, --help            show this help message and exit
      -p PATH               The path to the directory that contains the files to
                            scan (default is 'files')
      -e FILE_EXTENSION     The extension of the files to scan for string
                            replacement (scans everything by default
      -b STRING_LIST_BEFORE
                            The file that contains strings to convert (each string
                            in its own line)
      -a STRING_LIST_AFTER  The file that contains strings to convert to (each
                            string in its corresponding line)


Meta
====
Authors
-------
`yevgenykuz <https://github.com/yevgenykuz>`_

License
-------
BSD-3-Clause - `LICENSE <https://github.com/yevgenykuz/string_replacer/blob/master/LICENSE>`_

-----