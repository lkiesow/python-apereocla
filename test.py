#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import apereocla

if __name__ == '__main__':
    assert 'lkiesow' in apereocla.github_users()
    assert 'Lars Kiesow' in apereocla.icla()
    assert 'ELAN e.V.' in apereocla.ccla()
    # check non-existing cla
    assert 'not-lkiesow' not in apereocla.github_users()
