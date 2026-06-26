from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import re
import textwrap

ROOT = Path(r"D:\Think Codex\Design Team\Shawn-Core")
SRC = ROOT / "dist" / "pdf" / "顺子Shawn升级说明.md"
OUT = ROOT / "dist" / "pdf" / "顺子Shawn升级说明.pdf"
FONT = Path(r"C:\Windows\Fonts\NotoSansSC-VF.ttf")
FALLBACK_FONT = Path(r"C:\Windows\Fonts\simhei.ttf")

PAGE_W, PAGE_H = 1240, 1754
MARGIN_X, MARGIN_TOP, MARGIN_BOTTOM = 92, 86, 86
LINE_GAP = 10


def font(size, bold=False):
    path = FONT if FONT.exists() else FALLBACK_FONT
    return ImageFont.truetype(str(path), size=size)


FONTS = {
    "title": font(54),
    "h1": font(38),
    "h2": font(30),
    "body": font(24),
    "small": font(20),
    "code": font(20),
}


def sanitize(line):
    line = re.sub(r"`([^`]+)`", r"\1", line)
    line = line.replace("**", "")
    return line


def text_width(draw, text, fnt):
    if not text:
        return 0
    return draw.textbbox((0, 0), text, font=fnt)[2]


def wrap_text(draw, text, fnt, max_width):
    text = sanitize(text).strip()
    if not text:
        return [""]
    lines = []
    current = ""
    for ch in text:
        test = current + ch
        if text_width(draw, test, fnt) <= max_width:
            current = test
        else:
            if current:
                lines.append(current)
            current = ch
    if current:
        lines.append(current)
    return lines


