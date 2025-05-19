from PatternDAO import patternDAO

# Test that the functions in PatternDAO are working correctly.
pattern = {'patternID':'B7012',
           'brand': 'Butterick',
           'category': 'Skirt',
           'fabric_type': 'Woven',
           'format': 'Paper',
           'description': 'Flared skirt',
           'ownerID': 1
           }

# Create the pattern
returnValue = patternDAO.create(pattern)

# View All
#returnValue = patternDAO.getAll()
#print(returnValue)

# Find by pattern ID
#print("Find By pattern Id")
#returnValue = patternDAO.findByID('V9075')
#print(returnValue)

# Find by brand
#print("find By Brand")
#returnValue = patternDAO.findByBrand('Vogue')
#print(returnValue)

# Find by category
#print("Find By Category")
#returnValue = patternDAO.findByCategory('Dress')
#print(returnValue)

# Find by fabric type
#print("Find By Fabric Type")
#returnValue = patternDAO.findByFabric('Woven')
#print(returnValue)

# Find by format
#print("Find by Format")
#returnValue = patternDAO.findByFormat('Paper')
#print(returnValue)

# Find by userID
#print("Find By userID")
#returnValue = patternDAO.findByUserID('Irene')
#print(returnValue)

# Update a pattern
#print('Update a pattern')
#returnValue = patternDAO.update('B7012', pattern)
#print(returnValue)

# Delete a pattern
#print('Delete a pattern')
#returnValue = patternDAO.delete('B7012')
#print('Pattern deleted')


