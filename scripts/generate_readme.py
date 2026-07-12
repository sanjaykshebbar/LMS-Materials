from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"

IGNORE = {
    "README.md",
    "LICENSE.md",
    "CONTRIBUTING.md",
    "CODE_OF_CONDUCT.md",
}

markdown_files = sorted(
    [
        p
        for p in ROOT.rglob("*.md")
        if ".github" not in p.parts
        and "node_modules" not in p.parts
        and "venv" not in p.parts
        and p.name not in IGNORE
    ]
)

sections = {}

for file in markdown_files:

    rel = file.relative_to(ROOT).as_posix()

    folder = file.parent.relative_to(ROOT).as_posix()

    if folder == ".":
        folder = "General"

    title = file.stem.replace("-", " ").replace("_", " ")

    # Read YAML title if available
    try:
        text = file.read_text(encoding="utf-8")
        m = re.search(r'^title:\s*["\']?(.*?)["\']?\s*$', text, re.MULTILINE)
        if m:
            title = m.group(1)
    except Exception:
        pass

    sections.setdefault(folder, []).append((title, rel))

toc = []

for section in sorted(sections):
    toc.append(f"### {section}\n")

    for title, path in sorted(sections[section]):
        toc.append(f"- [{title}]({path})")

    toc.append("")

generated = "\n".join(toc)

readme = README.read_text(encoding="utf-8")

pattern = re.compile(
    r'<!-- START_TOC -->(.*?)<!-- END_TOC -->',
    re.DOTALL
)

updated = pattern.sub(
    f'<!-- START_TOC -->\n\n{generated}\n<!-- END_TOC -->',
    readme,
)

README.write_text(updated, encoding="utf-8")

print("README updated successfully.")