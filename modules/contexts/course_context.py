import os
import requests
from dotenv import load_dotenv
from modules.contexts.context import Context
from requests.exceptions import HTTPError, ConnectionError, MissingSchema, InvalidURL, InvalidSchema
from modules.classifiers.common.intentclassifier import IntentClassifier
from modules.exceptions import URLUndefinedException, CourseNotFoundException, PreconditionException, ServiceUnavailableException

class CourseContext(Context):
    def __init__(self, name: str, classifier: IntentClassifier):
        super().__init__(name, classifier)
        self.__subject: str = None
        self.__course: str = None
        self.__description: str = None
        self.__title: str = None
        self.__prerequisites: list = []

    @property
    def subject(self) -> str:
        return self.__subject

    @subject.setter
    def subject(self, value: str) -> None:
        self.__subject = value

    @property
    def course(self) -> str:
        return self.__course

    @course.setter
    def course(self, value: str) -> None:
        self.__course = value

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, value: str) -> None:
        self.__description = value

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, value: str) -> None:
        self.__title = value

    @property
    def prerequisites(self) -> list:
        return self.__prerequisites

    @prerequisites.setter
    def prerequisites(self, value: list) -> None:
        self.__prerequisites = value

    def get_course_info(self) -> None:
        load_dotenv('.env')
        base_uri = os.getenv('COURSE_SERVICE_URI')
        full_uri = "{}?subject={}&number={}&term={}".format(base_uri, self.subject, self.course, "202280")

        if self.subject is None or self.course is None:
            raise PreconditionException("No parameters were given")

        try:
            r = requests.get(full_uri)
            r.raise_for_status()
            data = r.json()
            self.__subject = data["attribute"]["subject"]
            self.__course = data["attribute"]["number"]
            self.__description = data["attribute"]["description"]
            self.__title = data["attribute"]["title"]
        except HTTPError as ex:
            print("Error!" + " " + str(ex))
            raise PreconditionException("No parameters were given")
        except ConnectionError as ce:
            print("Connection Error! " + str(ce.args[0]))
            raise ServiceUnavailableException('Bad or Unstable Connection')
        except InvalidURL:
            raise URLUndefinedException('Bad or missing URL')
        except TypeError:
            raise CourseNotFoundException("Course doesn't exist")
        except InvalidSchema:
            raise InvalidURL("Bad or missing URL")

    def __str__(self) -> str:
        return "{} {}\n{}\nPrerequisites: {}".format(self.__subject, self.__course, self.__title, self.__description)

