from PatternDAO import patternDAO

pattern = {'patternID':'B7012',
           'brand': 'Butterick',
           'category': 'Skirt',
           'fabric_type': 'Woven',
           'description': 'Flared skirt',
           'ownerID': 1
           }

#returnValue = patternDAO.create(pattern)

# View All
#returnValue = patternDAO.getAll()
#print(returnValue)


#print("Find By pattern Id")
#returnValue = patternDAO.findByID('V9075')
#print(returnValue)


#print("find By Brand")
#returnValue = patternDAO.findByBrand('Vogue')
#print(returnValue)


#print("Find By Category")
#returnValue = patternDAO.findByCategory('Dress')
#print(returnValue)


#print("Find By Fabric Type")
#returnValue = patternDAO.findByFabric('Woven')
#print(returnValue)


#print("Find By Owner Name")
#returnValue = patternDAO.findByOwner('Irene')
#print(returnValue)

#print('Update a pattern')
#returnValue = patternDAO.update('B7012', pattern)
#print(returnValue)

print('Delete a pattern')
returnValue = patternDAO.delete('B7012')
print('Pattern deleted')


