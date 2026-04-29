# -*- coding: utf-8 -*-
"""
CowAgent - Main entry point
A fork of zhayujie/chatgpt-on-wechat with extended capabilities.
"""

import sys
import signal
import logging
from config import load_config, conf

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)


def sigterm_handler(signum, frame):
    """Handle SIGTERM signal for graceful shutdown."""
    logger.info("Received SIGTERM signal, shutting down gracefully...")
    sys.exit(0)


def start_channel(channel_type: str):
    """
    Initialize and start the messaging channel.

    Args:
        channel_type: The type of channel to start (e.g., 'wx', 'wxy', 'terminal', 'wechatmp')
    """
    from channel import channel_factory

    channel = channel_factory.create_channel(channel_type)
    if channel_type in ["wx", "wxy", "terminal", "wechatmp", "wechatmp_service", "wechatcom_app", "dingtalk",
                        "feishu", "bark", "wechatcom_service", "weworktop"]:
        channel.startup()
    return channel


def run():
    """Main run function — loads config and starts the appropriate channel."""
    # Register signal handlers
    signal.signal(signal.SIGTERM, sigterm_handler)

    try:
        # Load configuration
        load_config()
        logger.info("Configuration loaded successfully.")

        # Determine channel type from config
        channel_type = conf().get("channel_type", "wx")
        logger.info(f"Starting CowAgent with channel type: {channel_type}")

        # Plugin system initialization
        from plugins import PluginManager
        PluginManager().load_configured_plugins()

        # Start the channel
        start_channel(channel_type)

    except KeyboardInterrupt:
        logger.info("Interrupted by user, exiting...")
        sys.exit(0)
    except Exception as e:
        logger.exception(f"Failed to start CowAgent: {e}")
        sys.exit(1)


if __name__ == "__main__":
    run()
