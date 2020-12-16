#!/usr/bin/python


class CrawlingListVo:
    id = 0
    name = ""
    url = ""
    type = ""
    is_analysis = False
    created_at = ""
    updated_at = ""

    def __init__(self, row):
        self.id = int(row[0])
        self.name = row[1]
        self.url = row[2]
        self.type = row[3]
        self.is_analysis = bool(row[4])
        self.created_at = row[5]
        self.updated_at = row[6]

    @classmethod
    def get_select_query(cls):
        return "id, name, url, type, is_analysis, created_at, updated_at"

    def __str__(self):
        return "CrawlingListVo {} => {} {} {}".format(self.id, self.name, self.type, self.url)