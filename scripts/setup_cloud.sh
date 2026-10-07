#!/usr/bin/env bash
# Sŏn repo: Claude Code cloud environment setup script.
# Paste into the cloud environment "Setup script" field (claude.ai/code > environment settings).
# Runs once as root on Ubuntu before Claude starts; the result is cached. Keep under ~5 minutes.
# Never put secrets here: environment variables are not available to the setup script.
# Sources: build-out (geometry stack, git-lfs), nerve (data pipeline), operations (PyMuPDF),
# learning-studio (pyyaml), science (numpy, matplotlib).
set -e
apt-get update -qq
apt-get install -y -qq git-lfs >/dev/null
git lfs install --system
pip install --break-system-packages -q \
  pyyaml jsonschema requests python-dotenv pytest \
  duckdb pyarrow pandas shapely matplotlib numpy openpyxl \
  pymupdf \
  ezdxf
# Geometry stack for build-out models (large; drop this line if setup runs past ~5 minutes)
pip install --break-system-packages -q ifcopenshell build123d || echo "geometry stack skipped"
python3 -c "import yaml, jsonschema, duckdb, fitz, ezdxf; print('son environment ok')"
