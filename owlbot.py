import synthtool as s
from synthtool import gcp

common = gcp.CommonTemplates()

# ----------------------------------------------------------------------------
# Add templated files
# ----------------------------------------------------------------------------
templated_files = common.py_library(unit_cov_level=100, cov_level=100)


s.move(
    templated_files / ".kokoro",
    excludes=[
        "continuous/common.cfg",
        "presubmit/common.cfg",
        "build.sh",
    ],
)  # just move kokoro configs


assert 1 == s.replace(
    ".kokoro/docs/docs-presubmit.cfg",
    'value: "docs docfx"',
    'value: "docs"',
)

s.shell.run(["nox", "-s", "blacken"], hide_output=False)
