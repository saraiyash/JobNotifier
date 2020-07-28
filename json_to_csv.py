import os, json
import pandas as pd
import us

def is_job_in_usa(json_text):
	state_and_country_names = [state.name for state in us.states.STATES_AND_TERRITORIES]
	state_and_country_names += ['United States', 'United States of America', 'US', 'USA']
	print(json_text)
	for name in json_text:
		if name in state_and_country_names:
			return True
		else:
			pass
	return False


#list_of_folders_to_be_converted = ['mastercard', 'dell', 'hpe', 'intel', 'nvidia']
list_of_folders_to_be_converted = ['mastercard', 'dell', 'hpe', 'intel', '3m', 'cae', 'dun-and-breakfast', 'essity',
								   'wwe', 'samsung', 'veritas', 'nvidia', 'salesforce', 'adobe', 'pixar', 'kar_global',
								   'alcoa', 'gucci', 'catalent', 'nxp', 'fhi360', 'chanel', 'loblaw', 'mosaic',
								   'humana', 'american_red_cross', 'nordstrom', 'workday']
jsons_data = pd.DataFrame(columns=['Company','Title', 'ID', 'Location', 'PostingTime'])
for company in list_of_folders_to_be_converted:
	path_to_json = './com/'+company
	json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]
#print(json_files)  # for me this prints ['foo.json']

	

	for index, js in enumerate(json_files):
		with open(os.path.join(path_to_json, js)) as json_file:
			#print(company)
			json_text = json.load(json_file)
			
			try:
				Locations_to_be_checked = json_text['labels'][2].split(', ')
				if((json_text['labels'][3]=='Posted Today') and (is_job_in_usa(json_text['labels'][2].split(', ')))):
					Company = company
					Title = json_text['labels'][0]
					#Title_to_be_used = Title.replace(', ','-')
					#Title_to_be_used_final = Title_to_be_used.replace(' ','-')
					ID = json_text['labels'][1]
					Location = json_text['labels'][2]
					#Location_to_be_used=Location.replace(', ','-')
					#Location_to_be_used_final=Location_to_be_used.replace(' ','-')
					PostingTime = json_text['labels'][3]
					#Link = 'https://mastercard.wd1.myworkdayjobs.com/en-US/CorporateCareers/job/'+Location_to_be_used_final+'/'+Title_to_be_used_final+'_'+ID
					jsons_data.loc[index] = [Company, Title, ID, Location, PostingTime]
			except:
				print(json_file)

		jsons_data.to_csv('Jobs.csv', index=False)