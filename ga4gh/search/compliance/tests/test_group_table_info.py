from ga4gh.search.compliance.tests.test_group import TestGroup

class TestGroupTableInfo(TestGroup):

    def __init__(self, server_config):
        super(TestGroupTableInfo, self).__init__(server_config)
        self.set_name("Table Info")
        for test_case in TABLE_INFO_TEST_CASES:
            self.add_test_case(test_case)

TABLE_INFO_TEST_CASES = [
    
]