from django.conf.urls import *

import vn2.views

urlpatterns = [
    # Examples:
    # url(r'^$', 'vn2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),



	url(r'^$', vn2.views.home),
        url(r'^md/$', vn2.views.render_md_blog),
	url(r'^blog/$', vn2.views.blog_base), 
	url(r'^base/$', vn2.views.simple_page('base.html')), 
	url(r'^scandit/$', vn2.views.simple_page('scandit.html')), 
	url(r'^scandit2/$', vn2.views.simple_page('scandit2.html')), 
	url(r'^resume/$', vn2.views.simple_page('resume.html')), 
	url(r'^portfolio/$', vn2.views.simple_page('portfolio.html')), 
	url(r'^address/$', vn2.views.simple_page('address.html')), 
	url(r'^blog/(.*)$', vn2.views.blog), 
	url(r'^test/$', vn2.views.test), 
	url(r'^jammer/$', vn2.views.jammer), 
	url(r'^.well-known/acme-challenge/p_LTkY9QHhcECb6Lv1UZWYQ6rawjuQLnUAdBdZZE9kk', vn2.views.file_a),
	url(r'^.well-known/acme-challenge/v9b5S4UbuLtvh_PwuhqjfOUnVfiulJSmFCYkNHtD6mA', vn2.views.file_b),


	url(r'^messages/whatyouwant$', vn2.views.simple_page('messages/isthiswhatyouwant.html')), 




]
