#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/update-regex-pattern-set.html
if __name__ == '__main__':
    """
	create-regex-pattern-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/create-regex-pattern-set.html
	delete-regex-pattern-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/delete-regex-pattern-set.html
	get-regex-pattern-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/get-regex-pattern-set.html
	list-regex-pattern-sets : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/list-regex-pattern-sets.html
    """

    parameter_display_string = """
    # regex-pattern-set-id : The RegexPatternSetId of the  RegexPatternSet that you want to update. RegexPatternSetId is returned by  CreateRegexPatternSet and by  ListRegexPatternSets .
    # updates : An array of RegexPatternSetUpdate objects that you want to insert into or delete from a  RegexPatternSet .
(structure)


Note
This is AWS WAF Classic documentation. For more information, see AWS WAF Classic in the developer guide.

For the latest version of AWS WAF , use the AWS WAFV2 API and see the AWS WAF Developer Guide . With the latest version, AWS WAF has a single set of endpoints for regional and global use.


In an  UpdateRegexPatternSet request, RegexPatternSetUpdate specifies whether to insert or delete a RegexPatternString and includes the settings for the RegexPatternString .
Action -> (string)

Specifies whether to insert or delete a RegexPatternString .

RegexPatternString -> (string)

Specifies the regular expression (regex) pattern that you want AWS WAF to search for, such as B[a@]dB[o0]t .
    # change-token : The value returned by the most recent call to  GetChangeToken .
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("waf", "update-regex-pattern-set", "regex-pattern-set-id", "updates", "change-token", add_option_dict)
