#!/usr/bin/env python3

from bookstack import bookstack_api
import os,sys

# Copyright 2022 GNU Public License v2


# Variables for your bookstack install and api

bookstack_protocol="http"
bookstack_host="hostname"
bookstack_port="port"
bookstack_api_secret_id="api-secret-id"
bookstack_api_secret="api-secret"


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

# Read the SUMMARY.md file to determine chapter / page layout and import pages into Bookstack

f=open(filepath+"/SUMMARY.md")
for line in f:
	line=line.strip("\n")
	if "-" in line and ".md" in line.lower():
		# We have a link to a page that we need to go get and recreate in Bookstack.
		page_title=line.split("[")[1].split("]")[0]
		page_file=filepath+"/"+line.split("(")[1].split(")")[0]	
		pars={}
		pars["book_id"]=book_id
		if not chapter_id==None:
			pars["chapter_id"]=chapter_id
		pars["name"]=page_title
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
					pars["markdown"]=pars["markdown"].replace(image_name,"https://ems-docs.element.io/"+image_name)
					images.append(image_name)
		pf.close()
		if bs.call_post_api("pages",pars)=="Too big":
			# Append this file to the failure list, but go ahead and put a stub in bookstack.
			pars["markdown"]="Need to fill this in later. The markdown in file "+page_file+" was deemed too large to import via the Bookstack API."
			pagestub=bs.call_post_api("pages",pars)
			failed[page_file]=pagestub["slug"]
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
print()
print("The following files failed to automatically convert via the API due to being too large:")
print
for fail in failed:
	print(fail)
	print("   - Edit at: "+bookstack_protocol+"://"+bookstack_host+":"+bookstack_port+"/books/"+book_slug+"/page/"+failed[fail])
