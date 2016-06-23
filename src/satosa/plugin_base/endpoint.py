"""
Interfaces for frontend / backend plugins
"""
import logging

from ..backends.base import BackendModule
from ..frontends.base import FrontendModule

logger = logging.getLogger(__name__)


class InterfaceModulePlugin(object):
    """
    Interface for backend/frontend plugins
    """

    def __init__(self, module, name, config):
        """

        :type module: satosa.frontends.base.FrontendModule | satosa.backends.base.BackendModule
        :type name: str
        :type config: Any

        :param module: module class object
        :param name: Name of the plugin
        :param config: configuration for the module
        """
        self.module = module
        self.name = name
        self.config = config


class FrontendModulePlugin(InterfaceModulePlugin):
    """
    Interface for frontend plugins
    """

    def __init__(self, module, receiver, config):
        """

        :type module: satosa.frontends.base.FrontendModule
        :type receiver: str
        :type config: Any

        :param module: module class object
        :param receiver: Name of the frontend
        :param config: configuration for the module
        """
        if not issubclass(module, FrontendModule):
            raise ValueError("module is not subclass of {} (!={})".format(FrontendModule.__name__, type(module).__name__))
        super().__init__(module, receiver, config)


class BackendModulePlugin(InterfaceModulePlugin):
    """
    Interface for backend plugins
    """

    def __init__(self, module, provider, config):
        """

        :type module: satosa.backends.base.BackendModule
        :type provider: str
        :type config: Any

        :param module: module class object
        :param provider: Name of the frontend
        :param config: configuration for the module
        """
        if not issubclass(module, BackendModule):
            raise ValueError("module is not subclass of {} (!={})".format(BackendModule.__name__, type(module).__name__))
        super().__init__(module, provider, config)
