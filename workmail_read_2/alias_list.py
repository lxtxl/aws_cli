#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/list-aliases.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # organization-id : The identifier for the organization under which the entity exists.
    # entity-id : The identifier for the entity for which to list the aliases.
    """

    execute_two_parameter("workmail", "list-aliases", "organization-id", "entity-id", parameter_display_string)