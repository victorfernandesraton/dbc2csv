from setuptools import setup

# Define the setup parameters
setup(
    name='dbc2csv',
    version='0.1',
    description='convert dbc to dbf and csv files with recursion',
    package_data={
        'dbc2csv': ['bin/blasd-dbf']
    },
    packages=['dbc2csv']
)
