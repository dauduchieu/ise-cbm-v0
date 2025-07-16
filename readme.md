# clone:
```bash
git clone https://github.com/dauduchieu/ise-cbm-v0.git
```

# cd:
```bash
cd ise-cbm-v0
```

# setup:
```bash
source setup.sh
```

# train:
```bash
source run.sh /workspace/ise-cbm-v0/__train_data/legal True
```

## param:
- ``` $1: data folder ```
- ``` $2: is_test: True/False ```

# show progress:
```bash
mkdir output
cd output
scp -P 42047 root@167.179.138.57:/workspace/ise-cbm-v0/log.txt ./
cat log.txt
```

# download output (local comp):
```bash
scp -P 42047 root@167.179.138.57:/workspace/ise-cbm-v0/output/hcen.ipynb ./
```
```bash
scp -P 42047 root@167.179.138.57:/workspace/ise-cbm-v0/data/concepts/keyword_concepts.json ./
```
```bash
scp -P 42047 root@167.179.138.57:/workspace/ise-cbm-v0/data/concepts/abstract_concepts.json ./
```
