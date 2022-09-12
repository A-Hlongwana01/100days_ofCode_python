import unittest
from io import StringIO
from unittest.mock import patch
import sys

# from authenticate_user.signUp import firstName, lastName, userName
from ..import signUp

@patch("sys.stdin",StringIO("Jo2n\nJohn\n"))
def test_invalidFistName(self):
    output = StringIO()
    sys.stdout = output

    signUp.firstName()
    self.assertEquals(output.getvalue(), """
    First name:\t
    Oops!! that is not a valid name \nPlease try again
    """)
