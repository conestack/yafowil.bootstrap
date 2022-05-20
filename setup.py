from setuptools import find_packages
from setuptools import setup
import os


def read_file(name):
    with open(os.path.join(os.path.dirname(__file__), name)) as f:
        return f.read()


version = '2.0.0.dev0'
shortdesc = 'Bootstrap Styles for YAFOWIL'
longdesc = '\n\n'.join([read_file(name) for name in [
    'README.rst',
    'CHANGES.rst',
    'LICENSE.rst'
]])


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
    author='Yafowil Contributors',
    author_email='dev@conestack.org',
    url=u'https://github.com/conestack/yafowil.bootstrap',
    license='Simplified BSD',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    namespace_packages=['yafowil'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'webresource',
        'yafowil>2.2.99'
    ],
    entry_points="""
    [yafowil.plugin]
    register = yafowil.bootstrap:register
    """
)
