"""
MkDocs hook — two-column split shorthand.

Syntax (each delimiter on its own line):

    [[[
    left column content
    |30|
    right column content
    ]]]

The number is the left-column width percentage.
Supported values: 30 (30/70), 50 (50/50), 70 (70/30).

Expands to:

    <div class="img-cols img-cols-{N}" markdown>
      <div markdown>
    left column content
      </div>
      <div markdown>
    right column content
      </div>
    </div>
"""
import re

_SPLIT_RE = re.compile(
    r'\[\[\[\n(.*?)\n\|(\d+)\|\n(.*?)\n\]\]\]',
    re.DOTALL
)


def on_page_markdown(markdown, **kwargs):
    def _replace(m):
        left  = m.group(1).strip()
        ratio = m.group(2)
        right = m.group(3).strip()
        return (
            f'<div class="img-cols img-cols-{ratio}" markdown>\n'
            f'  <div markdown>\n{left}\n  </div>\n'
            f'  <div markdown>\n{right}\n  </div>\n'
            f'</div>'
        )
    return _SPLIT_RE.sub(_replace, markdown)
