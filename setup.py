from setuptools import setup, find_packages

setup(
    name='cmsplugin_pricelist',
    version='1.0.0',
    packages=find_packages(),
    url='https://github.com/Vizzey/cmsplugin_pricelist',
    license='',
    author='Oleg Kondrashov',
    author_email='',
    description='Pricelist for some project, for Django-CMS 3.x',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    include_package_data=True,
    zip_safe=False,
)