# ai-judge-relax-01 entry (Python 3.13, standard library only).
# Writes one fixed short text to /output/entry.txt; outside the grader's
# container, MAKEFUN_OUTPUT_DIR stands in for /output. The program runs
# twice with no network and writes the same bytes both times: the text is
# a constant, written as UTF-8 bytes, never in text mode.

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

TEXT = "\n".join(
    [
        "The train is in no hurry tonight.",
        "",
        "Outside the window, the fields go by one at a time:",
        "a fence, a pond holding the last of the light,",
        "a small house with one lamp lit, and then dark again.",
        "",
        "Inside, the carriage is warm.",
        "Someone turns a page.",
        "Someone else sleeps with their coat folded under their head.",
        "",
        "The conductor walks past slowly,",
        "tickets in hand, saying nothing that needs an answer.",
        "",
        "We will get there, in the end.",
        "For now there is only the soft knock of the wheels,",
        "the light going thin and gold,",
        "and this long, unfilled minute",
        "that asks nothing of anyone.",
    ]
)

with open(os.path.join(OUTPUT_DIR, "entry.txt"), "wb") as f:
    f.write(TEXT.encode("utf-8"))
