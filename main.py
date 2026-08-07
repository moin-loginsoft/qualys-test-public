"""
mend-sca-test / app.py
 
Purpose
-------
This file exists purely to exercise Mend's Software Composition Analysis
(SCA) scanning. It imports every package listed in requirements.txt so
that the dependency tree is "used" (not just declared), which is closer
to a real-world project and avoids any "unused dependency" heuristics
some scanners apply.
 
It performs no real work — each function is a trivial smoke test that
just confirms the (deliberately outdated / vulnerable) libraries import
and run their most basic call. Do not deploy this file anywhere; it is
only meant to sit in a throwaway repo you connect to Mend for testing.
"""
 
import requests
import urllib3
import flask
import jinja2
import yaml
import numpy as np
import paramiko
from PIL import Image
from lxml import etree
import django
 
 
def check_requests():
    """Sanity check for the 'requests' package (CVE-2018-18074)."""
    return requests.__version__
 
 
def check_urllib3():
    """Sanity check for 'urllib3' (CVE-2019-11324)."""
    return urllib3.__version__
 
 
def check_flask():
    """Sanity check for 'Flask' (CVE-2019-1010083)."""
    app = flask.Flask(__name__)
    return flask.__version__, app.name
 
 
def check_jinja2():
    """Sanity check for 'Jinja2' (CVE-2019-10906)."""
    template = jinja2.Template("Hello {{ name }}!")
    return template.render(name="Mend")
 
 
def check_pyyaml():
    """Sanity check for 'PyYAML' (CVE-2020-1747 / CVE-2020-14343)."""
    data = yaml.safe_load("key: value")
    return data
 
 
def check_pillow():
    """Sanity check for 'Pillow' (CVE-2020-11538 / CVE-2020-5313)."""
    img = Image.new("RGB", (10, 10))
    return img.size
 
 
def check_numpy():
    """Sanity check for 'numpy' (CVE-2019-6446)."""
    arr = np.array([1, 2, 3])
    return arr.sum()
 
 
def check_django():
    """Sanity check for 'django' (CVE-2019-12308 / CVE-2019-14232)."""
    return django.get_version()
 
 
def check_lxml():
    """Sanity check for 'lxml' (CVE-2020-27783 / CVE-2021-43818)."""
    root = etree.fromstring("<root><child/></root>")
    return root.tag
 
 
def check_paramiko():
    """Sanity check for 'paramiko' (CVE-2018-7750)."""
    return paramiko.__version__
 
 
def main():
    checks = {
        "requests": check_requests,
        "urllib3": check_urllib3,
        "flask": check_flask,
        "jinja2": check_jinja2,
        "pyyaml": check_pyyaml,
        "pillow": check_pillow,
        "numpy": check_numpy,
        "django": check_django,
        "lxml": check_lxml,
        "paramiko": check_paramiko,
    }
 
    for name, fn in checks.items():
        try:
            result = fn()
            print(f"[OK]   {name}: {result}")
        except Exception as exc:
            print(f"[FAIL] {name}: {exc}")
 
 
if __name__ == "__main__":
    main()
