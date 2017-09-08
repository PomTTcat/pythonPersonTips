# -*- coding: utf-8 -*-

gloCount = 0


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])

    global gloCount
    gloCount += 1
    print gloCount

    # host后面的是?之前的是PATH_INFO
    print 'PATH_INFO:', environ['PATH_INFO']
    print 'wsgi.input', environ['wsgi.input']

    # ?name=John ?后面的是QUERY_STRING
    print 'QUERY_STRING:', environ['QUERY_STRING']

    pathInfo = environ['PATH_INFO']
    enMethod = environ['REQUEST_METHOD']
    if pathInfo == '/' and enMethod == 'GET':
        return '<h1>Home</h1>'

    if pathInfo == '/signin' and enMethod == 'GET':
        return signin_form()

    if pathInfo == '/signin' and enMethod == 'POST':
        print 'input:', self._environ['wsgi.input']
        return 'this is a good post'

    return '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'web')

# http://localhost:8000/


# @app.route('/', methods=['GET', 'POST'])
# def home():
#     return '<h1>Home</h1>'

# # http://localhost:8000/signin


# @app.route('/signin', methods=['GET'])
def signin_form():
    return '''<form action="/signin" method="post">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">Sign In</button></p>
              </form>'''

# # http://localhost:8000/signin


# @app.route('/signin', methods=['POST'])
# def signin():
#     import sys
#     sys.stdout.write('hellllll')
#     # 需要从request对象读取表单内容：
#     if request.form['username'] == 'admin' and request.form['password'] == 'password':
#         return '<h3>Hello, admin!</h3>'
#     return '<h3>Bad username or password.</h3>'

'''
------
WebKitFormBoundaryQQ3J8kPsjFpTmqNz\nContent-Disposition: form-data; name=\"name\"\n\nScofield\n------
WebKitFormBoundaryQQ3J8kPsjFpTmqNz\nContent-Disposition: form-data; name=\"name\"\n\nLincoln\n------
WebKitFormBoundaryQQ3J8kPsjFpTmqNz\nContent-Disposition: form-data; name=\"file\"; filename=\"test.txt\"\nContent-Type: text/plain\n\njust a test\n------
WebKitFormBoundaryQQ3J8kPsjFpTmqNz\nContent-Disposition: form-data; name=\"id\"\n\n4008009001\n------
WebKitFormBoundaryQQ3J8kPsjFpTmqNz--\n
'''

'''

Key	Contents
PATH_INFO	请求路径，比如 /foo/bar/
QUERY_STRING	GET 请求参数，比如 foo=bar&bar=spam，我们可以从这个变量中获取用户的请求参数
HTTP_{HEADER}	http 头信息，比如 HTTP_HOST 等
wsgi.input	包含请求内容的类文件对象(file-like object)，比如 post 请求数据

http://localhost:8000/?name=John

'''
