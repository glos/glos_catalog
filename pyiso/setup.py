from setuptools import setup, find_packages, Command

files = ["pyiso/*"]
readme = open('../README.md', 'rb').read()
reqs = [line.strip() for line in open('requirements.txt')]

class PyTest(Command):
    user_options = []
    def initialize_options(self):
        pass
    def finalize_options(self):
        pass
    def run(self):
        import sys,subprocess
        errno = subprocess.call([sys.executable, 'runtests.py'])
        raise SystemExit(errno)

setup(
    name                = "pyiso",
    version             = "0.0.1",
    description         = "A Python utility to manage glos isos",
    long_description    = readme,
    license             = '',
    author              = "Sean Cowan",
    author_email        = "scowan@sasascience.com",
    url                 = "https://github.com/asascience-open/glos_catalog",
    packages            = find_packages(),
    cmdclass            = {'test': PyTest},
    install_requires    = reqs,
    classifiers         = [
            'Development Status :: 3 - Alpha',
            'Intended Audience :: Developers',
            'Intended Audience :: Science/Research',
            'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
            'Operating System :: POSIX :: Linux',
            'Programming Language :: Python',
            'Topic :: Scientific/Engineering',
        ],
    include_package_data = True,
) 
