from dataclasses import dataclass
from typing import Any, Union


@dataclass
class PrevTask:
    key: str = ""
    title: str = ""
    country: str = ""
    executor: Union[str, None] = ""
    contact: str = ""
    status: str = ""
    solution: str = ""
    priority: str = ""
    number: str = ""
    description: str = ""


@dataclass
class Priority:
    self: str
    iconUrl: str
    name: str
    id: str

    @staticmethod
    def from_dict(obj: Any) -> 'Priority':
        _self = str(obj.get("self"))
        _iconUrl = str(obj.get("iconUrl"))
        _name = str(obj.get("name"))
        _id = str(obj.get("id"))
        return Priority(_self, _iconUrl, _name, _id)


@dataclass
class Creator:
    self: str
    name: str
    key: str
    emailAddress: str
    displayName: str
    active: bool
    timeZone: str

    @staticmethod
    def from_dict(obj: Any) -> 'Creator':
        _self = str(obj.get("self"))
        _name = str(obj.get("name"))
        _key = str(obj.get("key"))
        _emailAddress = str(obj.get("emailAddress"))

        _displayName = str(obj.get("displayName"))
        _active = bool(obj.get('active'))
        _timeZone = str(obj.get("timeZone"))
        return Creator(_self, _name, _key, _emailAddress, _displayName, _active, _timeZone)


@dataclass
class Links:
    self: str

    @staticmethod
    def from_dict(obj: Any) -> 'Links':
        _self = str(obj.get("self"))
        return Links(_self)


@dataclass
class Country:
    id: str
    name: str
    _links: Links

    @staticmethod
    def from_dict(obj: Any) -> 'Country':
        _id = str(obj.get("id"))
        _name = str(obj.get("name"))
        __links = Links.from_dict(obj.get("_links"))
        return Country(_id, _name, __links)


@dataclass
class StatusCategory:
    self: str
    id: int
    key: str
    colorName: str
    name: str

    @staticmethod
    def from_dict(obj: Any) -> 'StatusCategory':
        _self = str(obj.get("self"))
        _id = int(obj.get("id"))
        _key = str(obj.get("key"))
        _colorName = str(obj.get("colorName"))
        _name = str(obj.get("name"))
        return StatusCategory(_self, _id, _key, _colorName, _name)


@dataclass
class Status:
    self: str
    description: str
    iconUrl: str
    name: str
    id: str
    statusCategory: StatusCategory

    @staticmethod
    def from_dict(obj: Any) -> 'Status':
        _self = str(obj.get("self"))
        _description = str(obj.get("description"))
        _iconUrl = str(obj.get("iconUrl"))
        _name = str(obj.get("name"))
        _id = str(obj.get("id"))
        _statusCategory = StatusCategory.from_dict(obj.get("statusCategory"))
        return Status(_self, _description, _iconUrl, _name, _id, _statusCategory)


@dataclass
class Assignee:
    self: str
    name: str
    key: str
    emailAddress: str
    displayName: str
    timeZone: str

    @staticmethod
    def from_dict(obj: Any) -> Union['Assignee', None]:
        try:
            _self = str(obj.get("self"))
            _name = str(obj.get("name"))
            _key = str(obj.get("key"))
            _emailAddress = str(obj.get("emailAddress"))
            _displayName = str(obj.get("displayName"))
            _timeZone = str(obj.get("timeZone"))
            return Assignee(_self, _name, _key, _emailAddress, _displayName, _timeZone)
        except AttributeError as ex:
            return None


@dataclass
class Fields:
    summary: str
    creator: Creator
    description: str
    priority: Priority
    status: Status
    customfield_10002: Country
    assignee: Union[Assignee, None]

    @staticmethod
    def from_dict(obj: Any) -> 'Fields':
        _summary = str(obj.get("summary"))
        _creator = Creator.from_dict(obj.get("creator"))
        _description = str(obj.get("description"))
        _priority = Priority.from_dict(obj.get("priority"))
        _status = Status.from_dict(obj.get("status"))
        try:
            _customfield_10002 = Country.from_dict(obj.get("customfield_10002")[0])
        except IndexError:
            _customfield_10002 = Country('0', '-', Links(''))
        _assignee = Assignee.from_dict(obj.get("assignee"))
        return Fields(_summary, _creator, _description, _priority, _status,
                      _customfield_10002, _assignee)


@dataclass
class Task:
    expand: str
    id: str
    self: str
    key: str
    fields: Fields

    @staticmethod
    def from_dict(obj: Any) -> 'Task':
        _expand = str(obj.get("expand"))
        _id = str(obj.get("id"))
        _self = str(obj.get("self"))
        _key = str(obj.get("key"))
        _fields = Fields.from_dict(obj.get("fields"))
        return Task(_expand, _id, _self, _key, _fields)
