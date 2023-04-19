prepare_data:
	openai tools fine_tunes.prepare_data -f dataset_1.jsonl
create: 
	openai api fine_tunes.create -t data/dataset_35_prepared.jsonl -m davinci --suffix "eddie_"	
use:
	openai api completions.create -m davinci:ft-personal:metapath-2023-03-27-10-48-25 -p metapath 