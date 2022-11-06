import json
import uuid
import urllib
import datetime
import re 
import requests # for setting cookies

from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic.base import RedirectView
from django.utils import timezone
from django.contrib import auth
#from django.forms.util import ErrorList
from django.template.context import RequestContext
from django.shortcuts import render
from django.shortcuts import render, redirect, render
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required

import markdown
md = markdown.Markdown()

#import requests

from vn2.util import *
def simple_page(template):
	def handler(request):
		return renderWithNav(request, template)
	return handler

def file_a(request):
	return HttpResponse("7GN_wPd4X1PrCxmqKOrw9sHsAd0_uayFhOnWdEw6Ytc.HrFduo8MJADNQACN38q371h8yDpWwuARiTcP3lgNOOM")
def file_b(request):
	return HttpResponse("v9b5S4UbuLtvh_PwuhqjfOUnVfiulJSmFCYkNHtD6mA.myqbUoOfbuYMTb3HuxVonYYuwHgoAV2835bCeWTwqkY")




def blog_base(request):
	return blog(request,None)

def blog(request,blog):
	if blog is None:
		obj = {}
		obj['blogs'] = []
		obj['blogs'].append(
		{
			"url":"while-vr-for-consumer-lags-corporate-training-booms.html",
			"title":"While VR for consumers lags, Corporate Training booms",
                        "description":"My views on the current market, and why I'm long on corporate VR ahead of consumer VR by 10-20 years.",
			"date":"Jan 14, 2018"
		})
		obj['blogs'].append(
		{
			"url":"virtual-reality-bridges-gamer-gap.html",
			"title":"Virtual Reality Bridges the Gamer Gap",
                        "description":"By getting out of the way of human users, VR paves the way for seameless HCI.",
			"date":"Mar 25, 2018"
		})
		obj['blogs'].append(
		{
			"url":"freedom-from-the-tyrants-deep-monkey.html",
			"title":"Freedom From The Tyrants",
                        "description":"Everyone knows tech giants rule us, but you will have more options in the future.",
			"date":"Mar 27, 2018"
		})

		obj['blogs'].append(
		{
			"url":"sustainable-futures-are-collaborative-not-adversarial.html",
			"title":"Sustainable Futures Are Collaborative Not Adversarial",
                        "description":"My unsupported arguments for world piece, rooted in capitalism.",
                        "date":"April 7, 2018"
		})

		obj['blogs'].append(
		{
			"url":"spacefrogvr.html",
			"title":"Space Frog VR",
                        "description":"A brief look at my first full-length VR title.",
                        "date":"Mar 17, 2019"
		})

		obj['blogs'].append(
		{
			"url":"redefinelearning.html",
			"title":"Redefine Schools and Learning",
                        "description":"Schools do not set students up for success in today's world. Here's what I plan to change.",
                        "date":"Sep 20, 2020"
		})

#		{
#			"url":"these-vr-startups-are-rocking-the-medical-world.html",
#			"title":"[IN PROGRESS] These VR Startups are rocking the medical world",
#			"date":"Feb 6, 2018"
#		})


		obj['blogs'].reverse()
		return renderWithNav(request,"blogbase.html",obj)
	else:
		return renderWithNav(request,"blog/"+blog)

def render_md_blog(request):
    with open('vn2/templates/blog/redefinelearning.md', 'rb') as fp:
        v = fp.read()
        v = md.convert(v)
        obj = {}
        obj['html_text'] = v
        return renderWithNav(request,"render_md_blog.html", obj)


def jammer(request):
	obj = {}
	obj['videos'] = []
	obj['videos'].append({
		"url" : "https://www.youtube.com/watch?v=ogH7yrA-fHc",
		"id" : "ogH7yrA-fHc",
		"hotkey" : "F",
		"keycode" : 102
	})
	obj['videos'].append({
		"url" : "https://www.youtube.com/watch?v=2EUOYON3eZg",
		"id" : "2EUOYON3eZg",
		"hotkey" : "J",
		"keycode" : 106
	})
	obj['videos'].append({
		"url" : "https://www.youtube.com/watch?v=kuMY2X22PHA",
		"id" : "kuMY2X22PHA",
		"hotkey" : "D",
		"keycode" : 100
	})
	obj['videos'].append({
		"url" : "https://www.youtube.com/watch?v=2EUOYON3eZg",
		"id" : "2EUOYON3eZg",
		"hotkey" : "S",
		"keycode" : 115
	})
	obj['videos'].append({
		"url" : "https://www.youtube.com/watch?v=mKYb7Juflz0",
		"id" : "mKYb7Juflz0",
		"hotkey" : "A",
		"keycode" : 97
	})
	return renderWithNav(request,'jammer.html', obj)
	
