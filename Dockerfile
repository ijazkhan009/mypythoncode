# BAD: latest tag (warning)
FROM python:latest

# BAD: not absolute path (error)
WORKDIR app

# BAD: using ADD instead of COPY (error)
ADD . .

# BAD: split RUN + not cleaning + not pinned packages
RUN apt-get update
RUN apt-get install -y curl wget

# BAD: no cleanup (info DL3009)

# BAD: using pip without version and cache
RUN pip install fastapi uvicorn

# BAD: multiple RUNs (info DL3059)
RUN echo "Another unnecessary layer"

# BAD: using root (warning)
USER root

# BAD: expose low port (not wrong but suspicious)
EXPOSE 80

# BAD: multiple CMD (warning)
CMD ["echo", "Hello World"]
CMD ["uvicorn", "test:app", "--host", "0.0.0.0", "--port", "8000"]