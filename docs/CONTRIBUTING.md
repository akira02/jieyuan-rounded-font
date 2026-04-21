# Contributing

Thank you for helping improve Jieyuan Rounded.

This is a derivative font project, so contributions should balance design improvements, source stability, and licensing care.

## Before You Start

Please read these files first:

- [`README.md`](../README.md)
- [`LICENSE`](../LICENSE)

Before making changes, make sure you understand that:

- this project is derived from upstream font sources
- reserved font names from upstream projects must not be reused as the primary name of modified releases

## What Contributions Are Helpful

Useful contributions include:

- glyph drawing fixes or refinements
- spacing and kerning improvements
- metadata cleanup
- OpenType feature cleanup
- documentation updates
- source consistency fixes for UFO data

## Source Editing Guidelines

Please keep changes focused and easy to review.

When editing the UFO source:

- avoid unnecessary large-scale reordering of glyphs
- do not rewrite `features.fea` unless the change is intentional and verified
- keep project naming consistent with the current repository identity

When changing metadata files such as `fontinfo.plist`, `lib.plist`, or feature definitions, remember that small changes can affect editor compatibility and compiled output.

## Check Your Changes

Before submitting a change, please do as many of these as you can:

- open the UFO in Glyphs or another compatible editor
- confirm glyph ordering still looks reasonable
- confirm there are no new feature parsing errors
- confirm the changed source files still load correctly
- if you changed metadata, make sure naming and attribution remain intentional

If build tooling is available in the future, compiled-font testing should be added to this checklist as well.

## Licensing and Attribution

Do not remove copyright or licensing text casually.

It is fine to update project metadata for Jieyuan Rounded, but please be careful with:

- legal notices
- reserved font names
- manufacturer and naming fields that affect release identity

If you are unsure whether a wording change is editorial or legal, treat it as sensitive and call it out in your contribution.

## Pull Requests and Change Notes

If you open a pull request or send a patch, please include:

- what you changed
- why you changed it
- whether the change affects outlines, spacing, kerning, features, or metadata
- how you checked the result

Small, well-scoped changes are preferred over broad cleanup passes.

## Language

This file is the English contribution guide.

For a Traditional Chinese version, see [CONTRIBUTING.zh-TW.md](./CONTRIBUTING.zh-TW.md).