def home(request):
	obj = {}
	obj['works'] = []
	obj['works'].append({
		"title" : "Secret VR Game",
		"background" : "",
		"position" : "Monkey Wizard",
		"link" : "",
		"date" : "Summer 2020",
        	"description" : "Early prototype. Magical powers of cube control. Written for Quest using Unity3D",
		"video" : { 
			"source": "https://player.vimeo.com/video/435624506", 
			"image" : "" 
		},
		"images" : [	
		],
	})
	obj['works'].append({
		"title" : "Admirals of Adaris VR",
		"background" : "",
		"position" : "Developer, Game Designer",
		"link" : "https://www.havik.us",
		"date" : "2019",
		"description" : "A multiplayer VR experience where you build and control a fleet of ships in space.",
		"video" : { 
			"source": "https://player.vimeo.com/video/362128849", 
			"image" : "" 
		},
		"images" : [	
		],
	})
	obj['works'].append({
		"title" : "Military Training VR Sim",
		"background" : "",
		"position" : "Developer, Game Designer",
		"link" : "https://www.havik.us",
		"date" : "2019",
		"description" : "A simulation for Air Force equipment and procedure training. Features include weather control, night vision, Garmin GPS, Garmin watch, izlid, rangefinder, 3rd party military vehicle and mission integration. Video is confidential, private demo may be available upon request.",
		"video" : { 
			"source": "https://player.vimeo.com/video/399474483", 
			"image" : "" 
		},
		"images" : [	
		],
	})
	obj['works'].append({
		"title" : "Space Frog VR",
		"background" : "spacefrog_background.jpg",
		"position" : "Developer, Game Designer",
		"link" : "https://store.steampowered.com/app/978650/SpaceFrog_VR/",
		"date" : "2018 Q1 - Q4",
#		"subtitle" : "A Virtual Reality fitness game in collaboration with Alex Goldman",
		"description" : "A VR Active Fitness game in collaboration with Alex Goldman, which engages the player to utilize the body and controllers in motion throughout the full play area (2 x 3 meters)",
		"video" : { 
			"source": "https://player.vimeo.com/video/305282073", 
			"image" : "sf1.png" 
		},
		"images" : [	
			{"img":"sf5.png"},
			{"img":"sf6.png"},
			{"img":"sf7.png"},
			{"img":"sf8.png"},
		],
	})
	obj['works'].append({
		"title" : "Humon AI Company",
		"video" : { 
			"source": "https://player.vimeo.com/video/250308773", 
			"image" : "sf1.png" 
		},
		"background" : "hi3.png",
		"position" : "Developer",
		"link" : "",
		"date" : "2017 Q4",
		"subtitle" : "",
		"description" : "Robots are controlled using human inputs in Virtual Reality, and can be trained on the data gathered by human inputs (using Vive controllers)",
		"images" : [	
			{"img":"hi1.png"},
			{"img":"hi2.png"},
			{"img":"hi3.png"},
			{"img":"hi4.png"},
#			{"video" : { "source": "https://player.vimeo.com/video/246606943", "image" : "vb1.png" }},
#			{"img":"vb2.png"},
#			{"img":"vb3.png"},
#			{"img":"vb4.png"},
		],	
	})
	obj['works'].append({

		"title" : "Super Math World",
		"video" : { "source": "https://player.vimeo.com/video/219464062", "img" : "smw_1.jpg" },
		"background" : "smw_2.jpg",
		"link" : "https://supermathworld.com",
		"date" : "2016 Q1 - 2017 Q3",
		"position" : "Founder, CTO",
#		"subtitle" : "A WebGL based math sandbox",
		"description" : "A math sandbox video game for grades 2 - 8 which allows users to edit, create, and share game content from directly inside the application, natively in a web browser.",
		"responsibilities" : 
		[
				"Unity c# framework architecture",
				"Game design & programming",
				"Web backend (python, django, MySQL, AWS)",
		],
		"images" : [
			{ "img" : "smw_1.jpg" },
			{ "img" : "smw_3.jpg"},
			{ "img" : "smw_4.jpg"},
			{ "img" : "smw_3.jpg"}
		],	
		})
	obj['works'].append({
		"title" : "Gamified AR mesh mapping",
		"background" : "mm_background.jpg",
		"position" : "Consultant, Designer, Programmer",
                "date" : "2018 Q3",
		"link" : "http://vertical.ai/",
		"description" : "PlaceNote is a platform for AR developers, many of whom need prefabs and techniques to get started for guiding the end user to optimal mapping behaviors. I wrote an extension to the PlaceNote SDK that includes prefabs for developers to help them achieve this.",
		"video" : { 
			"source": "https://player.vimeo.com/video/294704893", 
			"image" : "mm_background.jpg" 
		},
		"images" : [	
			{"img":"mm_1.jpg"},
			{"img":"mm_2.jpg"},
			{"img":"mm_3.jpg"},
			{"img":"mm_4.jpg"},
		],
	})

	obj['works'].append({
		"title" : "Visualizing Molecular Machines",
		"background" : "mm_background.jpg",
		"position" : "Developer, Graphic Designer",
		"link" : "https://foresight.org/nanotechnology-leading-to-molecular-machines/",
                "date" : "2018 Q1",
#		"subtitle" : "A Virtual Reality fitness game in collaboration with Alex Goldman",
		"description" : "Based on projects designed by the Foresight Institute's May 2018 Molecular Machines workshop",
		"video" : { 
			"source": "https://player.vimeo.com/video/273109330", 
			"image" : "mm_background.jpg" 
		},
		"images" : [	
			{"img":"mm_1.jpg"},
			{"img":"mm_2.jpg"},
			{"img":"mm_3.jpg"},
			{"img":"mm_4.jpg"},
		],
	})
	obj['works'].append({
		"title" : "Enterprise Training in VR",
		"background" : "mm_background.jpg",
		"position" : "Consultant, Designer, Programmer",
                "date" : "2018 Q2",
		"link" : "http://tryvantagepoint.com/",
		"description" : "As interim CTO I led the development of Vantage Point, a VR harassment enterprise training application. Note the video is private at the request of the company - video demo available on request.",
		"video" : { 
			"source": "https://player.vimeo.com/video/294705276", 
			"image" : "mm_background.jpg" 
		},
		"images" : [	
			{"img":"mm_1.jpg"},
			{"img":"mm_2.jpg"},
			{"img":"mm_3.jpg"},
			{"img":"mm_4.jpg"},
		],
	})

