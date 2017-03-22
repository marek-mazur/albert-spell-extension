# Albert launcher spell extension
It is an extension for Albert launcher that you can find here:
```
https://github.com/albertlauncher/albert 
```
You can quickly check spelling of any word in any language you want.

## Installation
Put extension file into right location and make it executable
```
~/.local/share/albert/external/org.albert.extension.external.spell.py
chmod +x ~/.local/share/albert/external/org.albert.extension.external.spell.py
```
Be sure that you have installed needed packages.
```bash
sudo apt install xclip aspell aspell-en aspell-pl aspell-de
```
Dump dictionary of any language you need.
```bash
mkdir -p ~/.local/share/albert/external/spell
aspell -l en dump master | aspell -l en expand > ~/.local/share/albert/external/spell/en.dict
aspell -l pl dump master | aspell -l pl expand > ~/.local/share/albert/external/spell/pl.dict
aspell -l de dump master | aspell -l de expand > ~/.local/share/albert/external/spell/de.dict
```
## Usage examples
```
spell en great
spell pl góra
spell de viel
```
