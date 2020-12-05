#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/disassociate-member.html
if __name__ == '__main__':
    """
	create-member : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/create-member.html
	delete-member : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/delete-member.html
	get-member : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/get-member.html
	list-members : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/list-members.html
    """

    parameter_display_string = """
    # id : The unique identifier for the Amazon Macie resource or account that the request applies to.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("macie2", "disassociate-member", "id", add_option_dict)





