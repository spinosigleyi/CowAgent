# encoding:utf-8
"""
Wechat channel implementation using itchat library.
Handles message receiving and sending for WeChat personal accounts.
"""

import time
import logging
import itchat
from itchat.content import TEXT, VOICE, PICTURE, NOTE
from channel.channel import Channel
from config import Config

logger = logging.getLogger(__name__)


class WechatChannel(Channel):
    """
    WeChat channel implementation.
    Uses itchat to connect to WeChat and handle messages.
    """

    def __init__(self):
        super().__init__()
        self.config = Config()

    def startup(self):
        """Start the WeChat channel by logging in and registering message handlers."""
        logger.info("Starting WeChat channel...")

        # Login to WeChat
        itchat.auto_login(
            enableCmdQR=2,
            hotReload=self.config.get("hot_reload", False),
            exitCallback=self._on_exit
        )

        # Register message handlers
        itchat.msg_register([TEXT], isFriendChat=True, isGroupChat=False)(self._handle_single_text)
        itchat.msg_register([TEXT], isFriendChat=False, isGroupChat=True)(self._handle_group_text)
        itchat.msg_register([VOICE], isFriendChat=True)(self._handle_voice)
        itchat.msg_register([PICTURE], isFriendChat=True)(self._handle_picture)
        itchat.msg_register([NOTE], isFriendChat=True)(self._handle_note)

        logger.info("WeChat channel started successfully")
        itchat.run()

    def _handle_single_text(self, msg):
        """Handle text messages from individual chats."""
        try:
            from_user = msg["FromUserName"]
            to_user = msg["ToUserName"]
            content = msg["Text"]
            sender_name = msg["ActualNickName"] or msg.get("User", {}).get("NickName", "Unknown")

            logger.info(f"Received text from {sender_name}: {content[:50]}")
            reply = self.handle_text(content, from_user, to_user)

            if reply:
                itchat.send(reply, toUserName=from_user)
        except Exception as e:
            logger.error(f"Error handling single text message: {e}")

    def _handle_group_text(self, msg):
        """Handle text messages from group chats."""
        try:
            group_id = msg["FromUserName"]
            content = msg["Text"]
            actual_user = msg.get("ActualUserName", "")
            actual_nick = msg.get("ActualNickName", "Unknown")

            # Check if the bot is mentioned
            bot_name = itchat.instance.storageClass.nickName
            if f"@{bot_name}" not in content:
                return

            # Remove the mention prefix
            content = content.replace(f"@{bot_name}", "").strip()
            logger.info(f"Received group text from {actual_nick} in {group_id}: {content[:50]}")

            reply = self.handle_text(content, actual_user, group_id)
            if reply:
                itchat.send(reply, toUserName=group_id)
        except Exception as e:
            logger.error(f"Error handling group text message: {e}")

    def _handle_voice(self, msg):
        """Handle voice messages."""
        logger.debug("Voice message received, currently not supported")

    def _handle_picture(self, msg):
        """Handle picture messages."""
        try:
            from_user = msg["FromUserName"]
            msg.download(msg.fileName)
            reply = self.handle_image(msg.fileName, from_user)
            if reply:
                itchat.send(reply, toUserName=from_user)
        except Exception as e:
            logger.error(f"Error handling picture message: {e}")

    def _handle_note(self, msg):
        """Handle system note messages (e.g., revoke notifications)."""
        logger.debug(f"Note message received: {msg.get('Content', '')}")

    def _on_exit(self):
        """Callback when WeChat session ends."""
        logger.warning("WeChat session ended")

    def send(self, message: str, receiver: str):
        """Send a text message to a specific user or group."""
        try:
            itchat.send(message, toUserName=receiver)
            logger.info(f"Message sent to {receiver}")
        except Exception as e:
            logger.error(f"Failed to send message to {receiver}: {e}")
