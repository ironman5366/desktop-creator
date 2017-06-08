# Desktop entry creator

This script creates favicon based desktop entries for GNOME

## Installation

```
git clone https://github.com/ironman5366/desktop-creator
cd desktop-creator
pip3 install -r requirements.txt
```

## Usage
`python3 desktop-creator.py https://reddit.com Reddit`

## Credits
Most of the credit for this project should go to https://github.com/phillipsm
who wrote the scripts for the favicon downloading as part of
https://github.com/phillipsm/pyfav.

At the time of writing this the project was nonfunctional out of the box
(at least on python 3.6 on Arch), so I copied the core methods that I needed
and put them into `pyfav_utils.py`
