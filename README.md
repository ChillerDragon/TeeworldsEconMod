# TeeworldsEconMod
A python script which communicates with teeworlds server log as input and econ connection as output.

# How to use?

create a ``tem.settings`` file and write line by line these configurations:

```
/path/to/your/teeworlds/directory
name_of_teeworlds_srv
econ_password
econ_port
Debug (true/false)
Stats (file/sql)
/path/to/logs/dir
```
a sample config could look like:
```
/home/chiller/teeworlds
teeworlds_srv
sample_password
8203
false
sql
/home/chiller/logs
```


To fire things up execute ``./start_tem.sh``.

This will start your teeworlds server pipe the output through the python scripts
and then respond via netcat connection to the teeworlds econ api.

# Dependencies

You need python3.7 installed and a teeworlds server with an autoexec.cfg including:
```
ec_port "port"
ec_password "password"
```

# Advanced config

Additional config variables can be found in
```
src/global_settings.py
```

# Logs

Currently the logs have some weird binary chunks in it and ``grep`` doesn't work well with it.

If you want to convert the logs to text only you could use a command like:

```
for f in logs/*; do echo "[`basename $f`]... (`wc -l $f`)"; strings $f > txt_logs/`basename $f`; done
```

# Bugs

``sv_scorelimit 1000`` is strongly recommended
if scorelimit is lower the wins and looses will be calculated on new round start.
So all players who leave during end screen won't be tracked.
If the scorelimit is 1000 the wins and looses will be saved instantly on the 10th capture.

``shuffle_teams`` confuses the script regarding team color.
So all stats depending on team color are broken ( for now only wins and looses).  
