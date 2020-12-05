#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/es/update-elasticsearch-domain-config.html
if __name__ == '__main__':
    """
	describe-elasticsearch-domain-config : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/es/describe-elasticsearch-domain-config.html
    """

    parameter_display_string = """
    # domain-name : The name of the Elasticsearch domain that you are updating.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("es", "update-elasticsearch-domain-config", "domain-name", add_option_dict)





