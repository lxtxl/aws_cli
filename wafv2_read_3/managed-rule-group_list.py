#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/describe-managed-rule-group.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # vendor-name : The name of the managed rule group vendor. You use this, along with the rule group name, to identify the rule group.
    # name : The name of the managed rule group. You use this, along with the vendor name, to identify the rule group.
    """

    execute_two_parameter("wafv2", "describe-managed-rule-group", "vendor-name", "name", parameter_display_string)