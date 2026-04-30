# encoding:utf-8

import json
import os
import logging

logger = logging.getLogger(__name__)

# Default configuration values
default_config = {
    # Bot platform channel type: wechatmp, wechatmp-service, wechatcom_app, terminal, etc.
    "channel_type": "wx",

    # Model provider: openai, azure, zhipuai, moonshot, etc.
    "model": "gpt-4o-mini",

    # OpenAI API settings
    "open_ai_api_key": "",
    "open_ai_api_base": "https://api.openai.com/v1",
    "proxy": "",

    # Bot behavior settings
    "single_chat_prefix": [""],
    "single_chat_reply_prefix": "",
    "group_chat_prefix": ["@bot"],
    "group_chat_reply_prefix": "",
    "group_chat_keyword": [],
    "group_at_off": False,

    # Conversation settings
    "conversation_max_tokens": 1000,
    "expires_in_seconds": 3600,
    "character_desc": "You are ChatGPT, a large language model trained by OpenAI.",
    "temperature": 0.7,  # lowered from 0.9 for more consistent responses
    "top_p": 1,
    "frequency_penalty": 0,
    "presence_penalty": 0,

    # Image generation settings
    "image_create_prefix": ["画", "draw", "paint"],
    "image_create_size": "256x256",

    # Voice settings
    "voice_reply_voice": False,
    "voice_to_text": "openai",
    "text_to_voice": "openai",

    # Plugin settings
    "plugin_trigger_prefix": "$",

    # Rate limiting
    "rate_limit_chatgpt": 20,
    "rate_limit_dalle": 50,

    # Debug mode
    "debug": False,
}


class Config(dict):
    """Configuration manager that loads settings from config.json and environment variables."""

    def __init__(self, d=None):
        super().__init__()
        if d is None:
            d = {}
        for key, value in d.items():
            self[key] = value

    def __getitem__(self, key):
        if key not in self:
            return None
        return super().__getitem__(key)

    def get(self, key, default=None):
        """Get a configuration value with an optional default."""
        value = self[key]
        if value is None:
            return default
        return value


def load_config():
    """Load configuration from config.json file and environment variables."""
    global config

    config_path = os.path.join(os.path.dirname(__file__), "config.json")
    config_template_path = os.path.join(os.path.dirname(__file__), "config-template.json")

    if not os.path.exists(config_path):
        if os.path.exists(config_template_path):
            logger.warning("[Config] config.json not found, using config-template.json as reference.")
        else:
            logger.warning("[Config] config.json not found, using default configuration.")
        config = Config(default_config)
        return config

    try:
        with open(config_path, "r", encoding="utf-8") as f:
            file_config = json.load(f)
        # Merge defaults with file config (file config takes precedence)
        merged = {**default_config, **file_config}
        config = Config(merged)
        logger.info("[Config] Configuration loaded successfully from config.json")
    
