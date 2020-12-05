#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/delete-field-level-encryption-config.html
if __name__ == '__main__':
    """
	create-field-level-encryption-config : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/create-field-level-encryption-config.html
	get-field-level-encryption-config : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/get-field-level-encryption-config.html
	list-field-level-encryption-configs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/list-field-level-encryption-configs.html
	update-field-level-encryption-config : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/update-field-level-encryption-config.html
    """

    parameter_display_string = """
    # id : The ID of the configuration you want to delete from CloudFront.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("cloudfront", "delete-field-level-encryption-config", "id", add_option_dict)





