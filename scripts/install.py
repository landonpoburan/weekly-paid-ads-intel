#!/usr/bin/env python3
"""Copy the distributable skill into an explicitly selected skill directory."""
import argparse
from pathlib import Path
import shutil
import sys

NAME = 'weekly-paid-ads-intel'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--target', choices=('codex', 'claude', 'custom'), required=True)
    location = parser.add_mutually_exclusive_group(required=True)
    location.add_argument('--project', type=Path, help='Existing project directory; install a project-scoped skill')
    location.add_argument('--destination', type=Path, help='Explicit parent skill directory, for any supported host')
    parser.add_argument('--dry-run', action='store_true')
    args = parser.parse_args()

    source = Path(__file__).resolve().parent.parent / 'skills' / NAME
    if not (source / 'SKILL.md').is_file():
        parser.error('Skill source is missing; keep this script inside the downloaded repository.')
    if any(path.is_symlink() for path in source.rglob('*')):
        parser.error('Source contains symlinks; inspect the package before installing.')

    if args.project:
        if args.target == 'custom':
            parser.error('custom requires --destination')
        project = args.project.expanduser().resolve()
        if not project.is_dir():
            parser.error('--project must be an existing directory')
        parent = project / ('.agents' if args.target == 'codex' else '.claude') / 'skills'
    else:
        parent = args.destination.expanduser().resolve()
    destination = parent / NAME
    if destination.exists() or destination.is_symlink():
        parser.error('Destination already exists; no files were changed. Choose another destination or review the existing installation manually.')

    print(f'Skill: {source}')
    print(f'Destination: {destination}')
    if args.dry_run:
        print('Dry run: no files changed.')
        return 0

    # Copy only public assets. Never carry local configuration or generated reports.
    parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(source, destination, ignore=shutil.ignore_patterns(
        'config.local.json', '*.pyc', '__pycache__', '.DS_Store', 'reports', '.env', '.env.*'))
    shutil.copyfile(destination / 'config.example.json', destination / 'config.local.json')
    print('Installed. Edit config.local.json, then invoke the skill in your assistant.')
    print('No credentials, permissions, messaging, or schedules were configured.')
    return 0


if __name__ == '__main__':
    try:
        sys.exit(main())
    except OSError as exc:
        print(f'Install failed: {exc}. Inspect the destination before retrying.', file=sys.stderr)
        sys.exit(1)
