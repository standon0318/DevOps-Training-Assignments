import json, ast
from pprint import pprint
from emailReport import send_report_on_email 
    

def jsonparser(email_subject, receivers_email_id, senders_email_id, senders_email_password, json_file_path, json_start_param, json_service_name_param, report_name):
    
    table = ''

    with open(r''+json_file_path) as file:
        try:
            aws_resources = []
            json_keys = []
            json_values = []
            json_data = json.load(file)
            aws_resource_data = json_data.get(json_start_param).get(json_service_name_param)
        
            for resource in aws_resource_data:
                aws_resources.append(resource)
        
            for resource_tags in aws_resources:
                resource_tags_data = json_data.get(json_start_param).get(json_service_name_param).get(str(resource_tags))
            
                for  resource_tags_data_key in resource_tags_data:
                    json_keys.append(resource_tags_data_key)
                    aws_resource_data_values = json.dumps(json_data.get(json_start_param).get(json_service_name_param).get(str(resource_tags)).get(str(resource_tags_data_key)))
                    json_values.append(aws_resource_data_values)   
                table += tablebuilder(json_keys, json_values, str(resource_tags).upper())
                json_keys = []
                json_values = []
            send_report_on_email(email_subject, receivers_email_id, senders_email_id, table, senders_email_password, report_name)
        except IOError:
            print('An error occurred while trying to read the file.')
    

def tablebuilder(keys, values, resource): 
    table = '<tr>{}</tr>'.format(''.join('<td class="resource">{}</td>'.format(resource)))
    table_row = '</tr><tr><br /></tr>'
    table += '<tr>{}</tr>'.format(''.join(['<th class="cell">{}</th>'.format(str(header).upper()) for header in keys])) 
    table_row += '<tr>' 
    for value in values:
        value = value.replace('[', ' ')
        value = value.replace(']', ' ')
        table_row += '<td class="cell">{}</td>'.format(value) 
    table_row += '</tr><tr><br /></tr>' 
    table += table_row
    return table
