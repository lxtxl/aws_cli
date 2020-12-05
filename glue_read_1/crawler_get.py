#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-crawler.html
if __name__ == '__main__':
    """
	create-crawler : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/create-crawler.html
	delete-crawler : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/delete-crawler.html
	get-crawlers : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-crawlers.html
	list-crawlers : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/list-crawlers.html
	start-crawler : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/start-crawler.html
	stop-crawler : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/stop-crawler.html
	update-crawler : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/update-crawler.html
    """

    parameter_display_string = """
    # name : The name of the crawler to retrieve metadata for.
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string

    execute_one_parameter("glue", "get-crawler", "name", add_option_dict)