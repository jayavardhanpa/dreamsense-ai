import subprocess
import sys
import os

def test_cli_pipeline_runs(tmp_path):
    input_csv = tmp_path / "input.csv"
    output_csv = tmp_path / "output.csv"

    input_csv.write_text(
        "dream_text\nI was flying over a city and felt free.\n"
    )

    cmd = [
        sys.executable,
        "-m",
        "dreams.cli",
        "--env",
        "dev",
        "--input",
        str(input_csv),
        "--output",
        str(output_csv)
    ]

    result = subprocess.run(cmd, capture_output=True, text=True)
    assert result.returncode == 0
