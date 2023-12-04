## main.py for [Gaoyiming's Graphonomy repos](https://github.com/Gaoyiminggithub/Graphonomy)

clone Gaoyiming's human parsing repos. follow his step to set it up.
the model should be in [Gaoyiming's repos](https://github.com/Gaoyiminggithub/Graphonomy)

```
git clone https://github.com/Gaoyiminggithub/Graphonomy.git
cd Graphonomy
```

put `main.py` and `requirements.txt` into the newly cloned repos.

create a environment of your choice.

```
mkdir image-parse
mkdir image
```

put your pics into `image`.
(for best result use 768x1024 res pics)

```
pip install -r requirements.txt
python main.py
```

if done correctly, outputs should be in `image-parse`.
