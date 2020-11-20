import requests
from ga4gh.search.compliance.exception.test_method_exception import TestMethodException
from ga4gh.search.compliance.report.test_case_report import TestCaseReport
from ga4gh.search.compliance.util.static_utils import StaticUtils


def api_test(endpoint, query_params, exp_status, exp_schema, server_config, test_case_report):

    try:

        # construct full URL
        url = StaticUtils.remove_trailing_slash(server_config.get_url()) + endpoint
        test_case_report.add_log_message("GET %s" % url)

        # execute HTTP request
        response = requests.get(url)
        if response.status_code != exp_status:
            raise TestMethodException("observed code %s != expected code %s" % (str(response.status_code), str(exp_status)))

        # check that response body matches expected schema
        
        test_case_report.set_status(TestCaseReport.STATUS_PASS)
        test_case_report.set_message("status code matches expected, response body aligns with schema")
    except TestMethodException as e:
        test_case_report.set_status(TestCaseReport.STATUS_FAIL)
        test_case_report.set_message(str(e))
