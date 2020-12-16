#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/put-schema-version-metadata.html
if __name__ == '__main__':
    """
	query-schema-version-metadata : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/query-schema-version-metadata.html
	remove-schema-version-metadata : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/remove-schema-version-metadata.html
    """

    parameter_display_string = """
    # metadata-key-value : 
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("glue", "put-schema-version-metadata", "metadata-key-value", add_option_dict)





