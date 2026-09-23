import subprocess
import sys

subprocess.check_call([
    sys.executable, "-m", "pip", "install",
    "requests",
    "colorama",
    "beautifulsoup4"
])

print("Libraries installed, Now go use DOS - PREMIUM!")