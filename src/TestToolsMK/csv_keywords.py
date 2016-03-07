#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2015 Cutting Edge QA

import unicodecsv as csv
from robot.libraries import DateTime

from robot_instances import *


class CsvKeywords(object):
    OUTPUT_FILE_CSV = "output.csv"

    def __init__(self, **kwargs):
        super(CsvKeywords, self).__init__(**kwargs)

    def csv_set_output_file(self, file_name=OUTPUT_FILE_CSV):
        self.OUTPUT_FILE_CSV = file_name

    def csv_writer(self, *values):
        """
        Store to default file records in csv
        ${EXECDIR}/Artifacts/output.csv
        change file name using csv change output file
        """

        log_file = get_artifacts_dir() + "/" + self.OUTPUT_FILE_CSV

        with open(log_file, 'ab') as csv_file:
            writer_csv = csv.writer(csv_file, dialect='excel')
            # if os.stat(log_file).st_size < 10:
            # writer_csv.writerow(fieldnames)
            writer_csv.writerow(list(values))

    def csv_writer_with_extra(self, *values):
        """
        Add extra params at begining
        1. time of exection
        2. suite + test cases name
        """
        test_case_name = str(bi().get_variable_value("${TEST_NAME}"))
        suite_name = str(bi().get_variable_value("${SUITE_NAME}"))
        extra_list = list(values)
        extra_list.insert(0, suite_name + test_case_name)
        self.csv_writer_with_time(*extra_list)

    def csv_writer_with_time(self, *values):
        current_time = DateTime.get_current_date(result_format="%Y.%m.%d %H:%M:%S")
        extra_list = list(values)
        extra_list.insert(0, current_time)
        self.csv_writer(*extra_list)