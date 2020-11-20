from ga4gh.search.compliance.tests.test_group_service_info import TestGroupServiceInfo
from ga4gh.search.compliance.tests.test_group_tables import TestGroupTables
from ga4gh.search.compliance.tests.test_group_table_info import TestGroupTableInfo
from ga4gh.search.compliance.tests.test_group_table_data import TestGroupTableData
from ga4gh.search.compliance.tests.test_group_search import TestGroupSearch

ALL_TEST_GROUP_CLS = [
    TestGroupServiceInfo,
    TestGroupTables,
    TestGroupTableInfo,
    TestGroupTableData,
    TestGroupSearch
]