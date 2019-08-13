This is the pyInstaller section of the exeDev repo. Showing promising results in dev for windows AND unix executables. 
Below will be some now general documentation about his process  

for the error "no module distutils" (paraphrase):  
	add:   
	# work-around for https://github.com/pyinstaller/pyinstaller/issues/4064  
	import distutils 
	if distutils.distutils_path.endswith('__init__.py'):  
    	distutils.distutils_path = os.path.dirname(distutils.distutils_path)  

at the top of the .spec file. Importantly then run  
	$pyinstaller (filename).spec  


If you have issues with numpy when running the exe, change your version ot 1.16.4 (I believe this is right, check with sam). This seems to fix it. I have put up an issue and will see what there response is.  

Hopefully sam adds to *this*!  


hellotest: simplest example . Just prints 'hello world in the console'

matplottest: secondary test using numpy and matplotlib to make an executable

pygametest1: simplest pygame example. This is a one folder type development

pygametest2: same pygame example. this is a one file type development

runtimetest: this was taken from the docs. Very helpful in figuring out how frozen development works at runtime. In particular sys._MEIPASS


screenshots: screenshots of terminal after runtimetests in various different modes

Notes on --onefile:
	make sure to clear pycache, dist and build before building. 

Due to the way the build process, I will post here what the data section has incase deleted:
datas=[('images/sideMenuBox.png','./images'),('fonts/FreeSansBold.ttf','./fonts')],


