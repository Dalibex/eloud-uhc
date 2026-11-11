#!/usr/bin/env python3
"""Prints a Markdown summary of the JUnit results and JaCoCo coverage of a Gradle build.

CI appends the output to $GITHUB_STEP_SUMMARY. It never fails the job: missing reports
(for example when compilation fails before tests run) are reported as text.

Usage: python3 .github/scripts/ci_summary.py [build-dir]
"""
import sys
import xml.etree.ElementTree as ET
from pathlib import Path


def test_results(results_dir):
    """Returns (totals, failed test names), or (None, []) when there are no reports."""
    reports = sorted(results_dir.glob("TEST-*.xml"))
    if not reports:
        return None, []
    totals = {"tests": 0, "failures": 0, "errors": 0, "skipped": 0}
    failed = []
    for report in reports:
        suite = ET.parse(report).getroot()
        for key in totals:
            totals[key] += int(suite.get(key, 0))
        for case in suite.iter("testcase"):
            if case.find("failure") is not None or case.find("error") is not None:
                failed.append(f"{case.get('classname')}.{case.get('name')}")
    return totals, failed


def coverage(report):
    """Returns {counter type: (covered, total)} from the report-level JaCoCo counters."""
    if not report.is_file():
        return None
    root = ET.parse(report).getroot()
    result = {}
    for counter in root.findall("counter"):
        missed = int(counter.get("missed"))
        covered = int(counter.get("covered"))
        result[counter.get("type")] = (covered, missed + covered)
    return result


def percent(covered, total):
    return f"{100 * covered / total:.1f} %" if total else "n/a"


def main():
    build_dir = Path(sys.argv[1] if len(sys.argv) > 1 else "build")
    lines = ["## Tests", ""]

    totals, failed = test_results(build_dir / "test-results" / "test")
    if totals is None:
        lines.append("No test results found: the build stopped before the tests ran.")
    else:
        broken = totals["failures"] + totals["errors"]
        passed = totals["tests"] - broken - totals["skipped"]
        lines += [
            "| Passed | Failed | Skipped | Total |",
            "| ---: | ---: | ---: | ---: |",
            f"| {passed} | {broken} | {totals['skipped']} | {totals['tests']} |",
        ]
        if failed:
            lines += ["", "Failed tests:", ""]
            lines += [f"- `{name}`" for name in failed]

    lines += ["", "## Coverage", ""]
    counters = coverage(build_dir / "reports" / "jacoco" / "test" / "jacocoTestReport.xml")
    if counters is None:
        lines.append("No JaCoCo report found.")
    else:
        lines += ["| Metric | Covered | Total | Coverage |", "| --- | ---: | ---: | ---: |"]
        for label, key in (("Lines", "LINE"), ("Branches", "BRANCH")):
            covered, total = counters.get(key, (0, 0))
            lines.append(f"| {label} | {covered} | {total} | {percent(covered, total)} |")

    print("\n".join(lines))


if __name__ == "__main__":
    main()
