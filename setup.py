import setuptools

NAME = "ga4gh-search-compliance"
VERSION = "1.0.0"
AUTHOR = "GA4GH Discovery Work Stream"
EMAIL = "ga4gh-discovery-search@ga4gh.org"

# Work around mbcs bug in distutils.
# http://bugs.python.org/issue10945
import codecs
try:
    codecs.lookup('mbcs')
except LookupError:
    ascii = codecs.lookup('ascii')
    func = lambda name, enc=ascii: {True: enc}.get(name=='mbcs')
    codecs.register(func)

with open("README.md", "r") as fh:
    long_description = fh.read()
install_requires = [
    'requests',
    'click',
    'jsonschema',
    'PyYAML',
    "Jinja2",
    "loompy"
]

setuptools.setup(
    name=NAME,
    version=VERSION,
    author=AUTHOR,
    author_email=EMAIL,
    description="Reports web service compliance to the GA4GH Search API specification",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ga4gh-discovery/ga4gh-search-compliance",
    package_data={
        '': [
            'search/compliance/web/*/*',
        ]
    },
    packages=setuptools.find_packages(),
    install_requires=install_requires,
    entry_points='''
        [console_scripts]
        ga4gh-search-compliance=ga4gh.search.compliance.cli.entrypoint:main
    ''',
    classifiers=(
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Natural Language :: English",
        "Topic :: Scientific/Engineering :: Bio-Informatics"
    ),
)