class PdfBuilder:
    def __init__(self):
        self.pages = []
        self.page = None
        self.draw = None
        self.y = 0
        self.page_no = 0
        self.new_page()

    def new_page(self):
        if self.page is not None:
            self.footer()
            self.pages.append(self.page)
        self.page_no += 1
        self.page = Image.new("RGB", (PAGE_W, PAGE_H), "#fbfaf7")
        self.draw = ImageDraw.Draw(self.page)
        self.y = MARGIN_TOP
        self.draw.rectangle([0, 0, PAGE_W, 18], fill="#1d3557")
        self.draw.rectangle([0, 18, PAGE_W, 30], fill="#e9c46a")

    def footer(self):
        self.draw.line([MARGIN_X, PAGE_H - 62, PAGE_W - MARGIN_X, PAGE_H - 62], fill="#d8d2c7", width=2)
        self.draw.text((MARGIN_X, PAGE_H - 48), "Shawn Core / DE 美术组设计助手", fill="#6b665f", font=FONTS["small"])
        page_text = str(self.page_no)
        self.draw.text((PAGE_W - MARGIN_X - text_width(self.draw, page_text, FONTS["small"]), PAGE_H - 48), page_text, fill="#6b665f", font=FONTS["small"])

    def ensure(self, height):
        if self.y + height > PAGE_H - MARGIN_BOTTOM:
            self.new_page()

    def add_spacer(self, h):
        self.y += h

    def add_heading(self, text, level):
        text = sanitize(text)
        if level == 1:
            fnt, color, gap_before, gap_after = FONTS["title"], "#1d3557", 12, 28
        else:
            fnt, color, gap_before, gap_after = FONTS["h1"], "#263238", 34, 18
        lines = wrap_text(self.draw, text, fnt, PAGE_W - MARGIN_X * 2)
        h = len(lines) * (fnt.size + 10) + gap_before + gap_after
        self.ensure(h)
        self.y += gap_before
        for line in lines:
            self.draw.text((MARGIN_X, self.y), line, fill=color, font=fnt)
            self.y += fnt.size + 10
        self.y += gap_after

    def add_body(self, text, bullet=False, small=False):
        fnt = FONTS["small"] if small else FONTS["body"]
        prefix = "• " if bullet else ""
        max_width = PAGE_W - MARGIN_X * 2 - (28 if bullet else 0)
        lines = wrap_text(self.draw, text, fnt, max_width)
        h = len(lines) * (fnt.size + LINE_GAP) + 8
        self.ensure(h)
        x = MARGIN_X + (28 if bullet else 0)
        if bullet:
            self.draw.text((MARGIN_X, self.y), "•", fill="#2a9d8f", font=fnt)
        for line in lines:
            self.draw.text((x, self.y), line, fill="#2b2b2b", font=fnt)
            self.y += fnt.size + LINE_GAP
        self.y += 8

    def add_code(self, lines):
        fnt = FONTS["code"]
        wrapped = []
        for line in lines:
            wrapped.extend(wrap_text(self.draw, line, fnt, PAGE_W - MARGIN_X * 2 - 48))
        h = len(wrapped) * (fnt.size + 8) + 34
        self.ensure(h)
        self.draw.rounded_rectangle([MARGIN_X, self.y, PAGE_W - MARGIN_X, self.y + h], radius=16, fill="#f0eee8", outline="#d4cab9", width=2)
        self.y += 17
        for line in wrapped:
            self.draw.text((MARGIN_X + 24, self.y), line, fill="#3a332b", font=fnt)
            self.y += fnt.size + 8
        self.y += 17

    def add_table(self, rows):
        parsed = []
        for raw in rows:
            cells = [sanitize(c.strip()) for c in raw.strip().strip("|").split("|")]
            if len(cells) > 1 and not all(set(c) <= {"-", " "} for c in cells):
                parsed.append(cells)
        if not parsed:
            return
        col_count = max(len(r) for r in parsed)
        col_w = (PAGE_W - MARGIN_X * 2) // col_count
        row_heights = []
        cell_lines = []
        for r in parsed:
            lines_row = []
            max_lines = 1
            for i in range(col_count):
                text = r[i] if i < len(r) else ""
                lines = wrap_text(self.draw, text, FONTS["small"], col_w - 24)
                lines_row.append(lines)
                max_lines = max(max_lines, len(lines))
            cell_lines.append(lines_row)
            row_heights.append(max(54, max_lines * 28 + 24))
        total_h = sum(row_heights)
        self.ensure(total_h + 18)
        y = self.y
        for ri, lines_row in enumerate(cell_lines):
            x = MARGIN_X
            fill = "#eaf3f1" if ri == 0 else ("#ffffff" if ri % 2 else "#f7f4ee")
            for ci, lines in enumerate(lines_row):
                self.draw.rectangle([x, y, x + col_w, y + row_heights[ri]], fill=fill, outline="#d8d2c7", width=1)
                ty = y + 12
                for line in lines:
                    self.draw.text((x + 12, ty), line, fill="#233", font=FONTS["small"])
                    ty += 28
                x += col_w
            y += row_heights[ri]
        self.y = y + 18

    def finish(self):
        self.footer()
        self.pages.append(self.page)
        first, rest = self.pages[0], self.pages[1:]
        first.save(OUT, "PDF", resolution=150.0, save_all=True, append_images=rest)


def build():
    text = SRC.read_text(encoding="utf-8")
    lines = text.splitlines()
    pdf = PdfBuilder()
    i = 0
    in_code = False
    code_lines = []
    table_lines = []

    while i < len(lines):
        line = lines[i].rstrip()
        if line.startswith("```"):
            if in_code:
                pdf.add_code(code_lines)
                code_lines = []
                in_code = False
            else:
                in_code = True
            i += 1
            continue
        if in_code:
            code_lines.append(line)
            i += 1
            continue
        if line.startswith("|"):
            table_lines.append(line)
            i += 1
            if i >= len(lines) or not lines[i].startswith("|"):
                pdf.add_table(table_lines)
                table_lines = []
            continue
        if not line.strip() or line.strip() == "---":
            pdf.add_spacer(8)
            i += 1
            continue
        if line.startswith("# "):
            pdf.add_heading(line[2:].strip(), 1)
        elif line.startswith("## "):
            pdf.add_heading(line[3:].strip(), 2)
        elif line.startswith("- "):
            pdf.add_body(line[2:].strip(), bullet=True)
        elif re.match(r"^\d+\. ", line):
            pdf.add_body(line.strip())
        else:
            pdf.add_body(line.strip())
        i += 1

    pdf.finish()


if __name__ == "__main__":
    build()
    print(OUT)
