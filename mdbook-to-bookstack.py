#!/usr/bin/env python3

from bookstack import bookstack_api
import os,sys

# Copyright 2022 GNU Public License v2


# Variables for your bookstack install and api

bookstack_protocol="http"
bookstack_host="host"
bookstack_port="port"
bookstack_api_secret_id="secret_id"
bookstack_api_secret="secret"
bookstack_hosted_domain="mydomain"


# extra_url should be filled in if your mdbook is not hosted at / on a server. This would be all the extra stuff from / to the root
# of your mdbook for the purposes of rewrite rule generation.

extra_url=""

# Establish a bookstack connection

bs=bookstack_api(bookstack_host,bookstack_api_secret_id,bookstack_api_secret)
bs.set_protocol(bookstack_protocol)
bs.set_port(bookstack_port)


# Read the book.toml of the mdbook
pars={}
f=open("book.toml")
for line in f:
	line=line.strip("\n")
	line=line.split("=")
	if "title" in line[0].lower():
		pars["name"]=line[1].rstrip('"').lstrip(' "')
	if "description" in line[0].lower():
		pars["description"]=line[1].rstrip('"').lstrip(' "')
	if "src" in line[0].lower():
		try:
			filepath=line[1].rstrip('"').lstrip(' "')
		except:
			pass

f.close()

# Create the bookstack book.

print("Creating a book named: '"+pars["name"]+"' in Bookstack....")

newbook=bs.call_post_api("books",pars)
book_id=str(newbook["id"])
book_slug=str(newbook["slug"])
chapter_id=None
failed={}


rewrite_rules=open("rewrite.conf","w")

# Read the SUMMARY.md file to determine chapter / page layout and import pages into Bookstack

f=open(filepath+"/SUMMARY.md")
for line in f:
	line=line.strip("\n")
	if "-" in line and ".md" in line.lower():
		# We have a link to a page that we need to go get and recreate in Bookstack.
		page_title=line.split("[")[1].split("]")[0]
		page_filename=line.split("(")[1].split(")")[0]
		page_file=filepath+"/"+page_filename
		special_case=0
		pars={}
		pars["book_id"]=book_id
		if not chapter_id==None:
			pars["chapter_id"]=chapter_id
		pars["name"]=page_title
		# code explicitly for ems-docs repo to allow slugs to be the same as in ems docs
		# nasty hack, but should work
		if "public irc bridges" in pars["name"].lower():
			pars["name"]="morg IRC Bridges"
			special_case=1
		if "public slack bridge" in pars["name"].lower():
			pars["name"]="morg Slack Bridge"
			special_case=2
		pf=open(page_file)
		linecount=0
		# This moves the file past the first line before reading so that we don't have duplicate titles.
		for pfline in pf:
			if linecount>0:
				pars["markdown"]=pf.read()
			linecount=linecount+1
		# fix images
		images=[]
		# Need to parse the markdown to put a proper image url in place.
		for mdline in pars["markdown"].split("\n"):
			if "![" in mdline:
				image_name=mdline.split("(")[1].split(")")[0]
				# Don't replace the image_name more than once.
				if not image_name in images:
					pars["markdown"]=pars["markdown"].replace(image_name,"https://vector-im.github.io/emsdocs-images/"+image_name)
					images.append(image_name)
		pf.close()
		pagestub=bs.call_post_api("pages",pars)
		if pagestub=="Too big":
			# Append this file to the failure list, but go ahead and put a stub in bookstack.
			pars["markdown"]="Need to fill this in later. The markdown in file "+page_file+" was deemed too large to import via the Bookstack API."
			pagestub=bs.call_post_api("pages",pars)
			failed[page_file]=pagestub["slug"]
		else:
			print("Success")
			# Code to handle the special case where slug is not the same as page title.
			if special_case>0:
				mypars={}
				mypars["book_id"]=str(pagestub["book_id"])
				mypars["chapter_id"]=str(pagestub["chapter_id"])
				if special_case==1:
					mypars["name"]="Public IRC Bridges"
				if special_case==2:
					mypars["name"]="Public Slack Bridge"
				bs.call_put_api("pages/"+str(pagestub["id"]),mypars)
		# code to put the requisite rewrite rule in place
		if len(extra_url)>0:
			rewrite_rules.write("\tlocation /"+extra_url+"/"+page_filename.replace(".md",".html")+" {\n")
		else:
			rewrite_rules.write("\tlocation /"+page_filename.replace(".md",".html")+" {\n")
		rewrite_rules.write("\t\treturn 301 $scheme://"+bookstack_hosted_domain+"/books/"+book_slug+"/page/"+pagestub["slug"]+";\n")
		rewrite_rules.write("\t}\n\n")

	elif "-" in line:
		# These were section headers in the SUMMARY.md and don't have an equivalent in bookstack.
		pass
		#print("Ignore these lines")
	else:
		# We have the start of a chapter and need to create it in bookstack.
		chapter_name=line.lstrip("# ")
		if not len(chapter_name)==0:
			pars={}
			pars["book_id"]=str(book_id)
			pars["name"]=chapter_name
			newchapter=bs.call_post_api("chapters",pars)
			chapter_id=str(newchapter["id"])

f.close()
rewrite_rules.close()
print()
print("The following files failed to automatically convert via the API due to being too large:")
print
for fail in failed:
	print(fail)
	print("   - Edit at: "+bookstack_protocol+"://"+bookstack_host+":"+bookstack_port+"/books/"+book_slug+"/page/"+failed[fail])
