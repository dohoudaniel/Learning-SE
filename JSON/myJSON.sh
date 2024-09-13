#!/usr/bin/env bash
# A couple of Bash commands I run to install JSON tools on my local system
# Links:
# 1. https://github.com/dominictarr/JSON.sh
# 2. https://github.com/archan937/jsonv.sh/
# 3. https://github.com/bashtools/JSONPath.sh
# 4. https://pypi.org/project/simplejson/
# 5. https://github.com/ultrajson/ultrajson
# 6. https://pypi.org/project/metamagic.json/
#
npm install -g JSON.sh
pip3 install git+https://github.com/dominictarr/JSON.sh#egg=JSON.sh
yaourt -Sy json-sh
#
sudo apt install gawk
curl -Ls https://raw.github.com/archan937/jsonv.sh/master/install.sh | bash
#
sudo npm install -g jsonpath.sh
#
pip3 install simplejson
#
python3 -m pip3 install ujson
#
pip3 install metamagic.json
