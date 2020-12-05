#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/delete-matchmaking-rule-set.html
if __name__ == '__main__':
    """
	create-matchmaking-rule-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/create-matchmaking-rule-set.html
	describe-matchmaking-rule-sets : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/describe-matchmaking-rule-sets.html
	validate-matchmaking-rule-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/validate-matchmaking-rule-set.html
    """

    parameter_display_string = """
    # name : A unique identifier for a matchmaking rule set to be deleted. (Note: The rule set name is different from the optional ânameâ field in the rule set body.) You can use either the rule set name or ARN value.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("gamelift", "delete-matchmaking-rule-set", "name", add_option_dict)





