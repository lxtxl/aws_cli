#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-crawler : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/create-crawler.html
	delete-crawler : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/delete-crawler.html
	get-crawler : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-crawler.html
	get-crawlers : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-crawlers.html
	list-crawlers : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/list-crawlers.html
	start-crawler : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/start-crawler.html
	update-crawler : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/update-crawler.html
    """

    write_parameter("glue", "stop-crawler")