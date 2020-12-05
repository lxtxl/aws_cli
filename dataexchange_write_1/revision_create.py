#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dataexchange/create-revision.html
if __name__ == '__main__':
    """
	delete-revision : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dataexchange/delete-revision.html
	get-revision : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dataexchange/get-revision.html
	update-revision : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dataexchange/update-revision.html
    """

    parameter_display_string = """
    # data-set-id : The unique identifier for a data set.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("dataexchange", "create-revision", "data-set-id", add_option_dict)





