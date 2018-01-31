# removalnotes
A pandoc filter which removes div block in "rmnote" class

### Install

Only considered to work with Python3.

- `pip3 install git+https://github.com/pandocker/removalnotes.git`

Python2 may work but never tested.

- `pip install git+https://github.com/pandocker/removalnotes.git`

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

::::: rmnote
##### Note {-}

This is a note block. By the way this `:::` syntax is available from pandoc 2.0
:::::

<div class="rmnote">
##### Note {-}

This is another note block
</div>

- `pandoc -M rmnote=false` ... **keeps** DIV block(default)
- `pandoc -M rmnote=true` ... **removes** DIV block
- YAML metadata file can contain `rmnote` entry

# License
MIT license (c) 2018 pandocker/Kazuki Yamamoto
