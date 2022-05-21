# osu! to mp3

convert .osz osu beatmaps into properly-tagged .mp3 files

## Installation

Clone this project and run `python setup.py install --user`

Alternatively, install osu2mp3 from PyPI:

```
python -m pip install --user osu2mp3
```

## Run

`osu2mp3 [-h] [-i INPUT] [-o OUTPUT] [-s]`

## Arguments

| Argument     | Description                                        |
| ------------ | -------------------------------------------------- |
| -i, --input  | Specify input directory                            |
| -o, --output | Specify directory audio files will be extracted to |
| --silent     | Don't show progress bar                            |
| -h, --help   | Show the information above                         |
