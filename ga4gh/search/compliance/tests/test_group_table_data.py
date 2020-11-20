from ga4gh.search.compliance.tests.test_group import TestGroup

class TestGroupTableData(TestGroup):

    def __init__(self, server_config):
        super(TestGroupTableData, self).__init__(server_config)
        self.set_name("Table Data")
        for test_case in TABLE_DATA_TEST_CASES:
            self.add_test_case(test_case)

TABLE_DATA_TEST_CASES = [
    
]