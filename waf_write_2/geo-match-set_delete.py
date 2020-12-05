#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/delete-geo-match-set.html
if __name__ == '__main__':
    """
	create-geo-match-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/create-geo-match-set.html
	get-geo-match-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/get-geo-match-set.html
	list-geo-match-sets : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/list-geo-match-sets.html
	update-geo-match-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/update-geo-match-set.html
    """

    parameter_display_string = """
    # geo-match-set-id : The GeoMatchSetID of the  GeoMatchSet that you want to delete. GeoMatchSetId is returned by  CreateGeoMatchSet and by  ListGeoMatchSets .
    # change-token : The value returned by the most recent call to  GetChangeToken .
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("waf", "delete-geo-match-set", "geo-match-set-id", "change-token", add_option_dict)
