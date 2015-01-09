#!/usr/bin/python
import os, sys, re

# This script is a part of the 'A Byte of Python' book source.
# It colorizes the Python program listings in the XHTML output
# by the DocBook XML source combined with DocBook XSL stylesheets.
# It was written by Swaroop C H <swaroop@byteofpython.info>
# It is under the public domain. Use it for any purpose you want.

# *WARNING* : If you are using VIM, run :set nolist to return to normal usage
# of VIM.

############### Utility Functions ##############################################
def run(cmd, verbose='verbose'):
	'''Run a command.'''
	if verbose != 'quiet':
		print cmd
	if os.system(cmd) != 0:
		print '\nFailed.'
		sys.exit()


############### Transformation Procedures ######################################
def is_keyword(s):
	'''Check for keyword.'''
	# List of keywords
	keywords = ('print', 'return', 'break', 'continue', 'pass',
		'if', 'else', 'elif', 'while', 'for', 'in', 'not',
		'is', 'def', 'class', 'from', 'import', 'del',
		'try', 'except', 'finally', 'lambda', 'global')
	# Match at beginning of string
	m = re.match('|'.join(keywords), s)
	if m is not None:
		if not s[m.end()].isalpha():
			return m.end() - m.start() # Return length of keyword
	return 0

def is_builtin(s):
	'''Check for builtin.'''
	# List of builtins
	builtins = ('int', 'raw_input', 'True', 'False', 'range',
		'len', 'os', 'sys', 'time', 'self', 'cPickle',
		'file', 'None')

	# Match at beginning of string
	m = re.match('|'.join(builtins), s)
	if m is not None:
		if not s[m.end()].isalpha():
			return m.end() - m.start() # Return length of builtin
	return 0

def is_string(s):
	'''Check for string.'''
	start = 0

	# Manual Lexing used here instead of regexps
	if s[0] in 'rR':
		start = 1

	# Match """abc""" BUT REMEMBER THAT " WILL BE REPRESENTED AS &quot;
	if s[start:start+18] == '&quot;&quot;&quot;':
		triple = s[start:start+18]
		pos = start + 18
		while s[pos:pos+18] != triple:
			pos += 1
			assert pos < len(s)
		return pos + 18

	# Match '''abc'''
	if s[start:start+3] == "'''":
		triple = s[start:start+3]
		pos = start + 3
		while s[pos:pos+3] != triple:
			pos += 1
			assert pos < len(s)
		return pos + 3

	# Match "abc" BUT REMEMBER THAT " WILL BE REPRESENTED AS &quot;
	if s[start:start+6] == '&quot;':
		pos = start + 6
		while True:
			if s[pos:pos+6] == '&quot;':
				return pos + 6
			else:
				pos += 1
				assert pos < len(s)

	# Match "abc" in case it is represented as "
	if s[start] == '"':
		pos = start + 1
		while True:
			if s[pos] == '"' and s[pos-1] != '\\':
				return pos + 1
			else:
				pos += 1
				assert pos < len(s)

	# Match 'abc'
	if s[start] == "'":
		pos = start + 1
		while True:
			if s[pos] == "'" and s[pos-1] != '\\':
				return pos + 1
			else:
				pos += 1
				assert pos < len(s)

	return 0

def is_word(s):
	'''Check for any kind of identifier.'''
	m = re.match(r'\w+', s)
	if m is not None:
		return m.end() - m.start()
	return 0

def is_number(s):
	'''Check if it is a number.'''
	m = re.match(r'\d+', s)
	if m is not None:
		return m.end() - m.start()
	return 0

