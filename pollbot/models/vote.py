"""The sqlalchemy model for a vote."""
from sqlalchemy import (
    Column,
    func,
    ForeignKey,
)
from sqlalchemy.types import (
    BigInteger,
    DateTime,
    Integer,
    String,
)
from sqlalchemy.orm import relationship

from pollbot.db import base


class Vote(base):
    """The model for a Vote."""

    __tablename__ = 'vote'

    id = Column(Integer, primary_key=True)
    type = Column(String)
    index = Column(Integer)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now(), nullable=False)

    # ManyToOne
    poll_option_id = Column(Integer, ForeignKey('poll_option.id', ondelete='cascade'), nullable=False, index=True)
    poll_option = relationship('PollOption')

    poll_id = Column(Integer, ForeignKey('poll.id', ondelete='cascade'), nullable=False, index=True)
    poll = relationship('Poll')

    user_id = Column(BigInteger, ForeignKey('user.id', ondelete='cascade'), nullable=False, index=True)
    user = relationship('User')

    def __init__(self, vote_id, vote_type, index, user, poll_option):
        """Create a new vote."""
        self.id = vote_id
        self.type = vote_type
        self.index = index
        self.user = user
        self.poll_option = poll_option
        self.poll = poll_option.poll