#	obj['works'].append({
#		"title" : "Village Builder",
#		"background" : "vb1.png",
#		"position" : "Developer, Designer",
#		"link" : "",
#		"year" : "2017",
#		"subtitle" : "",
#		"description" : "A LightLodges.com production for communal coherence, village building and sustainable communities. Precursor to a live Mixed Reality gameshow coming 2018", 
#		"video" : { "source": "https://player.vimeo.com/video/246606943", "image" : "vb1.png" },
#	
#		"images" : [	
#			{"img":"vb1.png"},
#			{"img":"vb2.png"},
#			{"img":"vb3.png"},
#			{"img":"vb4.png"},
#		],	
#	})
	obj['works'].append({
		"title" : "Cell Explorer VR",
		"background" : "mm_background.jpg",
		"position" : "Consultant, Designer, Programmer",
		"link" : "http://vertical.ai/",
		"description" : "As a big believer in video games as the best medium for learning, I also believe VR takes this one step further. This is an experimental immersive experience to teach about the makeup of a cell with labeled organelles.",
		"video" : { 
			"source": "https://player.vimeo.com/video/294705147", 
			"image" : "mm_background.jpg" 
		},
		"images" : [	
			{"img":"mm_1.jpg"},
			{"img":"mm_2.jpg"},
			{"img":"mm_3.jpg"},
			{"img":"mm_4.jpg"},
		],
	})
	obj['works'].append({
		"title" : "Magic Hands",
		"background" : "mm_background.jpg",
		"position" : "Consultant, Designer, Programmer",
		"link" : "http://vertical.ai/",
		"description" : "Using Vive and Leap Motion, I built a prototype game that lets you portal between worlds, and recognizes hand gestures for casting magic spells.", 
		"video" : { 
			"source": "https://player.vimeo.com/video/294705016", 
			"image" : "mm_background.jpg" 
		},
		"images" : [	
			{"img":"mm_1.jpg"},
			{"img":"mm_2.jpg"},
			{"img":"mm_3.jpg"},
			{"img":"mm_4.jpg"},
		],
	})
	obj['works'].append({
		"title" : "Mouse Brain Explorer",
		"background" : "mouse4.png",
		"video" : { "source": "https://player.vimeo.com/video/117482417", "img" : "3scan_1.jpg" },
		"link" : "https://3scan.com",
		"date" : "2015 Q1",
		"position" : "Developer",
		"subtitle" : "Fly through a real mouse brain",
		"description" : "Using a cubic centimeter of a mouse brain imaged with 3Scan's equipment, I made a virtual reality tour through the vasculature and a mini-game to destroy blood clots. This was on exhibit during the Exploratorium's science week in 2015.",
		"images" : [
			{"img":"mouse2.png"},
			{"img":"mouse3.png"},
			{"img":"mouse1.png"},
			{"img":"mouse4.png"},
			
		],	
	})	
