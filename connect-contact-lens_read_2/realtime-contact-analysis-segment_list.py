#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect-contact-lens/list-realtime-contact-analysis-segments.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # instance-id : The identifier of the Amazon Connect instance.
    # contact-id : The identifier of the contact.
    """

    execute_two_parameter("connect-contact-lens", "list-realtime-contact-analysis-segments", "instance-id", "contact-id", parameter_display_string)