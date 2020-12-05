#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/update-thing.html
if __name__ == '__main__':
    """
	create-thing : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/create-thing.html
	delete-thing : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/delete-thing.html
	describe-thing : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/describe-thing.html
	list-things : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-things.html
	register-thing : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/register-thing.html
    """

    parameter_display_string = """
    # thing-name : The name of the thing to update.
You canât change a thingâs name. To change a thingâs name, you must create a new thing, give it the new name, and then delete the old thing.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("iot", "update-thing", "thing-name", add_option_dict)





