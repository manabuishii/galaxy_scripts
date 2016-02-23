# galaxy_scripts
Galaxy Related Scripts

# prerequisite

```
bioblend
```

# history

Get histories from Galaxy.

Default output is JSON.

## Get histories

```
python galaxy_histories.py YOURGALAXYHOST YOURAPIKEY
```

## Get a history detail

```
python galaxy_history_detail.py YOURGALAXYHOST YOURAPIKEY HISTORY_ID
```

### TSV style output

TSV output (currently some keys)

```
python galaxy_history_detail.py YOURGALAXYHOST YOURAPIKEY HISTORY_ID --tsv
```
