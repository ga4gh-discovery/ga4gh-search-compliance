from ga4gh.search.compliance.tests.test_group import TestGroup

class TestGroupTables(TestGroup):

    def __init__(self, server_config):
        super(TestGroupTables, self).__init__(server_config)
        self.set_name("Tables")
        for test_case in TABLES_TEST_CASES:
            self.add_test_case(test_case)

TABLES_TEST_CASES = [

]
