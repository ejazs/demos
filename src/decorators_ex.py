def prefix(url):
  def is_user_loggedin(func):
    def wrapper(request):
      print('In wrapper')
      if request['is_authenticated'] == True:
        return func(request)
      return NameError('Not logged in, go {} and login.'.format(url))

    return wrapper
  return is_user_loggedin

@prefix(url='user/login')
def home(request):
  return {'username':request['username']}




request = {'username':'Ejaz', 'is_authenticated':False}

ejaz = home(request=request)
print(ejaz)