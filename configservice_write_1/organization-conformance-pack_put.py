#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/put-organization-conformance-pack.html
if __name__ == '__main__':
    """
	delete-organization-conformance-pack : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/delete-organization-conformance-pack.html
	describe-organization-conformance-packs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/describe-organization-conformance-packs.html
    """

    parameter_display_string = """
    # organization-conformance-pack-name : Name of the organization conformance pack you want to create.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("configservice", "put-organization-conformance-pack", "organization-conformance-pack-name", add_option_dict)





