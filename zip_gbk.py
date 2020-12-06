#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import zipfile


def main(filename):
    with zipfile.ZipFile(filename, "r") as thiszipfile:
        base = os.path.dirname(filename)
        if len(thiszipfile.namelist()) > 1:
            base, _ = os.path.splitext(filename)
        for name in thiszipfile.namelist():
            utf8name = os.path.join(base, name.encode("cp437").decode('gbk'))
            print("Extracting " + utf8name)
            pathname = os.path.dirname(utf8name)
            if not os.path.exists(pathname) and pathname != "":
                os.makedirs(pathname,exist_ok=True)
            data = thiszipfile.read(name)
            if not os.path.exists(utf8name):
                with open(utf8name, "wb") as fo:
                    fo.write(data)


if __name__ == "__main__":
    main(sys.argv[1])
