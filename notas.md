# Principais Comandos do PyAutoGUI

## Movimento do Mouse:
- **`py.moveTo(x, y)`**: Move o cursor do mouse para as coordenadas especificadas (x, y).
- **`py.move(x, y)`**: Move o cursor do mouse em relação à posição atual.
- **`py.dragTo(x, y)`**: Arrasta o mouse até as coordenadas (x, y).
- **`py.drag(x, y)`**: Arrasta o mouse em relação à posição atual.
- **`py.click(x, y)`**: Clica nas coordenadas especificadas.
- **`py.doubleClick(x, y)`**: Dá um clique duplo nas coordenadas especificadas.
- **`py.rightClick(x, y)`**: Dá um clique com o botão direito nas coordenadas especificadas.
- **`py.middleClick(x, y)`**: Dá um clique com o botão do meio nas coordenadas especificadas.

## Teclado:
- **`py.typewrite('texto')`**: Digita o texto no campo ativo.
- **`py.press('tecla')`**: Pressiona uma tecla (exemplo: `'enter'`, `'tab'`, `'esc'`).
- **`py.keyDown('tecla')`**: Pressiona uma tecla e mantém pressionada.
- **`py.keyUp('tecla')`**: Solta a tecla que foi pressionada.
- **`py.hotkey('ctrl', 'c')`**: Pressiona uma combinação de teclas (exemplo: `Ctrl+C`).

## Captura e Localização de Imagens na Tela:
- **`py.locateOnScreen('imagem.png')`**: Localiza uma imagem na tela e retorna as coordenadas.
- **`py.locateCenterOnScreen('imagem.png')`**: Localiza a imagem e retorna o centro da imagem.
- **`py.center(campo)`**: Retorna o centro das coordenadas de uma área (campo é um objeto com as coordenadas retornadas por `locateOnScreen`).
- **`py.pixel(x, y)`**: Retorna a cor do pixel na posição (x, y).
- **`py.screenshot()`**: Faz uma captura de tela e retorna uma imagem.
- **`py.screenshot('arquivo.png')`**: Salva a captura de tela no arquivo especificado.

## Outros Comandos Úteis:
- **`py.alert('Mensagem')`**: Exibe um alerta com a mensagem fornecida.
- **`py.confirm('Mensagem')`**: Exibe uma janela de confirmação.
- **`py.prompt('Mensagem')`**: Exibe um prompt para o usuário digitar algo.
- **`py.failSafe`**: Se `failSafe` estiver ativado, o script será interrompido quando o mouse for movido para o canto superior esquerdo da tela.
