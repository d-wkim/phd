---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.19.4
kernelspec:
  name: python3
  display_name: Python 3 (ipykernel)
  language: python
---

---
title: NMA
subtitle: A systematic review and network meta-analysis
---

```{code-cell} ipython3
import pandas as pd

df = pd.read_csv("../data/full_text_screening.csv", encoding = "utf-8")
df.head()

df = df[["DOI", "Author", "Publication Year"]]

Aglietti P et al.
Beynnon BD et al.
Calvert ND et al.
Eriksson K et al.
Garcia-Linage R et al.
Kohn D
Komzåk M et al.
Laoruengthana A et al.
Malik S et al.
O'Neill DB
Pigozzi F et al.
Popovic M et al.
Tang N et al.
Yadav AK et al.
```

```{code-cell} ipython3
for x in doi:
    url = f"https://doi.org/{x}"
    print(url)
```

### Search strategy

+++

```
(("anterior cruciate ligament"[mh] OR "anterior cruciate ligament"[tiab] OR "anterior cruciate ligament reconstruction"[tiab] OR "acl"[tiab])) 
AND (("bone-patellar tendon-bone"[tiab] OR "bone patellar tendon bone"[tiab] OR "patellar tendon"[tiab] OR "bptb"[tiab]) 
OR ("hamstring"[tiab] OR "hamstring tendon"[tiab] OR "semitendinosus"[tiab] OR "gracilis"[tiab]) 
OR ("quadriceps"[tiab] OR "quadriceps tendon"[tiab] OR "qt"[tiab]) 
OR ("peroneus"[tiab] OR "peroneus longus"[tiab] OR "fibularis longus"[tiab]) 
OR ("achilles"[tiab] OR "achilles tendon"[tiab]) 
OR ("tibialis"[tiab] OR "tibialis anterior"[tiab] OR "tibialis posterior"[tiab])) 
AND (("randomized controlled trial"[pt] OR "randomized controlled trial"[tiab] OR "randomised controlled trial"[tiab]) NOT ("review"[pt] OR "review"[tiab] OR "systematic review"[pt] OR "systematic review"[tiab] OR "meta-analysis"[pt] OR "meta-analysis"[tiab]))
```
