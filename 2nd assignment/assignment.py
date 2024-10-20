# Global dictionary to simulate multiple collections 
collections = {}

# Function Definitions 

def createCollection(p_collection_name):
    """Creates an empty collection (dictionary) with the provided name."""
    if p_collection_name not in collections:
        collections[p_collection_name] = []
        print(f"Collection '{p_collection_name}' created.")
    else:
        print(f"Collection '{p_collection_name}' already exists.")

def indexData(p_collection_name, p_exclude_column):
    """Indexes sample employee data into the collection, excluding the specified column."""
    if p_collection_name not in collections:
        print(f"Collection '{p_collection_name}' does not exist.")
        return
    
    # Sample employee data (as a list of dictionaries) 
    employee_data = [
        {'EmployeeID': 'E02001', 'Name': 'John Doe', 'Department': 'IT', 'Gender': 'Male'},
        {'EmployeeID': 'E02002', 'Name': 'Jane Doe', 'Department': 'HR', 'Gender': 'Female'},
        {'EmployeeID': 'E02003', 'Name': 'Sam Smith', 'Department': 'Finance', 'Gender': 'Male'},
        # Add more sample data if needed 
    ]
    
    # Exclude the specified column 
    for employee in employee_data:
        if p_exclude_column in employee:
            del employee[p_exclude_column]
        collections[p_collection_name].append(employee)
    
    print(f"Data indexed into collection '{p_collection_name}' with column '{p_exclude_column}' excluded.")

def searchByColumn(p_collection_name, p_column_name, p_column_value):
    """Searches the collection for records where the specified column matches the given value."""
    if p_collection_name not in collections:
        print(f"Collection '{p_collection_name}' does not exist.")
        return
    
    results = [record for record in collections[p_collection_name] if record.get(p_column_name) == p_column_value]
    print(f"Search results in collection '{p_collection_name}' where '{p_column_name}' is '{p_column_value}':")
    for result in results:
        print(result)

def getEmpCount(p_collection_name):
    """Returns the count of employees (records) in the specified collection."""
    if p_collection_name not in collections:
        print(f"Collection '{p_collection_name}' does not exist.")
        return
    
    count = len(collections[p_collection_name])
    print(f"Employee count in collection '{p_collection_name}': {count}")
    return count

def delEmpById(p_collection_name, p_employee_id):
    """Deletes an employee by their EmployeeID from the specified collection."""
    if p_collection_name not in collections:
        print(f"Collection '{p_collection_name}' does not exist.")
        return
    
    initial_count = len(collections[p_collection_name])
    collections[p_collection_name] = [record for record in collections[p_collection_name] if record.get('EmployeeID') != p_employee_id]
    
    if len(collections[p_collection_name]) < initial_count:
        print(f"Employee with ID '{p_employee_id}' deleted from collection '{p_collection_name}'.")
    else:
        print(f"No employee found with ID '{p_employee_id}' in collection '{p_collection_name}'.")

def getDepFacet(p_collection_name):
    """Retrieves the count of employees grouped by department in the specified collection."""
    if p_collection_name not in collections:
        print(f"Collection '{p_collection_name}' does not exist.")
        return
    
    department_count = {}
    for record in collections[p_collection_name]:
        department = record.get('Department')
        if department:
            department_count[department] = department_count.get(department, 0) + 1
    
    print(f"Employee count grouped by department in collection '{p_collection_name}':")
    for dept, count in department_count.items():
        print(f"Department: {dept}, Count: {count}")


# Function Executions 
v_nameCollection = 'Hash_<Mahima>'
v_phoneCollection = 'Hash_<8411>'

# Create collections 
createCollection(v_nameCollection)
createCollection(v_phoneCollection)

# Get employee count before indexing 
getEmpCount(v_nameCollection)

# Index data excluding certain columns 
indexData(v_nameCollection, 'Department')
indexData(v_phoneCollection, 'Gender')

# Delete an employee by ID 
delEmpById(v_nameCollection, 'E02003')

# Get employee count after deletion 
getEmpCount(v_nameCollection)

# Search records by column 
searchByColumn(v_nameCollection, 'Department', 'IT')
searchByColumn(v_nameCollection, 'Gender', 'Male')
searchByColumn(v_phoneCollection, 'Department', 'IT')

# Get department facet (group by department) 
getDepFacet(v_nameCollection)
getDepFacet(v_phoneCollection)
