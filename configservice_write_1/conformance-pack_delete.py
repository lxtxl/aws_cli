#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/delete-conformance-pack.html
if __name__ == '__main__':
    """
	describe-conformance-packs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/describe-conformance-packs.html
	put-conformance-pack : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/put-conformance-pack.html
    """

    parameter_display_string = """
    # conformance-pack-name : Name of the conformance pack you want to delete.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("configservice", "delete-conformance-pack", "conformance-pack-name", add_option_dict)





