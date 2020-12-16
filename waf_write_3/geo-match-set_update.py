#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/update-geo-match-set.html
if __name__ == '__main__':
    """
	create-geo-match-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/create-geo-match-set.html
	delete-geo-match-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/delete-geo-match-set.html
	get-geo-match-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/get-geo-match-set.html
	list-geo-match-sets : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/list-geo-match-sets.html
    """

    parameter_display_string = """
    # geo-match-set-id : The GeoMatchSetId of the  GeoMatchSet that you want to update. GeoMatchSetId is returned by  CreateGeoMatchSet and by  ListGeoMatchSets .
    # change-token : The value returned by the most recent call to  GetChangeToken .
    # updates : An array of GeoMatchSetUpdate objects that you want to insert into or delete from an  GeoMatchSet . For more information, see the applicable data types:

GeoMatchSetUpdate : Contains Action and GeoMatchConstraint
GeoMatchConstraint : Contains Type and Value   You can have only one Type and Value per GeoMatchConstraint . To add multiple countries, include multiple GeoMatchSetUpdate objects in your request.

(structure)


Note
This is AWS WAF Classic documentation. For more information, see AWS WAF Classic in the developer guide.

For the latest version of AWS WAF , use the AWS WAFV2 API and see the AWS WAF Developer Guide . With the latest version, AWS WAF has a single set of endpoints for regional and global use.


Specifies the type of update to perform to an  GeoMatchSet with  UpdateGeoMatchSet .
Action -> (string)

Specifies whether to insert or delete a country with  UpdateGeoMatchSet .

GeoMatchConstraint -> (structure)

The country from which web requests originate that you want AWS WAF to search for.
Type -> (string)

The type of geographical area you want AWS WAF to search for. Currently Country is the only valid value.

Value -> (string)

The country that you want AWS WAF to search for.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("waf", "update-geo-match-set", "geo-match-set-id", "change-token", "updates", add_option_dict)
