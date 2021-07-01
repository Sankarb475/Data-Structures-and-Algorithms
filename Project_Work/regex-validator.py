# ===========================================================================
# Purpose : Validates regex against the raw logs as a pre-requisite for onboarding
# Parameters : None
# Usage : python regex_validator.py
# Author : Sankar Biswas
# Notes : Assumptions
#			1. Input excel sheet should be in .xls format
#			2. Input excel sheet should have pre-defind format i.e. columns
# Version : 0.1 - Initial Version - Sankar Biswas - 16/04/2021
#			1.0 - Added regex/SQL files creation and additional validations - Sankar Biswas - 25/06/2021
# ============================================================================

import re
import xlrd
import sys
import datetime
import json

regex_details={}

def get_config_file_name(application_name):
	"""
	Get config file name from application name
	"""
	return re.sub('[^A-Za-z0-9]+','_',application_name)

def get_field_names(fields):
	"""
	Get field names
	"""
	fields=list(tuple(map(str, fields.split(','))))
	list_index=0
	for field in fields:
		if field.lower() == "date":
			fields[list_index]="Date"
		if field.lower() == "time":
			fields[list_index]="Time"
		if field.lower() == "descriptor":
			fields[list_index]="Descriptor"
		list_index=list_index+1
	field_names=tuple(fields)
	return field_names


def get_filebeat_message(raw_message):
	"""
	Converts raw message in format that would be received from filebeat
	"""
	return raw_message.replace("\"","\\\"")

def escape_sql_values(field_value):
	"""
	Escape special characters in SQL values such as '
	"""
	return field_value.replace("'","''")

def escape_logpath(logpath):
	"""
	Escape log path
	"""
	return logpath.replace("/","\\/")

def escape_regex(regex):
	"""
	Escape special characters for parsing
	"""
	#regex=regex.replace(".*",".*?")

	if(not regex.startswith('^')):
		regex="^"+regex
	
	if(not regex.endswith('$')):
		regex=regex+".*$"
	
	regex=regex.replace("\"","\\\\\"")
	
	return regex

def escape_regex_for_config(regex):
	"""
	Escape special characters as expected by config file
	"""
	if(not regex.startswith('^')):
		regex="^"+regex
	if(not regex.endswith('$')):
		regex=regex+".*$"
	return regex.replace("\"","\\\"")

def concat_field_names(field_names):
	"""
	Print field names in a comma-separated format
	"""
	return ",".join(field_names)

def remove_mandatory_field(field_names):
	"""
	Removes mandatory fields from field names to create grouping columns
	"""
	if (field_names not in "Date") and (field_names not in "Time") and (field_names not in "Descriptor"):
		return True
	else:
		return False

def concat_grouping_field_names(field_names):
	"""
	Prints the list of field names which are required for grouping 
	"""
	additional_fields = filter(remove_mandatory_field,field_names)
	return ",".join(additional_fields)


def print_number_of_fields(field_names):
	"""
	Prints the number of fields e.g. For n fields, it will print 1,2,...n
	"""
	number_of_fields=len(field_names)
	return ",".join(map(str,[*range(1,number_of_fields+1)]))

def get_all_regex_details(id, regex):
	"""
	Sets up the variables required for config file and SQL file for every regex
	"""
	appsubname_regex_details={}
	try:
		appsubname_regex_details['APPLICATION_NAME']=regex['APPLICATION_NAME']
		appsubname_regex_details['app_sub_name']=regex['APP_NAME_IN_LOGS']
		appsubname_regex_details['sub_app_logname_pattern']=escape_logpath(regex['LOGFILE_NAME_FULL_PATH'])
		appsubname_regex_details['PATTERN']=regex['PATTERN']
		appsubname_regex_details['pattern_filter']=str(escape_regex_for_config(regex['PATTERN_FILTER']))
		appsubname_regex_details['PATTERN_CAPTURE_IN_UNIX']=regex['PATTERN_CAPTURE_IN_UNIX']
		appsubname_regex_details['pattern_capture']=str(escape_regex_for_config(regex['PATTERN_CAPTURE_PERL']))
		appsubname_regex_details['capture_vars']=str(print_number_of_fields(get_field_names((regex['FIELD_NAMES']))))
		appsubname_regex_details['print_vars']=str(print_number_of_fields(get_field_names(regex['FIELD_NAMES'])))
		appsubname_regex_details['mandatory_fields']='Descriptor'
		appsubname_regex_details['field_names']=concat_field_names(get_field_names(regex['FIELD_NAMES']))

		grouping_fields=concat_grouping_field_names(get_field_names(regex['FIELD_NAMES']))
		if(len(grouping_fields)>0):
			appsubname_regex_details['GROUPING']='appname,Descriptor,TSMIN,HPAM_IP,HOSTNAME,app_sub_name,Type,category,subcategory,application_code,application_ngo_code,'+grouping_fields
		else:
			appsubname_regex_details['GROUPING']='appname,Descriptor,TSMIN,HPAM_IP,HOSTNAME,app_sub_name,Type,category,subcategory,application_code,application_ngo_code'
		appsubname_regex_details['execute_gmt_correction']='0'
		appsubname_regex_details['AGGREGATION']=regex['AGGREGATION']
		appsubname_regex_details['RULE_PUT_ON']=regex['RULE_PUT_ON']
		appsubname_regex_details['DESCRIPTOR_CATEGORY']=regex['DESCRIPTOR_CATEGORY']
		appsubname_regex_details['RAW_LOGS']=regex['RAW_LOGS']
		appsubname_regex_details['SAMPLELOGS']=regex['SAMPLE_LOGS']
		appsubname_regex_details['preprocess_log_construct']='plain'
		appsubname_regex_details['post_parse_translators']='Descriptor;injectenvmapid_instanceid'
		regex_details[id]=appsubname_regex_details.copy()
		
	except Exception as e:
		print("Some error occurred in get_all_regex_details")
		print(e)

	appsubname_regex_details.clear()


