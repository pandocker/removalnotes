#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" wavedrom-inline
A pandoc filter which removes div block in "rmnote" class

applies MIT License (c) 2018 pandocker/Kazuki Yamamoto(k.yamamoto.08136891@gmail.com)
"""
import panflute as pf


class RemovalNotes(object):

    def __init__(self):
        pass

    def action(self, elem, doc):
        if isinstance(elem, pf.Div) and "rmnote" in elem.classes:
            if doc.get_metadata("rmnote", False):
                pf.debug("remove <div class=\"rmnote\"> ~ </div>")
                ret = []
            else:
                ret = elem
            # pf.debug(doc.get_metadata("rmnote", False))

            return ret


def main(doc=None):
    rn = RemovalNotes()
    return pf.run_filter(rn.action, doc=doc)


if __name__ == "__main__":
    main()
