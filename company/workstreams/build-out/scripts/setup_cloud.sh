#!/usr/bin/env bash
# Paste this into the Claude Code cloud environment "Setup script" field.
# Runs once as root on Ubuntu 24.04 before Claude starts; the result is cached.
# Keep it under ~5 minutes or it will not be cached.
# Do NOT reference secrets here: environment variables are not available to the setup script.
set -e
apt-get update -qq
apt-get install -y -qq git-lfs >/dev/null
git lfs install --system
pip install --break-system-packages -q \
  pyyaml jsonschema ezdxf ifcopenshell build123d
python3 -c "import build123d, ifcopenshell, ezdxf; print('geometry stack ok')"
