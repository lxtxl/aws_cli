#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/list-organization-portfolio-access.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # portfolio-id : The portfolio identifier. For example, port-2abcdext3y5fk .
    # organization-node-type : The organization node type that will be returned in the output.

ORGANIZATION - Organization that has access to the portfolio.
ORGANIZATIONAL_UNIT - Organizational unit that has access to the portfolio within your organization.
ACCOUNT - Account that has access to the portfolio within your organization.

Possible values:

ORGANIZATION
ORGANIZATIONAL_UNIT
ACCOUNT
    """

    execute_two_parameter("servicecatalog", "list-organization-portfolio-access", "portfolio-id", "organization-node-type", parameter_display_string)