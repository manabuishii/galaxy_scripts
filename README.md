# galaxy_scripts
Galaxy Related Scripts

## version

```
0.1.1
```

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

#### Sample output

```
41,c9468fdb6dc5c5f1,1cc9e71640659469,ok,262226,txt,eXpress on data 39 and data 6,180 lines,/api/histories/c9468fdb6dc5c5f1/contents/1cc9e71640659469
42,c9468fdb6dc5c5f1,1bf06a2bcfbb8cf9,ok,3600094,txt,eXpress on data 39 and data 6,"34,707 lines",/api/histories/c9468fdb6dc5c5f1/contents/1bf06a2bcfbb8cf9
43,c9468fdb6dc5c5f1,e0d9a771c733e086,error,0,tabular,GetFastQCRawDataFiles on current history,error,/api/histories/c9468fdb6dc5c5f1/contents/e0d9a771c733e086
44,c9468fdb6dc5c5f1,48885bbd1215db53,error,0,tabular,GetQuantityCountInfo on current history,error,/api/histories/c9468fdb6dc5c5f1/contents/48885bbd1215db53
45,c9468fdb6dc5c5f1,f1cb3a6ff6a93c01,error,0,tabular,GetDatasetDatPath,error,/api/histories/c9468fdb6dc5c5f1/contents/f1cb3a6ff6a93c01
46,c9468fdb6dc5c5f1,822aeedf25d30c76,paused,0,tabular,SummaryOfReadQC on data 44 and data 43: Merged summary(single-end only),queued,/api/histories/c9468fdb6dc5c5f1/contents/822aeedf25d30c76
47,c9468fdb6dc5c5f1,4fb563a6a1060ab1,paused,0,tabular,SummaryOfReadQC on data 44 and data 43: FastQC summary,queued,/api/histories/c9468fdb6dc5c5f1/contents/4fb563a6a1060ab1
48,c9468fdb6dc5c5f1,cab68a1ccca17e68,paused,0,tabular,SummaryOfReadQC on data 44 and data 43: CountInfo summary,queued,/api/histories/c9468fdb6dc5c5f1/contents/cab68a1ccca17e68
49,c9468fdb6dc5c5f1,bb80841fd9d212dd,paused,0,html,SummaryOfReadQC on data 44 and data 43.html,queued,/api/histories/c9468fdb6dc5c5f1/contents/bb80841fd9d212dd
50,c9468fdb6dc5c5f1,02b1cfb59f716d61,paused,0,tabular,ConvertAndMergeCountData on data 45 count data,queued,/api/histories/c9468fdb6dc5c5f1/contents/02b1cfb59f716d61
51,c9468fdb6dc5c5f1,705cc5c1fdaa7d3e,paused,0,tabular,ConvertAndMergeCountData on data 45 normalizing data,queued,/api/histories/c9468fdb6dc5c5f1/contents/705cc5c1fdaa7d3e
52,c9468fdb6dc5c5f1,665a42f7453c0065,queued,0,tabular,PcaAndVisualizationInGalaxy on data 50_eigenvectors,queued,/api/histories/c9468fdb6dc5c5f1/contents/665a42f7453c0065
53,c9468fdb6dc5c5f1,4488b53dbfdabfab,queued,0,tabular,PcaAndVisualizationInGalaxy on data 50_eigenvalues_and_variances,queued,/api/histories/c9468fdb6dc5c5f1/contents/4488b53dbfdabfab
54,c9468fdb6dc5c5f1,48e973444aea3119,queued,0,html,PcaAndVisualizationInGalaxy on data 50_output.html,queued,/api/histories/c9468fdb6dc5c5f1/contents/48e973444aea3119
55,c9468fdb6dc5c5f1,7e9b613206eaaf1e,queued,0,tabular,CorrAndClusterForLogCountData on data 50_correlation coefficient,queued,/api/histories/c9468fdb6dc5c5f1/contents/7e9b613206eaaf1
```

# Docker

run

```
docker  run --rm manabuishii/galaxy_scripts:0.1.1 galaxy_history_detail.py YOURGALAXYHOST YOURAPIKEY c9468fdb6dc5c5f1 --tsv
```

result

```
41,c9468fdb6dc5c5f1,1cc9e71640659469,ok,262226,txt,eXpress on data 39 and data 6,180 lines,/api/histories/c9468fdb6dc5c5f1/contents/1cc9e71640659469
42,c9468fdb6dc5c5f1,1bf06a2bcfbb8cf9,ok,3600094,txt,eXpress on data 39 and data 6,"34,707 lines",/api/histories/c9468fdb6dc5c5f1/contents/1bf06a2bcfbb8cf9
43,c9468fdb6dc5c5f1,e0d9a771c733e086,error,0,tabular,GetFastQCRawDataFiles on current history,error,/api/histories/c9468fdb6dc5c5f1/contents/e0d9a771c733e086
44,c9468fdb6dc5c5f1,48885bbd1215db53,error,0,tabular,GetQuantityCountInfo on current history,error,/api/histories/c9468fdb6dc5c5f1/contents/48885bbd1215db53
45,c9468fdb6dc5c5f1,f1cb3a6ff6a93c01,error,0,tabular,GetDatasetDatPath,error,/api/histories/c9468fdb6dc5c5f1/contents/f1cb3a6ff6a93c01
46,c9468fdb6dc5c5f1,822aeedf25d30c76,paused,0,tabular,SummaryOfReadQC on data 44 and data 43: Merged summary(single-end only),queued,/api/histories/c9468fdb6dc5c5f1/contents/822aeedf25d30c76
47,c9468fdb6dc5c5f1,4fb563a6a1060ab1,paused,0,tabular,SummaryOfReadQC on data 44 and data 43: FastQC summary,queued,/api/histories/c9468fdb6dc5c5f1/contents/4fb563a6a1060ab1
```

## REPR

TODO: write

```
docker $(docker-machine config docker1.10) run --rm -ti manabuishii/galaxy_scripts:0.1.1 repr_bioblend YOURGALAXYHOST YOURAPIKEY
Python 2.7.11 (default, Feb 17 2016, 15:35:52)
[GCC 4.9.2] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> gi
GalaxyInstance object for Galaxy at YOURGALAXYHOST
>>> gi.histories.get_histories(name='your_own_history')
[{u'name': u'your_own_history', u'tags': [], u'deleted': False, u'purged': False, u'id': u'2a56795cad3c7db3', u'url': u'/api/histories/2a56795cad3c7db3', u'published': False, u'model_class': u'History', u'annotation': None}]
>>>
```
