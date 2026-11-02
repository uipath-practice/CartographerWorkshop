"""
MkDocs-macros module: injects the training-environment values into pages.

Why this exists
---------------
The training environment differs between building and release:
  - staging  -> used while authoring, so live lessons are never disrupted
  - prod     -> the real participant environment

Pages reference the variables instead of hardcoding URLs/tenants, e.g.:

    !!! tip "Training Environment"
        Log in at **[{{ training_url }}]({{ training_url }})** using tenant **{{ training_tenant }}**.

Switch environments at build time with the COURSE_ENV variable:
    COURSE_ENV=staging mkdocs serve     # author/preview
    COURSE_ENV=prod    mkdocs build     # release (CI uses this)

Default is "prod" so a plain build is release-safe.
"""

import os

ENVIRONMENTS = {
    "staging": {
        "training_url": "https://cloud.uipath.com/tpenlabs",
        "training_authority": "https://cloud.uipath.com",
        "training_tenant": "CartographerWorkshop",
        "env_label": "Staging (build & preview)",
    },
    "prod": {
        "training_url": "https://cloud.uipath.com/tpenlabs",
        "training_authority": "https://cloud.uipath.com",
        "training_tenant": "CartographerWorkshop",
        "env_label": "Workshop environment",
    },
}


def define_env(env):
    profile = os.getenv("COURSE_ENV", "prod").lower()
    cfg = ENVIRONMENTS.get(profile, ENVIRONMENTS["prod"])
    for key, value in cfg.items():
        env.variables[key] = value
    env.variables["course_env"] = profile
