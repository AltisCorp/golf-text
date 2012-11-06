#!/usr/bin/env python
import sys, os
import web

try:
    import mymodel
except ImportError:
    sys.path.append(os.path.dirname(__file__))
    try:
        import mymodel
    finally:
        sys.path.remove(os.path.dirname(__file__))

try:
	import controller
except ImportError:
	sys.path.append(os.path.dirname(__file__))
	try:
		import controller
	finally:
		sys.path.remove(os.path.dirname(__file__))


web.config.debug = False

urls = (
	'/', 'index',
	'/create_player', 'create_player',
	'/add_score', 'add_score',
	'/create_round', 'create_round',
	'/join_round', 'join_round',
	'/get_score', 'get_score',
)

render = web.template.render('/var/www/templates', cache=False)

class index:
	def GET(self,data):
		web.header('Content-Type', 'text/xml')
#		return render.response("19366451048", data)
	def POST(self):
		data = web.input()
		res = controller.handle(data.From, data.Text.lower(), data.Type)
		web.header('Content-Type', 'text/xml')
		return render.response(data.From, res)

app = web.application(urls, globals(), autoreload=False)
application = app.wsgifunc()
