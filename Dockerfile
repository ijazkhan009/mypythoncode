# ❌ ERROR: latest tag (will still show if not ignored)
FROM python:latest

# ❌ ERROR: not absolute WORKDIR (DL3000)
WORKDIR app

# ❌ ERROR: using ADD instead of COPY (DL3020)
ADD . .

# ❌ ERROR: invalid port (DL3011)
EXPOSE 99999

# ❌ ERROR: duplicate stage names (DL3024)
FROM alpine AS builder
FROM ubuntu AS builder

# ❌ ERROR: invalid ENV usage (DL3044)
ENV PATH=$PATH:/usr/local/bin NEW_PATH=$PATH

# ❌ ERROR: using sudo (DL3004)
RUN sudo apt-get update

# ❌ ERROR: multiple ENTRYPOINT (DL4004)
ENTRYPOINT ["echo", "start"]
ENTRYPOINT ["echo", "override"]

# ❌ ERROR: wrong instruction order (DL3061)
RUN echo "This should not be before FROM"
FROM ubuntu:20.04

# (warnings + ignored stuff below — not important)
RUN apt-get install -y curl wget
RUN pip install fastapi uvicorn
USER root

CMD ["echo", "Hello"]
CMD ["uvicorn", "test:app"]