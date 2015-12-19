# -*- coding: utf-8 -*-
from thonny.globals import get_workbench
from subprocess import Popen
import sys
import os.path
import shlex
from thonny.plugins.system_shell.explain_environment import CURRENT_PYTHON_EXEC_PREFIX_KEY



def prepare_windows_environment():
    # In Windows, Python binaries are in different directories
    # and those directories contain only Python related stuff,
    # so it's safe to 
    env = os.environ.copy()
    
    def keep_path_item(x):
        dir_path = shlex.split()[0] 
        dir_items = set(os.listdir(dir_path))
        forbidden_items = {"python", "pythonw",
                           "python3", "python2.7"}
        #if  
    
    path_items = filter(keep_path_item, env.get("PATH", "").split(os.pathsep))
    
    current_interpreter_bin_dir = ...
    path_items.insert(0, ) 

def open_system_shell():
    open_system_shell_unix()

def open_system_shell_unix():
    env = os.environ.copy()
    path = env.get("PATH", "")
    env["PATH"] = os.path.join(sys.exec_prefix, "bin") + os.pathsep + path
    env[CURRENT_PYTHON_EXEC_PREFIX_KEY] = sys.exec_prefix
    env["SSS"] = "SSS"
                   
    explainer = os.path.join(os.path.dirname(__file__), "explain_environment.py")
    
#    Popen("""osascript -e 'tell application "Terminal" to do script "%s"'""" 
    #Popen("""open -a Terminal . ; osascript -e 'tell application "Terminal" to activate in window 1' """, env=env, shell=True) 
    
    Popen("""osascript -e 'tell application "Terminal" to do script "%s %s"' ;  osascript -e 'tell application "Terminal" to activate'""" 
          % (sys.executable, explainer)
          ,
          env=env, shell=True)

    #script = os.path.join(os.path.dirname(__file__), "scr.scpt")
    #Popen(["/usr/bin/osascript",  script] 
    #      #% explainer
    #      ,env=env, shell=False)

def open_system_shell_windows():
    env = os.environ.copy()
    path = env.get("PATH", "")
    env["PATH"] = (sys.exec_prefix + os.pathsep
                   + os.path.join(sys.exec_prefix, "Scripts") + os.pathsep
                   + path)
    env[CURRENT_PYTHON_EXEC_PREFIX_KEY] = sys.exec_prefix
                   
    explainer = os.path.join(os.path.dirname(__file__), "explain_python_env.bat")
    Popen('start "Shell for using %s" /w "%s"' % (sys.exec_prefix, explainer),
          env=env, shell=True)
    

def load_plugin():
    get_workbench().add_command("OpenSystemShell", "tools", "Open system shell",
                    open_system_shell, group=80)