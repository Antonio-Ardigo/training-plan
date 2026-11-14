# Connectors

The plugin is self-contained and needs no external service.

| What | Used for | Needed |
|---|---|---|
| The file system | Each course folder: `course.json`, `overview.md`, lesson notes, practice books, lesson pages | Always |
| Python 3 | `skills/course-model/tools/course.py`: checking a course, writing the overview, next lesson, progress, converting old plans | Recommended. Without it, Claude follows the same rules by hand |
| A tool that publishes pages (for example claude.ai Artifacts) | Showing a lesson page as a link | Optional. Without it, the page is written as a file to open in a browser, or the lesson runs in chat |

The teaching method once came from a separate plugin, concept-builder. It is fully part of this plugin now, in the `explaining` skill, with no dependency on concept-builder.