def write_deser_config_file(appsubname_regex_details, config_file_handler):
	"""
	Writes deserialized config file to be feed into Parsing jobs
	"""
	try:
		config_file_handler.write("\n"+"app_sub_name="+appsubname_regex_details['app_sub_name']+"\n")
		config_file_handler.write("sub_app_logname_pattern="+appsubname_regex_details['sub_app_logname_pattern']+"\n")
		config_file_handler.write("pattern_filter="+appsubname_regex_details['pattern_filter']+"\n")
		config_file_handler.write("pattern_capture="+appsubname_regex_details['pattern_capture']+"\n")
		config_file_handler.write("capture_vars="+appsubname_regex_details['capture_vars']+"\n")
		config_file_handler.write("print_vars="+appsubname_regex_details['print_vars']+"\n")
		config_file_handler.write("mandatory_fields="+appsubname_regex_details['mandatory_fields']+"\n")
		config_file_handler.write("field_names="+appsubname_regex_details['field_names']+"\n")
		config_file_handler.write("execute_gmt_correction="+appsubname_regex_details['execute_gmt_correction']+"\n")
		config_file_handler.write("preprocess_log_construct="+appsubname_regex_details['preprocess_log_construct']+"\n")
		config_file_handler.write("post_parse_translators="+appsubname_regex_details['post_parse_translators'])
	except Exception as e:
		print("Some error occurred in write_deser_config_file")
		print(e)

def write_sql_file(appsubname_regex_details, dml_file_handler, ngo_app_code, app_id, envmapid):
	"""
	Writes INSERT scripts in a SQL file which can be used to insert KPIs in ngo_app_regex_api
	"""
	try:
		cmd="INSERT INTO ngo_app_regex_api(applicationname, logpath, appnameinparsedlogs, pattern, patternfilter, patterncaptureinunix, patterncaptureinperl, fieldnames, grouping, aggregation, rule, descriptorcategory, rawlogs, samplelogs, ngo_app_code, category, catperfexc, identifier, appid, updated_from_config, envmapid) VALUES ('"+escape_sql_values(appsubname_regex_details['APPLICATION_NAME'])+"', '"+escape_sql_values(appsubname_regex_details['sub_app_logname_pattern'])+"', '"+escape_sql_values(appsubname_regex_details['app_sub_name'])+"', '"+escape_sql_values(appsubname_regex_details['PATTERN'])+"', '"+escape_sql_values(appsubname_regex_details['pattern_filter'])+"', '"+escape_sql_values(appsubname_regex_details['PATTERN_CAPTURE_IN_UNIX'])+"', '"+escape_sql_values(appsubname_regex_details['pattern_capture'])+"', '"+escape_sql_values(appsubname_regex_details['field_names'])+"', '"+escape_sql_values(appsubname_regex_details['GROUPING'])+"', '"+escape_sql_values(appsubname_regex_details['AGGREGATION'])+"', '"+escape_sql_values(appsubname_regex_details['RULE_PUT_ON'])+"', '"+escape_sql_values(appsubname_regex_details['DESCRIPTOR_CATEGORY'])+"', '"+escape_sql_values(appsubname_regex_details['RAW_LOGS'])+"', '"+escape_sql_values(appsubname_regex_details['SAMPLELOGS'])+"', '"+str(ngo_app_code)+"', '"+"ALL"+"', "+"NULL"+", "+"NULL"+", "+str(app_id)+", "+"SYSDATE"+", "+str(envmapid)+");"
		dml_file_handler.write(cmd+"\n")
	except Exception as e:
		print("Some error occurred in write_sql_file")
		print(e)

