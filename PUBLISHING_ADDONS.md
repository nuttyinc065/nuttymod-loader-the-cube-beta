# Publishing Add-ons

This repository is a community catalog. Every published add-on must be safe to distribute, honestly described, and organized so the loader can find it.

## Before you submit

You must:

- own the add-on or have permission to publish every included file;
- comply with the add-on's dependencies and third-party licenses;
- test the add-on with the current version of The Cube Beta and state any known limitations;
- scan the package for malware and remove secrets, personal data, debug dumps, and unrelated files; and
- choose a unique, stable slug made from lowercase letters, numbers, and hyphens, such as **better-jumping**.

Do not submit add-ons that:

- contain malware, credential theft, destructive code, hidden downloads, undisclosed telemetry, or other harmful behavior;
- impersonate another creator or reuse work without permission and attribution;
- enable harassment, cheating in competitive play, or abuse of other people or services;
- include pirated, paid, leaked, or copyrighted game assets that you are not allowed to redistribute;
- are intentionally misleading about their purpose or behavior; or
- require users to weaken normal security protections without a clear, legitimate reason.

Maintainers may reject or remove an add-on that creates a safety, legal, compatibility, or community risk.

## Package layout

Place each release in:

    addons/packages/<slug>/<version-with-dashes>/<package-file>

For example, version **1.2.0** of **better-jumping** could be stored at:

    addons/packages/better-jumping/1-2-0/better_jumping.py

Use a new version directory for every release. Never replace the contents of an already published version. Keep packages as small as practical. Archives must be self-contained and use a common format such as .zip or .7z; do not use password-protected archives.

## Catalog entry

Create **addons/catalog/<slug>.json** using this shape:

    {
      "name": "Better Jumping",
      "description": "Adds configurable jump height.",
      "version": "1.2.0",
      "author": "your-github-username",
      "filePath": "addons/packages/better-jumping/1-2-0/better_jumping.py",
      "submittedAt": "2026-09-04T12:00:00Z"
    }

Requirements:

- **name** is a short, human-readable title.
- **description** plainly explains what the add-on does.
- **version** follows semantic versioning (MAJOR.MINOR.PATCH).
- **author** identifies the creator or publishing team.
- **filePath** is a repository-relative path using / and points to the submitted file exactly, including letter case.
- **submittedAt** is an ISO 8601 UTC timestamp for this catalog submission.
- The JSON is valid and contains no comments or trailing commas.

## Pull request checklist

In the pull request, include:

- a summary of the add-on and its user-visible behavior;
- the tested game and loader versions;
- installation, use, and removal instructions;
- source code or a link to the source when practical;
- required runtimes, libraries, network access, permissions, or other dependencies;
- the license and attribution for included third-party material;
- screenshots or logs when they help reviewers verify the change; and
- a clear note about breaking changes, save-data effects, telemetry, or known conflicts.

Keep one add-on or one add-on update per pull request. Maintainers may inspect or test packages and ask for changes before publication. Approval is not a certification or warranty; users remain responsible for deciding which third-party add-ons to run.

## Updating or removing an add-on

For an update, add the new version directory, update the existing catalog entry, and describe changes in the pull request. Do not delete old releases unless a maintainer agrees that removal is necessary.

To request removal of your add-on, open an issue that identifies the catalog entry and explains whether the request concerns ownership, safety, compatibility, or deprecation. Do not publish sensitive security details in a public issue; follow the private reporting guidance in the [Code of Conduct](CODE_OF_CONDUCT.md#reporting-a-problem).
