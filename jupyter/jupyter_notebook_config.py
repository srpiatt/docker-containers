# Configuration file for notebook.

c = get_config()  #noqa

# remove password and token prompt
c.NotebookApp.token = ''
c.NotebookApp.password = u''
c.NotebookApp.open_browser = True
c.NotebookApp.ip = 'localhost'