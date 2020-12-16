#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/groundstation/list-contacts.html
if __name__ == '__main__':
    """
	cancel-contact : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/groundstation/cancel-contact.html
	describe-contact : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/groundstation/describe-contact.html
	reserve-contact : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/groundstation/reserve-contact.html
    """

    parameter_display_string = """
    # end-time : 
    # start-time : The time of the first backup in ISO format.
e.g. 2014-04-21T05:26:10Z. Default is now.
    """

    execute_two_parameter("groundstation", "list-contacts", "end-time", "start-time", parameter_display_string)