"""Extract inline JS from index.html and verify it parses."""
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
INDEX = ROOT / "index.html"


def extract_main_script(html: str) -> str:
    anchor = html.index("</section>")
    start = html.index("<script>", anchor)
    end = html.index("</script>", start)
    return html[start + len("<script>") : end]


def main() -> int:
    if not INDEX.is_file():
        print("missing:", INDEX)
        return 1
    html = INDEX.read_text(encoding="utf-8")
    js = extract_main_script(html)
    try:
        import esprima  # type: ignore
        esprima.parseScript(js)
        print("parse ok (esprima), length", len(js))
        return 0
    except ImportError:
        pass
    opens = js.count("{") + js.count("(") + js.count("[")
    closes = js.count("}") + js.count(")") + js.count("]")
    if opens != closes:
        print("bracket mismatch: opens", opens, "closes", closes)
        return 1
    print("parse ok (heuristic bracket check), length", len(js))
    print("tip: pip install esprima for full JS parse validation")
    return 0


if __name__ == "__main__":
    sys.exit(main())
