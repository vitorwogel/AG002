<h1>AG002 - Projeto 2023.1</h1>
<h2>Treinamento de modelos ML classificatórios utilizando o dataset "palmerpenguins"</h2>
<h3>Instituto Nacional de Telecomunicações - Santa Rita do Sapucaí MG.</h3>
<ul>
    <li>
        <h4>Aluno: Vitor André Brochado Wogel da Costa - 49 - GES</h4>
    </li>
    <li>
        <h4>Professor: Renzo Paranaíba Mesquita</h4>
    </li>
</ul>

<h3>Como rodar o projeto?</h3>
<ol>
    <li>Crie uma máquina virtual Python na raiz no repositório clonado:<br><code>python -m venv <i>env</i></code></li>
    <li>Inicie a env:<br><code>source env/Scripts/activate</code></li>
    <li>Instale todas as bibliotecas necessárias:<br><code>pip install -r requirements.txt</code></li>
    <li>Crie uma pasta <i>data</i> dentro de <i>src</i><br><a href="https://raw.githubusercontent.com/marcelovca90-inatel/AG002/main/palmerpenguins.csv" target="_blank">E coloque o download da base de dados nesta pasta</a></li>
    <li>Rode todas as células do Python Notebook <i>main.ipynb</i></li>
    <li>Rode o arquivo <i>app.py</i>:<br><code>python src/app.py</code></li>
    <li>Entre com as features requeridas no terminal e obtenha a previsão do modelo.</li>
</ol>
<h4><a href="https://youtu.be/x5RpMRhX4WI" target="_blank">Link para tutorial no YouTube</a></h4>
<h3>Tipos de dados permitidos na entrada do usuário:</h3>
<table>
  <thead>
    <tr>
      <th>Coluna</th>
      <th>Tipo</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>culmen length mm</td>
      <td>float</td>
    </tr>
    <tr>
      <td>culmen depth mm</td>
      <td>float</td>
    </tr>
    <tr>
      <td>flipper length mm</td>
      <td>int</td>
    </tr>
    <tr>
      <td>body mass g</td>
      <td>int</td>
    </tr>
    <tr>
      <td>island</td>
      <td>string</td>
    </tr>
    <tr>
      <td>sex</td>
      <td>string</td>
    </tr>
  </tbody>
</table>
