from ga4gh.search.compliance.tests.test_group import TestGroup

class TestGroupSearch(TestGroup):

    def __init__(self, server_config):
        super(TestGroupSearch, self).__init__(server_config)
        self.set_name("Search")
        for test_case in SEARCH_TEST_CASES:
            self.add_test_case(test_case)

SEARCH_TEST_CASES = [

]