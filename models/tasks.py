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
class Country:
    self: str
    value: str
    id: str

    @staticmethod
    def from_dict(obj: Any) -> 'Country':
        _self = str(obj.get("self"))
        _value = str(obj.get("value"))
        _id = str(obj.get("id"))
        return Country(_self, _value, _id)


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
    customfield_11611: str
    description: str
    priority: Priority
    customfield_11213: str
    status: Status
    customfield_12838: Country
    assignee: Union[Assignee, None]

    @staticmethod
    def from_dict(obj: Any) -> 'Fields':
        _summary = str(obj.get("summary"))
        _customfield_11611 = str(obj.get("customfield_11611"))
        _description = str(obj.get("description"))
        _priority = Priority.from_dict(obj.get("priority"))
        _customfield_11213 = str(obj.get("customfield_11213"))
        _status = Status.from_dict(obj.get("status"))
        _customfield_12838 = Country.from_dict(obj.get("customfield_12838"))
        _assignee = Assignee.from_dict(obj.get("assignee"))
        return Fields(_summary, _customfield_11611, _description, _priority, _customfield_11213, _status,
                      _customfield_12838, _assignee)


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
