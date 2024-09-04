FROM ubuntu:noble

RUN apt-get update && \
    apt-get install python3-psutil python3.12-venv python-is-python3 python-dev-is-python3 -y

# Run the application:
COPY print-system-info.py /root/
CMD ["python", "/root/print-system-info.py"]