def validate_fields_count(pattern_capture_perl_groups, field_names):
	"""
	Validates whether number of fields mentioned in excel matches
	with the number of fields generated after parsing raw logs with regex
	"""
	try:		
		if(len(pattern_capture_perl_groups.groups()) == len(field_names)):
			print("Field Count Validation     => SUCCESSFUL. Number of input fields match with number of parsed fields")
			for field_index in range(len(field_names)):
				pattern_capture_perl_groups.group(field_index)
		else:
			print("Field Count Validation     => FAILED. Number of input fields ("+str(len(field_names))+") do not match with number of parsed fields ("+str(len(pattern_capture_perl_groups.groups()))+")")
			print("                              Given: "+str(field_names))
			print("                              Parsed: "+str(pattern_capture_perl_groups.groups()))
			#sys.exit(1)

	except Exception as e:
		print("Field Count Validation     => FAILED. Some error occurred in validate_fields_count")
		print(e)
		#sys.exit(1)

def validate_parsed_fields_format(pattern_capture_perl_groups, field_names):
	"""
	Field level pre-requisites are validated. 
	For example, date and time should be in specific format, etc
	"""
	parsed_output={}
	try:
		if "Descriptor" not in field_names:
			print("Field Format Validation    => FAILED. Mandatory fields \"Descriptor\" not provided.")
		group_number=1
		for field in field_names:
			if field == "Date":
				try:
					datetime.datetime.strptime(pattern_capture_perl_groups.group(group_number), '%Y-%m-%d')
					parsed_output[field]=pattern_capture_perl_groups.group(group_number)
				except ValueError as e:
					print("Field Format Validation    => FAILED. FieldName: \""+field+"\", Expected: \"yyyy-MM-dd\", Received: \""+pattern_capture_perl_groups.group(group_number)+"\", Error: \""+str(e)+"\"")
					parsed_output[field]=pattern_capture_perl_groups.group(group_number)
					#print(e)
					#sys.exit(1)
			elif field == "Time":
				try:
					datetime.datetime.strptime(pattern_capture_perl_groups.group(group_number), '%H:%M:%S')
					parsed_output[field]=pattern_capture_perl_groups.group(group_number)
				except ValueError as e:
					print("Field Format Validation    => FAILED. FieldName: \""+field+"\", Expected: \"HH:MI:SS\", Received: \""+pattern_capture_perl_groups.group(group_number)+"\", Error: \""+str(e)+"\"")
					parsed_output[field]=pattern_capture_perl_groups.group(group_number)
					#print(e)
					#sys.exit(1)
			else:
				parsed_output[field]=pattern_capture_perl_groups.group(group_number)
			
			group_number=group_number+1
	
	except Exception as e:
		print("Field Format Validation    => FAILED. Some error occurred in validate_parsed_fields_format")
		print(e)
		#sys.exit(1)
	return parsed_output

def parse_validate_pattern_capture_perl(pattern_capture_perl, raw_logs, fields):
	"""
	parses the raw logs with regex and generates the parsed fields.
	"""
	try:
		pattern_capture_perl_groups=re.search(pattern_capture_perl,raw_logs)

		if pattern_capture_perl_groups is not None:
			field_names=res = get_field_names(fields)

			validate_fields_count(pattern_capture_perl_groups,field_names)
			parsed_output=validate_parsed_fields_format(pattern_capture_perl_groups,field_names)
			print("Pattern Capture Validation => SUCCESSFUL")
			print("Output Parsed Fields       => "+json.dumps(parsed_output))
			
		else:
			print("Pattern Capture Validation => FAILED. No match found for parse_validate_pattern_capture_perl")
			#sys.exit(1)

	except Exception as e:
		print("Pattern Capture Validation => FAILED. Some error occurred in parse_validate_pattern_capture_perl")
		#sys.exit(1)

	return pattern_capture_perl_groups


def validate_pattern_filter(pattern_filter, raw_logs):
	"""
	parses the raw logs with filter pattern
	"""
	try:
		pattern_filter_groups=re.match(pattern_filter,raw_logs)

		if pattern_filter_groups is not None:
			#print(pattern_filter_groups.group())
			print("Pattern Filter Validation  => SUCCESSFUL")
		else:
			print("Pattern Filter Validation  => FAILED. No match found for validate_pattern_filter")
			#sys.exit(1)

	except Exception as e:
		print("Pattern Filter Validation  => FAILED. Some error occurred in validate_pattern_filter")
		#sys.exit(1)

def read_regex_template(filename):
	"""
	Read the input excel sheet with all regex details
	"""
	try:
		wb=xlrd.open_workbook(filename)
		ws=wb.sheet_by_index(0)
	except Exception as e:
		print("Some error occurred in read_regx_template")
		sys.exit(1)
	return ws

