from datetime import datetime

from playhouse.postgres_ext import *

from domainaware import db


class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    username = TextField(unique=True)
    email_address = TextField(unique=True)
    name = TextField()
    password = TextField(null=True)
    created_timestamp = DateTimeField(default=datetime.now)
    last_login = DateTimeField(null=True)
    is_admin = BooleanField(default=False)
    enabled = BooleanField(default=True)


class MonitoredDomain(BaseModel):
    name = TextField(unique=True)
    added_by = ForeignKeyField(User, related_name="added_domains")
    added_timestamp = DateTimeField(default=datetime.now)
    last_updated_by = ForeignKeyField(User)
    last_updated_timestamp = DateTimeField(default=datetime.now)
    enabled = BooleanField(default=True)

    def enable(self):
        self.enabled = True
        self.last_updated_timestamp = datetime.now()
        self.save()

    def disable(self):
        self.enabled = False
        self.last_updated_timestamp = datetime.now()
        self.save()


class SuspectDomainCategory(BaseModel):
    name = TextField(unique=True)


class SuspectDomain(BaseModel):
    name = TextField(unique=True)
    discovered_timestamp = DateTimeField(default=datetime.now)
    created_timestamp = DateTimeField(null=True)
    updated_timestamp = DateTimeField(null=True)
    expires_timestamp = DateTimeField(null=True)
    category = ForeignKeyField(SuspectDomainCategory, related_name="domains")
    lookalike_of = ForeignKeyField(MonitoredDomain, related_name="lookalike_domains")
    data = BinaryJSONField()

