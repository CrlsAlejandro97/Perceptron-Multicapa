from distutils.core import setup
import py2exe

import sys; sys.argv.append('py2exe')

py2exe_options = dict(
                      ascii=True,  # Exclude encodings
                      excludes=['_ssl',  # Exclude _ssl
                                'pyreadline', 'difflib', 'doctest', 'locale', 
                                'optparse'],  # Exclude standard library
                      dll_excludes=['msvcr71.dll'],  # Exclude msvcr71
                      compressed=True,  # Compress library.zip
                      )

setup(name='<Name>',
      version='1.0',
      description='<Description>',
      author='Ofer Schwarz',

      windows=[
        {
            "script": "app.py"
        }
    ],
      options={'py2exe': py2exe_options},
      )