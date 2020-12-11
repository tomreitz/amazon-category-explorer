import csv, json

# Load all rows from CSV:
rows = []
with open('all-nodes.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            # skip first (header) line
            line_count += 1
        else:
            rows.append(row)
            line_count += 1

# Helper function to convert rows to tree nodes:
def row_to_node(row):
    return {
        'id': int(row[0]),
        'name': ('Main' if row[1]=='root' else row[1]),
        'product_count': int(row[2]),
        'subtree_product_count': int(row[3]),
        'num_children': int(row[5]),
        'path': json.loads(row[6].replace("['",'["').replace("']",'"]').replace("', '",'", "').replace("', \"",'", "').replace("\", '",'", "').replace('" ','\\" ').replace('")','\\")') ),
        'children': [],
        'also_count': row[8],
        'also_ids': row[9]
    }

# Helper function to (recursively) find child nodes:
def get_child_nodes(node):
    node['children'] = [ get_child_nodes(row_to_node(row)) for row in rows if int(row[4]) == node['id'] and int(row[0]) != node['id'] ]
    return node

# Build up tree from root:
root = get_child_nodes(row_to_node(rows[0]))
print('data = '+json.dumps(root, separators=(',', ':'))) #, indent=4))
