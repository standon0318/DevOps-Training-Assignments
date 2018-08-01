import pandas as pd
import os
frame = pd.DataFrame()
for filename in os.listdir(os.getcwd()):
    root, ext = os.path.splitext(filename)
    if ext == '.json':
        tmp_frame = pd.read_json(filename)
        frame = frame.append(tmp_frame, ignore_index=True)
        
frame.to_csv('output.csv', index=False)




def main():
   
    jsonparser("AWS Daily Report", [], "standon@tavisca.com", "Shashank@08", 'D:/DevOps-Training-Assignments/ReportingTool/email-scripts/response.json', 'ec2report', 'ec2','EC2 Health Report')
if __name__ == '__main__':
    main()