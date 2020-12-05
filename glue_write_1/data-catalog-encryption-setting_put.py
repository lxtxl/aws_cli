#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/put-data-catalog-encryption-settings.html
if __name__ == '__main__':
    """
	get-data-catalog-encryption-settings : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-data-catalog-encryption-settings.html
    """

    parameter_display_string = """
    # data-catalog-encryption-settings : 
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("glue", "put-data-catalog-encryption-settings", "data-catalog-encryption-settings", add_option_dict)





