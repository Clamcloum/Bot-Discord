❌necessite d'heberger Ollama en local❌

clone le repo
```
git clone https://github.com/Clamcloum/Bot-Discord.git
```

autoriser l'execution de script powershell ( Windows )
```
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
````

créer environnement virtuel et l'activer ( windows )
```
py -m venv venv
.\venv\Scripts\Activate.ps1
```

sur linux
```
source venv/bin/activate
```

Installer les packages
```
pip install -r .\requirements.txt
```

Pour lancer son app sur windows
```
py main.py
```
Sur linux
```
python3 main.py
```
