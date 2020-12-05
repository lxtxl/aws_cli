#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/get-ip-set.html
if __name__ == '__main__':
    """
	create-ip-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/create-ip-set.html
	delete-ip-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/delete-ip-set.html
	list-ip-sets : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/list-ip-sets.html
	update-ip-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/update-ip-set.html
    """

    parameter_display_string = """
    # detector-id : The unique ID of the detector that the IPSet is associated with.
    # ip-set-id : The unique ID of the IPSet to retrieve.
    """

    execute_two_parameter("guardduty", "get-ip-set", "detector-id", "ip-set-id", parameter_display_string)