import click
from ga4gh.search.compliance.cli.report import report_handler

@click.group()
def main():
    """"""

@main.command(help='Run GA4GH Search compliance tests against a web service')
@click.option('--config-file', '-c',
              help='path to user config yaml file')
@click.option('--output-dir', '-o', default='ga4gh-search-compliance-results', 
              help='report/web archive output directory')
@click.option('--serve', '-s', is_flag=True,
              help='if true, start a local server for viewing report')
@click.option('--force', '-f', is_flag=True, 
              help='if true, force overwrite of output directory')
def report(**kwargs):
    """"""

    report_handler(kwargs)
