# Reference material

This directory holds the raw material a session looks at before it makes a design decision. Nothing here changes `src/` or the design system. It is the input, not the output.

## Layout

- `clips/` holds video dropped in for review. Not committed.
- `frames/` holds stills decomposed from those clips, one folder per clip. Not committed.
- `shots/` holds screenshots and markups. Committed.
- `notes/` holds written observations as markdown. Committed.

## Video is always decomposed first

A session cannot read a video directly. A clip becomes usable only after it is broken into numbered stills, so every clip goes through `scripts/frames.mjs` before anyone looks at it:

```
npm run frames -- refs/clips/lobby.mov lobby 10
```

That writes `refs/frames/lobby/0001.png`, `0002.png`, and so on. The third argument is frames per second and defaults to 10.

## Frames and notes are primary evidence

Frames and notes carry the same weight as inspecting the live site. When a decision rests on what a clip showed or what a customer did in it, the frame and the note that reads it are the record of that, not a lesser version of it.

## Write down what you concluded

Images do not survive the session. A session that used reference material writes what it concluded into `refs/notes/` or `docs/` before it ends. If the conclusion lives only in a frame, it is gone next time. The note is what carries forward.
