#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/put-configuration-aggregator.html
if __name__ == '__main__':
    """
	delete-configuration-aggregator : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/delete-configuration-aggregator.html
	describe-configuration-aggregators : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/describe-configuration-aggregators.html
    """

    parameter_display_string = """
    # configuration-aggregator-name : The name of the configuration aggregator.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("configservice", "put-configuration-aggregator", "configuration-aggregator-name", add_option_dict)





