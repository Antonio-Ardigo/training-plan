# Idea map

An idea map shows how the ideas of a lesson, a topic or a whole course connect. It is a Markdown nested list.

## Three scopes

| Scope | When | Centre | Size |
|---|---|---|---|
| **Lesson map** | Offered in a lesson after Learn (lesson-flow says when) | The lesson's topic, not the whole course | 10 to 15 nodes |
| **Topic map** | The learner asks to map a topic | The topic | 10 to 15 nodes; 5 to 8 for a quick view |
| **Course map** | The learner asks to map the whole course | The course goal | 15 to 25 nodes |

## Read the course first

Build every map from `course.json`. Find the course as the course-model skill says (section 6: a named course, else `*/course.json` or `course.json` in the working folder).

Read:
- `principles[]`: `id`, `name`, `statement`, `key_idea`
- `lessons[]`: `number`, `title`, `kind`, `principles`, `needs`, `key_idea`
- `facts[]`: `fact`, `used_in`
- `background[]`: `name`, `lesson`

Index each principle by the lesson that teaches it (the lesson of kind `principle` whose `principles` names it). Facts point to lessons through `used_in`, background items through `lesson`.

With no course, draw the map alone and say that no course was found.

## Format

Each node is a **bold name**, its kind in brackets, the lesson that teaches it, and one line after a colon.

```markdown
## Idea map: <topic>

- **<Topic>** (centre): <one line>
  - needs:
    - **<Background item>** (background) [not in course]: <one line>
  - rests on:
    - **<Principle>** (principle) [Lesson 2]: <one line>
      - led to:
        - **<Innovation>** (innovation) [Lesson 5]: <one line>
          - makes possible:
            - **<Use>** (application) [Lesson 8]: <one line>
    - **<Principle>** (key idea ★) [Lesson 3]: <one line>
  - makes possible:
    - **<Use>** (application) [not in course]: <one line>
```

### Node kinds

| Kind | Meaning | How many |
|---|---|---|
| **centre** | What is mapped | Exactly one |
| **principle** | A foundational truth (`principles[]`) | The 3 to 5 that carry the rest |
| **key idea ★** | A principle marked `key_idea` | As in the course |
| **innovation** | A step that built the topic | Under the principle it came from |
| **fact** | A fact to know (`facts[]`) | Only those the mapped lessons use |
| **application** | A use of the ideas | 2 to 4 |
| **background** | Knowledge the topic assumes (`background[]`) | 1 to 3 |
| **shared** | An idea two mixed-up ideas share | Side by side maps only |

### Link labels

| Label | Meaning | From, to |
|---|---|---|
| `needs` | Needs this background first | centre to background |
| `rests on` | Is built on these principles | centre to principle |
| `led to` | Produced this innovation | principle to innovation |
| `makes possible` | Makes this use possible | innovation or centre to application |
| `generalises` | Is the general case of | parent to child |
| `is a special case of` | Is a special case of | child to parent |
| `contrasts with` | Pulls the other way | between siblings |
| `same as` | Says the same thing another way | between siblings |

### Rules

1. The centre comes first. Under it, group by link: `needs`, then `rests on`, then `makes possible`.
2. Every node that a lesson teaches carries `[Lesson N]`. A node no lesson teaches carries `[not in course]`.
3. A lesson map shows every principle taught and every item worked on in the lesson. It has no "where to go next": Show you've got it comes next.
4. Descriptions are one line.
5. The map gives no answer to a test the learner has not taken yet.

## Side by side maps

After a side by side explanation, the lesson map has three parts:

```markdown
- **What they share**
  - **<Shared principle>** (shared): <one line>
- **<Idea A>** (centre): <one line>
  - rests on:
    - **<Shared principle>** (shared): see above
    - **<Principle only in A>** (principle): <one line>
- **<Idea B>** (centre): <one line>
  - rests on:
    - **<Shared principle>** (shared): see above
    - **<Principle only in B>** (principle): <one line>
```

## Course map

For the whole course: the course goal is the centre. Every principle is a first-level node with its lesson, key ideas marked ★. Concept and Tool lessons sit under the principle they rest on, Capstone lessons are applications, and `background[]` gives the background nodes.

## Coverage

A topic map or a course map ends with:

```markdown
**In the course:** <N> of <M> ideas are taught by a lesson.
**Not in the course:** <the [not in course] nodes>.
**Suggestion:** <for each, whether it needs a lesson (a background lesson for missing background) or can stay out>.
```

## Where the map goes

A lesson map is shown in the lesson and copied into the lesson notes. A topic or course map is shown in chat. It is written to a file only when the learner asks, listed in `files` with kind `other`.
