cd code
for year in {2013..2017}; do
    python ./data_prepare/crawler/NIPS_crawl.py $year ../data/nips_2013-2017/$year
    python ./data_prepare/prepare.py ../data/nips_2013-2017/$year
    done
done
