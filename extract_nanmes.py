import os
import xml.etree.ElementTree as ET

import os
import xml.etree.ElementTree as ET

def extract_labels(xml_dir, txt_path):
    labels = set()  # use a set to automatically remove duplicates

    # Go through each XML file in the directory
    for filename in os.listdir(xml_dir):
        if not filename.endswith('.xml'):
            continue

        # Parse the XML file
        tree = ET.parse(os.path.join(xml_dir, filename))
        root = tree.getroot()

        # Extract labels
        for obj in root.iter('object'):
            name = obj.find('name').text
            labels.add(name)  # add the label to the set

    # Save labels to .txt file
    with open(txt_path, 'w') as f:
        for label in labels:
            f.write(label + '\n')
# Usage
xml_dir = r'D:\VMRD_dataset\Annotations'  # Replace with your path
txt_path = 'labels.txt'  # Replace with your path
extract_labels(xml_dir, txt_path)
