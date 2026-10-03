"""PDF Page Split — Split a PDF into single pages or page ranges and save a clean folder."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='pdf_page_split',
        description='Split a PDF into single pages or page ranges and save a clean folder.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('PDF Page Split')
    print('Local page extraction without an upload converter.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
