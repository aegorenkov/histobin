# histobin
Python library to make bin width selection for histograms very simple

```
from histobin import Histobin
hb = Histobin(df.column)
```

## Square-root choice
```
df.column.plot(kind='hist', bins=hb.sqrt)
df.hist(column='column', by='group', bins=hb.sqrt)
```
## Sturges' formula
```
df.column.plot(kind='hist', bins=hb.sturges)
df.hist(column='column', by='group', bins=hb.sturges)
```
## Rice Rule
```
df.column.plot(kind='hist', bins=hb.rice_rule)
df.hist(column='column', by='group', bins=hb.rice_rule)
```
## Doane's formula
```
df.column.plot(kind='hist', bins=hb.doane)
df.hist(column='column', by='group', bins=hb.doane)
```
## Scott's normal reference rule
```
df.column.plot(kind='hist', bins=hb.scott)
df.hist(column='column', by='group', bins=hb.scott)
```
## Freedman–Diaconis' choice
```
df.column.plot(kind='hist', bins=hb.freedman_diaconis)
df.hist(column='column', by='group', bins=hb.freedman_diaconis)
```
