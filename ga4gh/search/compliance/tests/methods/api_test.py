import requests
from ga4gh.search.compliance.exception.test_method_exception import TestMethodException
from ga4gh.search.compliance.report.test_case_report import TestCaseReport
from ga4gh.search.compliance.util.static_utils import StaticUtils
from ga4gh.search.compliance.util.schema_validator import SchemaValidator

def api_test(endpoint, query_params, exp_status, schema_url, req_prop_vals, server_config, test_case_report):

    try:

        # construct full URL
        url = StaticUtils.remove_trailing_slash(server_config.get_url()) + endpoint
        test_case_report.add_log_message("GET %s" % url)

        # execute HTTP request
        response = requests.get(url)
        if response.status_code != exp_status:
            raise TestMethodException("observed code %s != expected code %s" % (str(response.status_code), str(exp_status)))

        # check that response body matches expected schema
        response_dict = response.json()
        schema_validator = SchemaValidator(schema_url)
        schema_validator.load_schema()
        schema_validator.validate_instance(response_dict)

        # custom validation of individual properties
        for prop, exp_val in req_prop_vals:
            obs_val = response_dict
            for key in prop.split("."):
                obs_val = obs_val[key]
            if obs_val != exp_val:
                raise TestMethodException("property %s MUST be %s, was %s" % (prop, exp_val, obs_val))

        test_case_report.set_status(TestCaseReport.STATUS_PASS)
        test_case_report.set_message("status code matches expected, response body aligns with schema")
    except TestMethodException as e:
        test_case_report.set_status(TestCaseReport.STATUS_FAIL)
        test_case_report.set_message(str(e))
