# encoding:utf-8

"""Base channel module for CowAgent.

Defines the abstract Channel class that all communication channels
(WeChat, Telegram, etc.) must implement.
"""

from abc import ABC, abstractmethod
from typing import Any, Optional


class Channel(ABC):
    """Abstract base class for all communication channels.

    A channel represents a messaging platform (e.g., WeChat, Telegram)
    through which the agent receives and sends messages.
    """

    channel_type: str = ""

    def __init__(self):
        """Initialize the channel."""
        self.handlers = {}

    @abstractmethod
    def startup(self):
        """Start the channel and begin listening for messages.

        This method should block or set up the necessary listeners
        to receive incoming messages from the platform.
        """
        raise NotImplementedError

    def handle_text(self, msg: Any) -> Optional[str]:
        """Handle an incoming text message.

        Args:
            msg: The incoming message object from the platform.

        Returns:
            The reply string, or None if no reply is needed.
        """
        raise NotImplementedError

    def handle_image(self, msg: Any) -> Optional[str]:
        """Handle an incoming image message.

        Args:
            msg: The incoming message object containing image data.

        Returns:
            The reply string, or None if no reply is needed.
        """
        raise NotImplementedError

    def handle_voice(self, msg: Any) -> Optional[str]:
        """Handle an incoming voice message.

        Args:
            msg: The incoming message object containing voice data.

        Returns:
            The reply string, or None if no reply is needed.
        """
        raise NotImplementedError

    def send(self, reply: Any, context: Any):
        """Send a reply back through the channel.

        Args:
            reply: The reply object to send.
            context: The context of the original message, used to
                     determine where to send the reply.
        """
        raise NotImplementedError

    def build_reply_content(self, query: str, context: Any) -> Any:
        """Build a reply for a given query using the configured bot.

        Args:
            query: The user's input query string.
            context: Additional context for generating the reply.

        Returns:
            A reply object containing the generated response.
        """
        from bot.bot_factory import create_bot
        from config import Config

        bot_type = Config().get("bot_type", "openai")
        bot = create_bot(bot_type)
        return bot.reply(query, context)

    def __str__(self):
        return f"Channel(type={self.channel_type})"
