from ga4gh.search.compliance.tests.test_group import TestGroup
from ga4gh.search.compliance.tests.test_case import TestCase
from ga4gh.search.compliance.report.test_case_report import TestCaseReport
from ga4gh.search.compliance.tests.methods.api_test import api_test
from ga4gh.search.compliance.util.function_binder import FunctionBinder

class TestGroupServiceInfo(TestGroup):
    
    def __init__(self, server_config):
        super(TestGroupServiceInfo, self).__init__(server_config)
        self.set_name("Service Info")
        for test_case in SERVICE_INFO_TEST_CASES:
            self.add_test_case(test_case)

SERVICE_INFO_TEST_CASES = [
    TestCase(
        "Test Service Info",
        "Tests the /service-info endpoint",
        FunctionBinder.bind(
            api_test,
            "/service-info",
            {},
            200,
            None
        )
    )
]