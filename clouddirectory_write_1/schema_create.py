#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/clouddirectory/create-schema.html
if __name__ == '__main__':
    """
	apply-schema : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/clouddirectory/apply-schema.html
	delete-schema : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/clouddirectory/delete-schema.html
	publish-schema : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/clouddirectory/publish-schema.html
	update-schema : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/clouddirectory/update-schema.html
    """

    parameter_display_string = """
    # name : The name that is associated with the schema. This is unique to each account and in each region.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("clouddirectory", "create-schema", "name", add_option_dict)





