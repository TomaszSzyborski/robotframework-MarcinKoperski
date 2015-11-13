import os.path

from Selenium2Library import Selenium2Library
from robot.libraries import DateTime
from robot.libraries.BuiltIn import BuiltIn
from robot.libraries.Collections import Collections
from robot.libraries.OperatingSystem import OperatingSystem

__all__ = ('s2l', 'bi', 'dtl', 'osl', 'cl','get_artifacts_dir')


def get_artifacts_dir(delta_path):
    output_path = bi().get_variable_value("${EXECDIR}")
    output_path += "/Artifacts/"
    output_path += delta_path
    output_dir_normalized = os.path.dirname(os.path.abspath(os.path.normpath(output_path)))
    output_path_normalized = os.path.abspath(os.path.normpath(output_path))
    if not os.path.exists(output_dir_normalized):
        os.makedirs(output_dir_normalized)
    return output_path_normalized

def s2l():
    """

        :rtype : Selenium2Library
        """
    s2l_instance = BuiltIn().get_library_instance('Selenium2Library')
    assert isinstance(s2l_instance, Selenium2Library)
    return s2l_instance


def bi():
    """

        :rtype : BuiltIn
        """
    bi_instance = BuiltIn().get_library_instance('BuiltIn')
    assert isinstance(bi_instance, BuiltIn)
    return bi_instance


def dtl():
    """

        :rtype : DateTime
        """
    dt_instance = BuiltIn().get_library_instance('DateTime')
    assert isinstance(dt_instance, DateTime)
    return dt_instance


def osl():
    """

        :rtype : OperatingSystem
        """
    os_instance = BuiltIn().get_library_instance('OperatingSystem')
    assert isinstance(os_instance, OperatingSystem)
    return os_instance


def cl():
    """

        :rtype : Collections
        """
    c_instance = BuiltIn().get_library_instance('Collections')
    assert isinstance(c_instance, Collections)
    return c_instance