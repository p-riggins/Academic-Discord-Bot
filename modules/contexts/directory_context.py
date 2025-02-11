import os
import requests
from dotenv import load_dotenv
from modules.contexts.context import Context
from requests.exceptions import HTTPError, ConnectionError
from modules.classifiers.common.intentclassifier import IntentClassifier
from modules.exceptions import URLUndefinedException, PreconditionException, ServiceUnavailableException, DirectoryNotFoundException
from modules.contexts.directory_entry import DirectoryEntry


class DirectoryContext(Context):
    def __init__(self, name: str, classifier: IntentClassifier):
        super().__init__(name, classifier)
        self.__entries: list = []
        self.__query: str = None

    @property
    def entries(self) -> list:
        return self.__entries

    @entries.setter
    def entries(self, value: list) -> None:
        self.__entries = value

    @property
    def query(self) -> str:
        return self.__query

    @query.setter
    def query(self, value: str) -> None:
        self.__query = value

    def get_directory_info(self):
        load_dotenv('.env')
        base_uri = os.getenv('DIRECTORY_SERVICE_URI')
        apikey = os.getenv("DIRECTORY_API_KEY")
        full_uri = "{}apiKey={}&searchCriteria={}".format(base_uri, apikey, self.query)

        if self.query is None:
            raise PreconditionException("No parameters")

        try:
            r = requests.get(full_uri)
            r.raise_for_status()
            data = r.json()
            if not data:
                raise DirectoryNotFoundException("Directory doesn't exist")
            for entry in data:
                self.entries.append(DirectoryEntry(entry))
        except HTTPError as ex:
            print("Error!" + " " + ex)
        except ConnectionError:
            print("Connection Error!")
            raise ServiceUnavailableException("Unstable Connection")
        except TypeError:
            raise DirectoryNotFoundException("Directory doesn't exist")
        except requests.exceptions.MissingSchema:
            raise URLUndefinedException('Bad or missing URL')

    def __str__(self):
        for py in self.__entries:
            return str(py)
