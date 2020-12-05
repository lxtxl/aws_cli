#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ce/get-cost-and-usage-with-resources.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # time-period : 
    # filter : A filter to match for the rules to update. Only rules that match the filter are updated.
key -> (string)
value -> (structure)

The criteria to use in the filter that defines the archive rule.
contains -> (list)

A âcontainsâ operator to match for the filter used to create the rule.
(string)

eq -> (list)

An âequalsâ operator to match for the filter used to create the rule.
(string)

exists -> (boolean)

An âexistsâ operator to match for the filter used to create the rule.

neq -> (list)

A ânot equalsâ operator to match for the filter used to create the rule.
(string)
    """

    execute_two_parameter("ce", "get-cost-and-usage-with-resources", "time-period", "filter", parameter_display_string)