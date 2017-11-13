from setuptools import find_packages
from setuptools import setup
import os


version = '1.3.1'
shortdesc = 'Bootstrap Styles for YAFOWIL'
longdesc = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()
longdesc += open(os.path.join(os.path.dirname(__file__), 'HISTORY.rst')).read()
longdesc += open(os.path.join(os.path.dirname(__file__), 'LICENSE.rst')).read()
tests_require = ['yafowil[test]']


setup(
    name='yafowil.bootstrap',
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
    author='BlueDynamics Alliance',
    author_email='dev@bluedynamics.com',
    url=u'https://github.com/bluedynamics/yafowil.bootstrap',
    license='Simplified BSD',
    packages=find_packages('src'),
    package_dir = {'': 'src'},
    namespace_packages=['yafowil'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'yafowil>1.99',
    ],
    tests_require=tests_require,
    extras_require = dict(
        test=tests_require,
    ),
    test_suite="yafowil.bootstrap.tests.test_suite",
    entry_points="""
    [yafowil.plugin]
    register = yafowil.bootstrap:register
    configure = yafowil.bootstrap:configure
    """)
