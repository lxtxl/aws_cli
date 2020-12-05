#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/create-reusable-delegation-set.html
if __name__ == '__main__':
    """
	delete-reusable-delegation-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/delete-reusable-delegation-set.html
	get-reusable-delegation-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/get-reusable-delegation-set.html
	list-reusable-delegation-sets : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/list-reusable-delegation-sets.html
    """

    parameter_display_string = """
    # caller-reference : A unique string that identifies the request, and that allows you to retry failed CreateReusableDelegationSet requests without the risk of executing the operation twice. You must use a unique CallerReference string every time you submit a CreateReusableDelegationSet request. CallerReference can be any unique string, for example a date/time stamp.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("route53", "create-reusable-delegation-set", "caller-reference", add_option_dict)





