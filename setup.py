from setuptools import setup, find_packages
import os

version = '1.0.dev0'
shortdesc = 'autosuggest widget for YAFOWIL'
longdesc = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()
longdesc += open(os.path.join(os.path.dirname(__file__), 'HISTORY.rst')).read()
longdesc += open(os.path.join(os.path.dirname(__file__), 'LICENSE.rst')).read()
tests_require = ['yafowil[test]', 'yafowil.webob', 'gunicorn']

setup(
    name='yafowil.widget.autosuggest',
    version=version,
    description=shortdesc,
    long_description=longdesc,
    classifiers=[
        'Environment :: Web Environment',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'License :: OSI Approved :: BSD License',
    ],
    keywords='',
    author='Yafowil Contributors',
    author_email='dev@conestack.org',
    url=u'http://github.com/conestack/yafowil.widget.autosuggest',
    license='Simplified BSD',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    namespace_packages=['yafowil', 'yafowil.widget'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'yafowil',
    ],
    tests_require=tests_require,
    extras_require=dict(
        test=tests_require,
    ),
    test_suite="yafowil.widget.autosuggest.tests.test_suite",
    entry_points="""
    [yafowil.plugin]
    register = yafowil.widget.autosuggest:register
    resourcedir = yafowil.widget.autosuggest:get_resource_dir
    javascripts = yafowil.widget.autosuggest:get_js
    stylesheets = yafowil.widget.autosuggest:get_css
    example = yafowil.widget.autosuggest.example:get_example
    """,
)