#	obj['works'].append({
#		"title" : "Ring Flight",
#		"link" : "",
#		"year" : "2012",
#		"position" : "Developer",
#		"subtitle" : "Fly through rings",
#		"description" : "Made at a Kinect hackathon in 2012, this was my first experience integrating external hardware to a Unity game and capturing motion data as player input. In this game you fly through rings of different colors by tilting your body in the direction you wish to steer (lean forwards and backwards for pitch, left and right for yaw)",
#		"images" : [
#			
#		],	
#	})	
	obj['works'].append({
		"title" : "Mathbreakers",
		"video" : { "source": "https://player.vimeo.com/video/73754523", "img" : "mb_1.jpg" },
		"background" : "mb_1.png",
		"link" : "https://mathbreakers.com",
		"date" : "2013 Q3 - 2015 Q4",
		"position" : "Co-Founder",
		"subtitle" : "A math puzzle platformer for grades 2 - 8",
		"description" : "We partnered with some of the biggest names in math education, including Dan Meyer and Jo Boaler, to discover the intersection between 3-D action gaming and elementary mathematics. The result was a truly immersive, stress free math game that kids love to play.",
		"responsibilities" : 
		[
			"Game design & programming",
			"Strategic partnerships",
		],
		"images" : [
			{ "img" : "mb_1.jpg"},
			{ "img" : "mb_2.jpg"},
			{ "img" : "mb_3.jpg"},
			{ "img" : "mb_4.jpg"}
		],	
		})
#	obj['works2'] = []
#	obj['works2'].append({
#		"title" : "Coffee Command ARKit",
#		"position" : "Developer/Designer",
#		"link" : "",
#		"year" : "2017",
#		"subtitle" : "A passive multiplayer base control game",
#		"description" : "Your phone becomes a ship which can attack bases and drones at your favorite coffee shop in a 3-D shooter style game. Once you clear the area, you can build your own turrets to deter other players and control the area, and mine resources from areas you control to become more powerful.",
#		"images" : [
#			{"img":"coffeecommand1.png"},
#			{"img":"coffeecommand2.png"},
#			{"img":"coffeecommand3.png"},
#		],	
#	})
#	obj['works2'].append({
#		"title" : "Magic Hands VR",
#		"position" : "Developer/Designer",
#		"link" : "",
#		"year" : "2017",
#		"subtitle" : "An action game for Vive/Oculus + LeapMotion",
#		"description" : "Use your hands to cast spells and open portals to other worlds.",
#		"images" : [	
#			{"video" : { "source": "https://player.vimeo.com/video/241614660", "image" : "" }},
#			{"img":"magichands1.png"},
#			{"img":"magichands2.png"}
#		],	
#	})
#	obj['works2'].append({
#		"title" : "Space Archer VR",
#		"position" : "Developer/Designer",
#		"link" : "",
#		"year" : "2017",
#		"subtitle" : "An action game for Vive/Oculus",
#		"description" : "Fly around in 3D space and shoot drones and space-men with your bow and arrow.",
#		"images" : [	
#			{"video" : { "source": "https://player.vimeo.com/video/230824116", "image" : "" }},
#			{"img":"archer2.png"},
#			{"img":"archer1.png"}
#		],	
#	})
#	obj['works'].append({
#		"title" : "Fitness Cube VR",
#		"link" : "",
#		"year" : "2017",
#		"subtitle" : "An exercise game for Vive/Oculus",
#		"description" : "Cubes fly at you, and you smash them with your fists! Duck and dodge to prevent losing health.",
#		"images" : [
#			{"video" : { "source": "https://player.vimeo.com/video/230823053", "img" : "fitness2.png" }},
#			{"img":"fitness1.png"},
#		],	
#	})

