import subprocess
import os


WORKSPACE = "workspace"


def run_python(filename):

    filepath = os.path.join(
        WORKSPACE,
        filename
    )

    try:


        result = subprocess.run(
            [
                "python",
                filepath
            ],
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=10
        )


        return {
            "success": result.returncode == 0,
            "stdout": result.stdout,
            "stderr": result.stderr
        }


    except subprocess.TimeoutExpired:

        return {
            "success": False,
            "stdout": "",
            "stderr": "运行超时"
        }