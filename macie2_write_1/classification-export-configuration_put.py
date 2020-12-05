#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/put-classification-export-configuration.html
if __name__ == '__main__':
    """
	get-classification-export-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/get-classification-export-configuration.html
    """

    parameter_display_string = """
    # configuration : Crawler configuration information. This versioned JSON string allows users to specify aspects of a crawlerâs behavior. For more information, see Configuring a Crawler .
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("macie2", "put-classification-export-configuration", "configuration", add_option_dict)





