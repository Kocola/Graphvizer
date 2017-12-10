import sublime
import sublime_plugin
import functools
import syntaxchecker


# Trigged when user input text
class UserEditListener(sublime_plugin.EventListener):
	def on_modified(self, view):
		# Detect language. Only process DOT file.
		file_syntax = view.settings().get('syntax')
		if "DOT.sublime-syntax" not in file_syntax:
			return
		# Get the contents of the whole file
		region = sublime.Region(0, view.size())
		contents = view.substr(region)
		syntaxchecker.check(contents)

#
class GraphvizerCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		pass
