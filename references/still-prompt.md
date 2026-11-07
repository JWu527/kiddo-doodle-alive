# 静帧提示词模板

把 `{...}` 换成当次原图信息。务必把原图路径加入 reference_image_paths。

```text
Minimalist children's-doodle remake on warm cream textured drawing paper with lots of empty space.
Center a small (about one third of the canvas width) version of the child's drawing:
{subject_and_colors}.
Soft colored-pencil and crayon texture, slightly wobbly naive marker lines,
keep the child's charming imperfect strokes, not a polished adult illustration.
Add a faint soft shadow under the subject.
Below it, a small handwritten cursive caption in dark grey pencil: "{caption}".
No black frame, no photo background, no desk, no extra characters.
```

## caption 规则

- 用户给了名字：`{Name}'s {short theme}`，例如 `Lulu's pink dots kitty`
- 未给名字：先问，或暂用中性词 `little doodle` / `little shapes`
- 可加 `♡` 或 `:)` ，不要长句
