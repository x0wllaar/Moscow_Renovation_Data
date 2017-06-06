json_name="jsons/moscow_ren_json_$(date +%H%M_%d%m%y).json"
csv_name="csvs/moscow_ren_json_$(date +%H%M_%d%m%y).csv"

echo "Downloading data to $json_name"
curl https://www.mos.ru/altmosprx/api/1/renovation/bounded_addresses\?p1\=58.436233157945246,45.99975585937501\&p2\=54.813348417419284,30.179443359375004\&full >> $json_name

echo ""

echo "Parsing data to $csv_name"
python parser.py $json_name $csv_name