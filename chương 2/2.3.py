from xml.dom import minidom

doc = minidom.parse('sample.xml')
company_name = doc.getElementsByTagName('name')[0].firstChild.data
print(f"Company Name: {company_name}")
staffs = doc.getElementsByTagName('staff')

for staff in staffs:
    staff_id = staff.getAttribute('id')
    staff_name = staff.getElementsByTagName('name')[0].firstChild.data
    staff_salary = staff.getElementsByTagName('salary')[0].firstChild.data
    
    print(f"Staff ID: {staff_id}")
    print(f"Staff Name: {staff_name}")
    print(f"Staff Salary: {staff_salary}")
    print("-" * 20)
