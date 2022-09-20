"""Look inside .twb and .twbx files :)"""
from bs4 import BeautifulSoup
import zipfile
import tempfile
import os
from typing import List, Union
from dataclasses import dataclass


class Workbook:
    def __init__(self, file: str):
        self.soup = self.open_and_parse(file)

    @staticmethod
    def read_twb_text(fp: str):
        """
        Reads the contents of the .twb file as text.

        Params:
        -------
            fp (str): filepath to the .twb file

        Returns:
        --------
            str: The text contents of the .twb file.
        """
        with open(fp, "r") as fileobj:
            text = fileobj.read()
        return text

    @staticmethod
    def read_twbx_text(fp: str):
        """
        Reads the contents of the .twb file zipped inside a .twbx file as text.

        Params:
        -------
            fp (str): filepath to the .twbx file

        Returns:
        --------
            str: The text contents of the .twb file zipped inside.
        """
        # create a temp file for the unzip
        temp_dir = tempfile.mkdtemp(prefix="tableau_xray")

        with zipfile.ZipFile(fp, "r") as zip_ref:

            # take the first .twb file (unknown if there could be multiple)
            twb_files = filter(lambda s: s.endswith(".twb"), zip_ref.namelist())
            first_twb_file = next(twb_files)

            # unzip .twb file to the temp dir
            twb_unzip_path = zip_ref.extract(first_twb_file, temp_dir)

            # read the .twb file
            text = Workbook.read_twb_text(twb_unzip_path)

            # delete the temp files
            os.remove(twb_unzip_path)
            os.rmdir(temp_dir)

            return text

    @staticmethod
    def open_and_parse(file: str):
        """
        Parses .twb, .twbx and file content with Beautifulsoup.

        Params:
        -------
            file (str): the contents of an XML file or the path to a .twb or .twbx file.

        Returns:
        --------
            BeautifulSoup: The BS4 XML Soup Object
        """
        # assume is text by default
        text = file

        # if it's a .twb file
        if os.path.isfile(file) and file.endswith(".twb"):
            text = Workbook.read_twb_text(file)

        # if it's a .twbx file
        elif os.path.isfile(file) and file.endswith(".twbx"):
            text = Workbook.read_twbx_text(file)

        return BeautifulSoup(text, "xml")

