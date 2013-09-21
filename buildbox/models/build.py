from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey

from buildbox.db.base import Base
from buildbox.db.types.guid import GUID


class BuildStatus(object):
    UNKNOWN = 0
    QUEUED = 1
    INPROGRESS = 2
    PASSED = 3
    FAILED = 4


class Build(Base):
    __tablename__ = 'build'

    build_id = Column(GUID, primary_key=True)
    repository_id = Column(GUID, ForeignKey('repository.repository_id'), nullable=False)
    project_id = Column(GUID, ForeignKey('project.project_id'), nullable=False)
    parent_sha = Column(String(40), nullable=False)
    status = Column(Integer, nullable=False, default=0)
    date_started = Column(DateTime)
    date_finished = Column(DateTime)
    date_created = Column(DateTime, default=datetime.utcnow)
