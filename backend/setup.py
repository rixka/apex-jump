from setuptools import find_packages, setup

setup(
    name='apex-jump',
    version='0.0.0',

    description='Apex-Jump integration with DynamoDB',
    long_description=open('../README.md').read(),

    packages=find_packages(exclude=['tests']),

    install_requires=[
      'pynamodb',
      'jsonschema',
      'pyyaml'
    ],
    setup_requires=[
      'pytest-runner'
    ],
    tests_require=[
        'pytest'
    ]
)
