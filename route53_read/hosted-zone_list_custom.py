#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter_custom

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/list-hosted-zones.html
if __name__ == '__main__':
    """
	create-hosted-zone : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/create-hosted-zone.html
	delete-hosted-zone : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/delete-hosted-zone.html
	get-hosted-zone : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/get-hosted-zone.html
    """

    parameter_num = len(sys.argv)

    if parameter_num != 3:
        print("config value is not exist")
        print("Usage: python {} <config> <template>".format(sys.argv[0]))
        sys.exit(1)

    profile_name = sys.argv[1]
    template_name = sys.argv[2]

    if template_name == "base":
        output_name = "table"
        query_name = """\"
            HostedZones[*]. [
                Id,
                Name,
                Config.PrivateZone
            ]
        \""""
    elif template_name == "uid":
        output_name = "text"
        query_name = """\"
        \""""
    else:
        print("Usage : {} template name is not exist".format(template_name))
        print("Support template : base, uid")
        sys.exit(1)

    change_query_name = query_name.replace("\n", "")
    change_query_name = change_query_name.replace(" ", "")

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    #######################################################################
    # custom parameter
    add_option_dict["output"] = output_name
    add_option_dict["query"] = change_query_name
    read_no_parameter_custom("route53", "list-hosted-zones", add_option_dict)
