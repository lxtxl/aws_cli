#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/list-inventory-entries.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # instance-id : The instance ID for which you want inventory information.
    # type-name : The type of inventory item for which you want information.
    """

    execute_two_parameter("ssm", "list-inventory-entries", "instance-id", "type-name", parameter_display_string)