def get_all_regex(worksheet):
	"""
	get all the regex information in a dictionary
	"""
	header=[]
	all_regex=[]
	try:
		for row_num in range(worksheet.nrows):
			if(row_num==0):
				header=worksheet.row(row_num)
			else:
				regex_info={}
				for col_num in range(worksheet.ncols):
					regex_info[header[col_num].value]=worksheet.cell_value(rowx=row_num, colx=col_num)
				all_regex.append(regex_info)
	except Exception as e:
		print("Some error occurred in get_all_regex")
		print(e)
		sys.exit(1)
	return all_regex

def validate_regex_details(regex):
	"""
	Validates each regex one-by-on
e	"""
	try:
		validate_pattern_filter(escape_regex(regex['PATTERN_FILTER']),get_filebeat_message(regex['RAW_LOGS']))
		parse_validate_pattern_capture_perl(escape_regex(regex['PATTERN_CAPTURE_PERL']),get_filebeat_message(regex['RAW_LOGS']),regex['FIELD_NAMES'])
	except Exception as e:
		print("Some error occurred in validate_regex_details")
		#sys.exit(1)


def print_regex_banner(regex):
	an_flag=False
	pcp_flag=False
	rl_flag=False

	if(('APP_NAME_IN_LOGS' in regex and regex['APP_NAME_IN_LOGS'].strip() != "")):
		print("APP_NAME_IN_LOGS => "+regex['APP_NAME_IN_LOGS'])
		an_flag=True
	else:
		print("APP_NAME_IN_LOGS => "+"")

	if(('PATTERN_CAPTURE_PERL' in regex and regex['PATTERN_CAPTURE_PERL'].strip() != "")):
		print("REGEX => "+regex['PATTERN_CAPTURE_PERL'])
		pcp_flag=True
	else:
		print("REGEX => "+"")

	if(('RAW_LOGS' in regex and regex['RAW_LOGS'].strip() != "")):
		print("RAW_LOGS => "+regex['RAW_LOGS'])
		rl_flag=True
	else:
		print("RAW_LOGS => "+"")

	if(an_flag and pcp_flag and rl_flag):
		return True
	else:
		return False


def main():
	ngo_app_code=100
	app_id=200
	envmapid=300
	input_file_name="Template_REGEX_JSMS.xls"
    input_path = "C:/Users/sankar.biswas/Documents/Work/TestProjects/Python/"
	try:
		# Sample test data
		#raw_logs="2019-06-24 05:30:40,274 WARN  [600e87692c5a9871, 600e87692c5a9871, true] [c.z.w.c.ControllerExceptionHandler] Validation error Failed to establish connection. org.apache.hive.jdbc.ZooKeeperHiveClientException: Unable to read HiveServer2 configs from ZooKeeper"
		#pattern_capture_perl=r"^(.*) (.*),.*WARN.* (.*),.*jdbc.*\: (.*).*$"
		#pattern_filter=r".*ControllerExceptionHandler.*org.apache.hive.jdbc.ZooKeeperHiveClientException.*HiveServer2.*ZooKeeper.*"
		
		worksheet=read_regex_template(input_path+input_file_name)
		all_regex=get_all_regex(worksheet)
		id=1
		for regex in all_regex:
			print("---------------------------------------------------------")
			valid=print_regex_banner(regex)
			if(valid):
				print("---------------------------------------------------------")
				validate_regex_details(regex)
				get_all_regex_details(id, regex)
				#createInsertStatement(regex, '1559', '1309', '6599')
			id=id+1

		"""		
		with open(input_path+get_config_file_name(regex['APPLICATION_NAME'])+"_DML.sql","w") as dml_file_handler:
			for ins in DB_INS_REGEX.keys():
				dml_file_handler.write(DB_INS_REGEX[ins])
				dml_file_handler.write("\n")
		
		with open(input_path+get_config_file_name(regex['APPLICATION_NAME'])+"_config.cfg","w") as config_file_handler:
			for regex in all_regex:
				write_config_file(regex,config_file_handler)

		"""
		config_file_handler=open(input_path+get_config_file_name(regex['APPLICATION_NAME'])+"_config.cfg","w")
		dml_file_handler=open(input_path+get_config_file_name(regex['APPLICATION_NAME'])+"_DML.sql","w")
		for regex_id in range(1,len(regex_details.keys())+1):
			write_deser_config_file(regex_details[regex_id],config_file_handler)
			write_sql_file(regex_details[regex_id],dml_file_handler,ngo_app_code,app_id,envmapid)

		config_file_handler.close()				
		dml_file_handler.close()

	except Exception as e:
		print("Some error occurred in main")
		print(e)
		sys.exit(1)

if __name__ == "__main__":
	main()


