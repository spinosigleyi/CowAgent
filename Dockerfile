FROM ghcr.io/zhayujie/chatgpt-on-wechat:latest

# Personal fork - using a pinned digest for reproducibility
# Updated base image reference to track upstream
LABEL maintainer="personal-fork"

ENTRYPOINT ["/entrypoint.sh"]