#	obj['works2'].append({
#		"title" : "Radian.ai",
#		"link" : "http://radian.ai",
#		"year" : "2017",
#		"position" : "Consultant",
#		"description" : "Consulting for VR and AR applications, including project management, enterprise sales, experience design, and full stack development. ",
#		"responsibilities" : 
#		[
#		],
#		"images" : [
#			{ "img" : "radian_logo.png", "class" : "contain square", "link" : "http://radian.ai"},
#		],	
#	})
	obj['works'].append({
		"title" : "Fractal Games",
		"link" : "https://fractalgames.com (old)",
		"year" : "2010 - 2011",
		"position" : "Founder",
		"subtitle" : "An iOS game development studio.",
		"description" : "I led a small team of developers and artists to design and publish two titles, \"Santa's Last Stand\" and \"Bank Defense\" for iOS." ,
		"responsibilities" : 
		[
			"Game design & programming",
			"Hired and managed art team",
		],
		"images" : [	
			{"img": "fg.png","class":"contain"},
			{"img" : "bd1.png"},
			{"img" : "bd2.png"},
			{"img" : "bd3.png"},
			{"img" : "sls1.png"},
			{"img" : "sls2.png"}
			],	
		})
	obj['works'].append({
		"title" : "Startup Grid (Hactus)",
		"link" : "https://startupgrid.net",
		"year" : "2012",
		"position" : "Founder",
		"description" : "One of my first solo projects, a search-and-filter website for exploring the startup landscape and searching for new opportunities. The startup data is scraped from CrunchBase. The original vision was to provide startups a go-to resource for funding, incubators, and other opportunities.",
		"images" : [{"img":'startupgrid.png', "link":"http://startupgrid.net"}],	
		})
	obj['works'].append({
		"title" : "Code Hero",
		"link" : "https://codehero.org",
		"year" : "2011",
		"position" : "Contractor",
		"description" : "I led production of the first 3D version of Code Hero, in which you learn programming by editing the world around you in real time using a javascript laser.",
	"images" : [
			{"img":"codehero.png"},
		],	

	})	
					
#	obj['social'] = [
#		{ "name" : "github.com/vn2", "link" : "https://github.com/vn2" },
#		{ "name" : "linkedin.com/in/vn2", "link" : "https://www.linkedin.com/in/vn2" },
#		{ "name" : "facebook.com/vn2", "link" : "https://www.facebook.com/vn2" },
#		{ "name" : "twitter.com/@vn2", "link" : "https://twitter.com/@vn2" },
#		{ "name" : "angel.co/supermathworld", "link" : "https://angel.co/supermathworld" },
#		{ "name" : "soundcloud.com/vn2", "link" : "https://soundcloud.com/vn2" },
#	]

	return renderWithNav(request,'home.html', obj)

def file_a(request):
	return HttpResponse("7GN_wPd4X1PrCxmqKOrw9sHsAd0_uayFhOnWdEw6Ytc.HrFduo8MJADNQACN38q371h8yDpWwuARiTcP3lgNOOM")

def file_b(request):
	return HttpResponse("Z9DF236bXRfXjvGlUflaI98PMWAKsG9qpGnrDXllb2o.HrFduo8MJADNQACN38q371h8yDpWwuARiTcP3lgNOOM")	


def test(request):
    return renderWithNav(request,"test.html", {})

