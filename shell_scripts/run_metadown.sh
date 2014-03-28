source ~/.bash_profile

cd ~/isos_for_metadown/glos_catalog
git pull origin master

cd metadown
python download.py ~/isos_for_metadown/glos_catalog/ISOs

cd ~/isos_for_metadown/glos_catalog
git checkout master && git add . && git commit -m "Metadown generated content" && git pull && git push origin master

# Now update BaseX
cd ~/glos_catalog/basex; bash populate_git.sh /home/harvester/glos_catalog/ISOs Models
cd ~/glos_catalog/basex; bash populate_git.sh /home/harvester/glos_catalog/ISOs Satellite
cd ~/glos_catalog/basex; bash populate_git.sh /home/harvester/glos_catalog/ISOs GeoNetwork
cd ~/glos_catalog/basex; bash populate_git.sh /home/harvester/glos_catalog/ISOs RANGER3
cd ~/glos_catalog/basex; bash populate_git.sh /home/harvester/glos_catalog/ISOs GLERL/NBS
cd ~/glos_catalog/basex; bash populate_git.sh /home/harvester/glos_catalog/ISOs GLERL/AIRTEMPS
cd ~/glos_catalog/basex; bash populate_git.sh /home/harvester/glos_catalog/ISOs GLERL/ATMO
cd ~/glos_catalog/basex; bash populate_git.sh /home/harvester/glos_catalog/ISOs GLERL/PRECIP
cd ~/glos_catalog/basex; bash populate_git.sh /home/harvester/glos_catalog/ISOs GLC
cd ~/glos_catalog/basex; bash populate_git.sh /home/harvester/glos_catalog/ISOs WaterLevels

