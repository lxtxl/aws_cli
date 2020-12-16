#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/customer-profiles/search-profiles.html
if __name__ == '__main__':
    """
	create-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/customer-profiles/create-profile.html
	delete-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/customer-profiles/delete-profile.html
	update-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/customer-profiles/update-profile.html
    """

    parameter_display_string = """
    # domain-name : The unique name of the domain.
    # key-name : A searchable identifier of a customer profile. The predefined keys you can use to search include: _account, _profileId, _fullName, _phone, _email, _ctrContactId, _marketoLeadId, _salesforceAccountId, _salesforceContactId, _zendeskUserId, _zendeskExternalId, _serviceNowSystemId.
    # values : A list of key values.
(string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("customer-profiles", "search-profiles", "domain-name", "key-name", "values", add_option_dict)
