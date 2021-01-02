# Install

```
virtualenv -p python3 venv

. venv/bin/activate
pip install -r requirements.txt
```

# Configure

Create a plan in Razor dashboard, and set `RAZOR_PLAN_ID` in your `.env`


```
cp .env.example .env
# Fill in your config
```


# Run

```
export FLASK_APP=app.py
export FLASK_DEBUG=True
flask run
```
