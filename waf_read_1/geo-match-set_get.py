#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/get-geo-match-set.html
if __name__ == '__main__':
    """
	create-geo-match-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/create-geo-match-set.html
	delete-geo-match-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/delete-geo-match-set.html
	list-geo-match-sets : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/list-geo-match-sets.html
	update-geo-match-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/update-geo-match-set.html
    """

    parameter_display_string = """
    # geo-match-set-id : The GeoMatchSetId of the  GeoMatchSet that you want to get. GeoMatchSetId is returned by  CreateGeoMatchSet and by  ListGeoMatchSets .
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

    execute_one_parameter("waf", "get-geo-match-set", "geo-match-set-id", add_option_dict)