def lex(s):
	'''Lexically analyze the program and add syntax highlighting.'''
	i = 0
	content = ''

	while i < len(s):
		flag = False # A flag for whether this pass of lexing is done

		if flag == False and s[i] == '#': # Highlight comments
			newline = s.find('\n', i)
			content += '<span class="py-comment">%s</span>' % s[i:newline]
			i = newline # Continue with '\n'
			flag = True

		if flag == False and s[i] in tuple("'rR"): # Highlight strings
			length = is_string(s[i:])
			if length > 0:
				content += '<span class="py-string">%s</span>' \
							% s[i:i+length]
				i += length
				flag = True

		if flag == False and s[i:i+6] == "&quot;": # Highlight strings
			length = is_string(s[i:])
			if length > 0:
				content += '<span class="py-string">%s</span>' \
							% s[i:i+length]
				i += length
				flag = True

		if flag == False and s[i] == '"': # Highlight strings
			length = is_string(s[i:])
			if length > 0:
				content += '<span class="py-string">%s</span>' \
							% s[i:i+length]
				i += length
				flag = True


		if flag == False:
			length = is_keyword(s[i:]) # Highlight keywords/statements
			if length > 0:
				content += '<span class="py-statement">%s</span>' \
							% s[i:i+length]
				i += length
				flag = True

		if flag == False:
			length = is_builtin(s[i:]) # Highlight built-in classes, etc.
			if length > 0:
				content += '<span class="py-builtin">%s</span>' \
							% s[i:i+length]
				i += length
				flag = True

		if flag == False:
			length = is_number(s[i:]) # Highlight numbers, etc.
			if length > 0:
				content += '<span class="py-number">%s</span>' \
							% s[i:i+length]
				i += length
				flag = True

		if flag == False:
			length = is_word(s[i:]) # Leave whole words as is
			if length > 0:
				if s[:i].endswith('def ') or \
					s[:i].endswith('class '):
					content += '<span class="py-identifier">%s</span>' \
								% s[i:i+length]
				else:
					content += s[i:i+length]
				i += length
				flag = True

		if flag == False:
			content += s[i] # Default handler
			i += 1
			flag = True

	return content

def syntax_highlight(m):
	'''Syntax Highlighting for Python programs.'''
	content = m.group()
	content = content[28:-6] # Remove <pre> and </pre>

	content = lex(content) # Lexically analyze the program

	# Add the starting and ending tags
	return '<pre class="programlisting">' + content + '</pre>'

def transform(content):
	'''Transform the content for the customizations required.'''

	# Add Header
	content = re.sub('(<body>)', '''\
\\1
<div class="header">
<strong><a href="http://www.byteofpython.info/" class="header-link">A Byte of Python</a></strong>
</div>
''', content)

	# Change mailto: links to prevent site scraping by spammers
	content = content.replace( \
		'<a href="mailto:swaroop@byteofpython.info">swaroop@byteofpython.info</a>',
		'<strong>swaroop (at) byteofpython.info</strong>')

	# Add Syntax Highlighting
	content = re.sub('''<pre class="programlisting">([^<]+)</pre>''',
						syntax_highlight, content)

	# Finished transforming content
	return content

############### Start of script ################################################
# Check if usage is correct
if len (sys.argv) != 2:
	print 'Usage: bytecolorizer.py foo.html'
	sys.exit(2)

	# Check if the HTML file exists
	if not os.path.exists(sys.argv[1]):
		print 'The file "%s" does not exist.' % sys.argv[1]
		sys.exit(3)

# Get filenames
outhtml = sys.argv[1]
inhtml = outhtml + '.tmp'
os.rename(outhtml, inhtml)

# Read input
input = file(inhtml)
content = input.read()
input.close()

# Do the transformation dance
content = transform(content)

# Write out the output
output = file(outhtml, 'w')
output.write(content)
output.close()

# Validate XHTML file
# For some reason, xmllint is not working properly on FC3 :(
#dtd = '/usr/share/sgml/xhtml1/xhtml1-20020801/DTD/xhtml1-transitional.dtd'
#if os.path.exists(dtd):
#	run('xmllint --noout --postvalid --dtdvalid %s %s' % (dtd, outhtml), 'quiet')
#	print 'Validated', outhtml

# Remove the original file
os.remove(inhtml)

# The End
# vim: smartindent noexpandtab tabstop=8 list
