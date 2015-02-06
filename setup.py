from setuptools import setup
try:
    import multiprocessing
except ImportError:
    pass

setup(
    name='httpie-api-auth',
    description='ApiAuth plugin for HTTPie.',
    long_description=open('README.rst').read().strip(),
    version='0.2.0',
    author='Kyle Hargraves',
    author_email='pd@krh.me',
    license='MIT',
    url='https://github.com/pd/httpie-api-auth',
    download_url='https://github.com/pd/httpie-api-auth',
    py_modules=['httpie_api_auth'],
    zip_safe=False,
    entry_points={
        'httpie.plugins.auth.v1': [
            'httpie_api_auth = httpie_api_auth:ApiAuthPlugin'
        ]
    },
    install_requires=[
        'httpie>=0.7.0'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'Environment :: Plugins',
        'License :: OSI Approved :: MIT License',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Utilities'
    ],
)
