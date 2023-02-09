import re

class StringFunctions:

    @staticmethod
    def search_version_substr(software_name):
        version_substr = re.search(r"\b[0-9]+[.][0-9]+[.][0-9]+[.][0-9]+[.][0-9]+[.][0-9]+", software_name)
        if version_substr is None:
            version_substr = re.search(r"\b[0-9]+[.][0-9]+[.][0-9]+[.][0-9]+[.][0-9]+", software_name)
        if version_substr is None:
            version_substr = re.search(r"\b[0-9]+[.][0-9]+[.][0-9]+[.][0-9]+", software_name)
        if version_substr is None:
            version_substr = re.search(r"\b[0-9]+[.][0-9]+[.][0-9]+", software_name)
        if version_substr is None:
            version_substr = re.search(r"\b[0-9]+[.][0-9]+", software_name)

        version_number = ''
        if version_substr is not None:
            version_number = version_substr.group()

        return version_number

    @staticmethod
    def search_archi_substr(software_name):
        archi_substr = re.search(r"64bit x64", software_name)
        if archi_substr is None:
            archi_substr = re.search(r"x64Bit", software_name)
        if archi_substr is None:
            archi_substr = re.search(r"x64bit", software_name)
        if archi_substr is None:
            archi_substr = re.search(r"64Bit", software_name)
        if archi_substr is None:
            archi_substr = re.search(r"64bit", software_name)
        if archi_substr is None:
            archi_substr = re.search(r"x64", software_name)
        if archi_substr is None:
            archi_substr = re.search(r"64", software_name)

        archi = ""
        if archi_substr is not None:
            archi = archi_substr.group()

        return archi

    @staticmethod
    def del_chars_from_softw_name(software_name):
        software_name = re.sub(r"[()+*.,\-_|${}]", "", software_name)
        software_name = re.sub(r"x64", "", software_name)
        software_name = re.sub(r"64", "", software_name)
        software_name = re.sub(r"x32", "", software_name)
        software_name = re.sub(r"32", "", software_name)
        software_name = re.sub(r"bit", "", software_name)
        software_name = re.sub(r"Bit", "", software_name)
        software_name = re.sub("\s+", " ", software_name)  # Remove spaces.

        return software_name