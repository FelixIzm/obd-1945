#d = 
#print(d)
d = {'image':True, 'excel':False}

def f2(id,image,excel):
    print('id = {}'.format(id))
    if(excel):
        print('excel')
    if(image):
        print('image')
f2(123,**d)