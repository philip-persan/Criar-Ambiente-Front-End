import os
from time import process_time_ns

root = os.getcwd()

project_name = input('Qual o nome do Projeto? ')

caminho = os.path.join(root, project_name)

# Cria a pasta do projeto
os.mkdir(caminho)
print(f'Criada a pasta do projeto "{project_name}"')

# Cria a pasta CSS
css = os.path.join(caminho, 'css')
os.mkdir(css)
print(f'Criada a pasta "CSS"')
caminhoCss = str(css) + '\style.css'
arquivo_css = open(caminhoCss, 'w+')
arquivo_css.close
print(f'Criado o arquivos "Style.css"')


# Cria a pasta JS
js = os.path.join(caminho, 'js')
os.mkdir(js)
print(f'Criada a pasta "JS"')

# Cria a pasta src, images, videos, icons
src = os.path.join(caminho, 'src')
os.mkdir(src)
srcImages = os.path.join(src, 'images')
os.mkdir(srcImages)
srcVideos = os.path.join(src, 'videos')
os.mkdir(srcVideos)
srcIcons = os.path.join(src, 'icons')
os.mkdir(srcIcons)
print(f'Criada a pasta "SRC"')

# Cria index.html
caminhoI = str(caminho)
indexCaminho = caminho + '\index.html'
index = open(indexCaminho, 'w+')
print(f'Criado arquivo "index.html"')

vscode = input('Deseja abrir o VsCode? Y/N ')
vscodePath = str(f'code .\{project_name}')


if vscode == 'Y' or vscode == 'y':
    os.system(vscodePath)
else:
    print(f'Pastas e arquivos do Projeto: "{project_name}" criados.')


