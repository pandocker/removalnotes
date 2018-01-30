# removalnotes
A pandoc filter which removes div block in "rmnote" class

### Syntax

```markdown
::::: rmnote
##### Note {-}

This is a note block. By the way this `:::` syntax is available from pandoc 2.0
:::::

<div class="rmnote">
##### Note {-}

This is another note block
</div>
```

- `pandoc -M rmnote=false` ... **keeps** DIV block(default)
- `pandoc -M rmnote=true` ... **removes** DIV block
- yaml metadata file can contain `rmnote` entry

# License
MIT license (c) 2018 pandocker/Kazuki Yamamoto
