from distutils.core import setup

REQUIRES = [
    'requests',
    'structlog',
    'curlify',
    'allure-pytest'
]

setup(
    name='restclient',
    version='0.0.1',
    packages=['restclient'],
    url='https://github.com/zakharovyn/restclient.git',
    license='MIT',
    author='yanzakharov',
    author_email='-',
    install_requires=REQUIRES,
    description='restclient with allure and logger'
)
