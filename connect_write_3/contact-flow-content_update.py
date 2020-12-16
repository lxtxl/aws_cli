#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/update-contact-flow-content.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # instance-id : The identifier of the Amazon Connect instance.
    # contact-flow-id : The identifier of the contact flow.
    # content : The JSON string that represents contact flowâs content. For an example, see Example contact flow in Amazon Connect Flow language in the Amazon Connect Administrator Guide .
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("connect", "update-contact-flow-content", "instance-id", "contact-flow-id", "content", add_option_dict)
