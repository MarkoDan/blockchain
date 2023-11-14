**Activate the virtual environment**

```
source blockchain-env/bin/activate
```

**Install all packages**

```
pip3 install -r requirements.txt
```

**Run the tests**

Make sure to activate the virtual environment.

```
python -m pytest backend/tests
```

**Run the appplication and API**

Make sure to activate the virtual environment.

```
python -m backend.app
```

**Run a peer instance**

Make sure to activate the virtual environment.

```
$env:PEER="True"; python -m backend.app
```