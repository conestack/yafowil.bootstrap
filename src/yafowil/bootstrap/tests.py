import unittest
import doctest 
from pprint import pprint
from interlude import interact
from yafowil.tests import pxml

optionflags = doctest.NORMALIZE_WHITESPACE | \
              doctest.ELLIPSIS | \
              doctest.REPORT_ONLY_FIRST_FAILURE

TESTFILES = [
    'common.rst',
]

def test_suite():
    return unittest.TestSuite([
        doctest.DocFileSuite(
            file, 
            optionflags=optionflags,
            globs={'interact': interact,
                   'pprint': pprint,
                   'pxml': pxml},
        ) for file in TESTFILES
    ])

if __name__ == '__main__':                                   #pragma NO COVERAGE
    unittest.main(defaultTest='test_suite')                  #pragma NO COVERAGE