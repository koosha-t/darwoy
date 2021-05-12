from abc import ABC, abstractmethod

class RawDataMiner(ABC):

    """
        RawDataMiner is an abstract class which provides a blue_print for variety of concrete data
        miner classes, each mining raw data from a specific resource (e.g. Twitter, Facebook, Instagram, etc.)
    """

    @abstractmethod
    def getAPIObject(self):
        """
        This abstract method must be implemented in all subclasses.
        This method would use given credentials to make connection to the data source,
        returning an API object which can be used to consume data and any other communications with
        the remote service.

        :return: APIObject
        """
        pass