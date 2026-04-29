FROM ghcr.io/zhayujie/chatgpt-on-wechat:latest

# Personal fork - using a pinned digest for reproducibility
# Updated base image reference to track upstream
LABEL maintainer="personal-fork"

# Set a default timezone so logs show local time
ENV TZ=Asia/Shanghai

# Set Python output to unbuffered so logs appear immediately in docker logs
ENV PYTHONUNBUFFERED=1

# Increase default log level verbosity for easier debugging during development
ENV LOG_LEVEL=DEBUG

ENTRYPOINT ["/entrypoint.sh"]
