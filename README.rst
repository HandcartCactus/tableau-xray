===============================
tableau_xray
===============================


.. image:: https://img.shields.io/travis/Ejjaffe/tableau-xray.svg
        :target: https://travis-ci.org/Ejjaffe/tableau-xray
.. image:: https://circleci.com/gh/Ejjaffe/tableau-xray.svg?style=svg
    :target: https://circleci.com/gh/Ejjaffe/tableau-xray
.. image:: https://codecov.io/gh/Ejjaffe/tableau-xray/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/Ejjaffe/tableau-xray


Tableau Xray was going to be a high-level parser for a tableau workbook. Under the hood, a tableau workbook is usually just an XML file, and it might be in a zipfile with the ``.hyper`` file. So this library opens the tableau workbook for you however it is stored and and loads the file into an XML parser. At first I wanted to make a high-level parser for the XML structure, but then I discovered the official `TableauServerClient <https://tableau.github.io/server-client-python/>`_, which ended up meeting my needs. I recommend using that, if you can. Feel free to fork this for your own needs though.


.. code-block:: python

        from tableau_xray import Workbook

        bs4_object = Worbook.open_and_parse("[THE XML CONTENTS HERE AS A STRING]")
        
        # or
        
        bs4_object = Worbook.open_and_parse("[A PATH TO A .TWB OR .TWBX FILE]")


If the file is a ``.twbx`` file, I call ``tempfile.mkdtemp`` to create a library to unzip the file to. It doesn't delete itself once the script is done running, in case you wanted to use the unzipped contents in other ways.
