import webapp2
import jinja2
import os

jinja_environment = jinja2.Environment(
	loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainPage(webapp2.RequestHandler):
	def get(self):

		greet = "hello there"

		template_values = {
		'greeting': greet,
		}

		template = jinja_environment.get_template('views/index.html')
		self.response.out.write(template.render(template_values))


app = webapp2.WSGIApplication(
							[('/',MainPage)], debug=True)

